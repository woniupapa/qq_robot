import random


class Repeat:
    group_msg = {}  # 存放复读消息的字典

    base_point1 = 0.99  # 复读概率基准参数1
    base_point2 = 10    # 复读概率基准参数2
    max_random = 10000000000    # 随机数最大值
    max_noise_msg_len = 2   # 最大可接受复读被打断的 噪音消息 上限

    def is_repeat(self, group_id):
        """
        判断是否要复读

        :param group_id:
        :return:
        """
        repeat_msg = self.get_group_msg_prop(group_id, 'repeat_msg')
        allow_repeat = self.get_group_msg_prop(group_id, 'allow_repeat')
        if allow_repeat is not True:
            return False

        if repeat_msg is None:
            return False

        repeat_count = len(repeat_msg)
        if repeat_count <= 0:
            return False

        rate = self.get_rate(repeat_count)
        is_repeat = self.rand_repeat(rate)

        if is_repeat:
            self.set_group_msg_prop(group_id, 'allow_repeat', False)

        return is_repeat

    def get_rate(self, repeat_count):
        """
        根据已重复的次数，计算复读的几率，目前最大的复读几率是 80%
        :param repeat_count:
        :return:
        """
        if repeat_count < 1:
            return 0

        p1 = self.base_point1
        for c in range(1, repeat_count + 1):
            p1 = p1 + 0.9 / (10 ** (1 + c))
        p2 = self.base_point2 ** (2 * repeat_count - 1)
        rate = 1 - (p1 ** p2)

        # 最大复读概率 80%
        if rate > 0.80:
            return 0.80

        return rate

    def rand_repeat(self, rate):
        """
        根据概率获取是否复读的结果
        :param rate:
        :return:
        """
        num = random.randint(1, self.max_random)

        percent = rate * self.max_random

        if num <= percent:
            return True

        return False

    def push_group_msg(self, group_id, msg):
        if group_id not in self.group_msg.keys():
            self.group_msg[group_id] = {
                'allow_repeat': True,
                'repeat_msg': [],
                'noise_msg': [],
            }

        if len(self.group_msg[group_id]['repeat_msg']) > 0:
            self.check_allow_repeat_status(group_id, msg)
        self.group_msg[group_id]['repeat_msg'].append(msg)

    def get_group_msg_prop(self, group_id, prop):
        if group_id not in self.group_msg.keys():
            return None

        if prop not in self.group_msg[group_id].keys():
            return None

        return self.group_msg[group_id][prop]

    def set_group_msg_prop(self, group_id, prop, value):
        if group_id not in self.group_msg.keys():
            return

        if prop not in self.group_msg[group_id].keys():
            return

        self.group_msg[group_id][prop] = value

    def check_allow_repeat_status(self, group_id, current_msg):
        repeat_msg_list = self.get_group_msg_prop(group_id, 'repeat_msg')


        if len(repeat_msg_list) > 0:
            repeat_msg = repeat_msg_list[0]
        else:
            return

        if repeat_msg != current_msg:
            self.set_group_msg_prop(group_id, 'allow_repeat', True)
            self.set_group_msg_prop(group_id, 'repeat_msg', [])
