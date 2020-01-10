import random
from bot.plugins.repeat import rate_plugin


class Repeat:
    group_msg = {}  # 存放复读消息的字典

    max_random = 10000000000  # 随机数最大值
    max_noise_msg_len = 2  # 最大可接受复读被打断的 噪音消息 上限

    is_noise = False  # 判断当前是否是噪音消息

    # 要使用的随机插件
    rand_plugin = rate_plugin.MOD_1
    # 随机插件的参数
    rand_plugin_args = ()
    # 随机插件的命名参数
    rand_plugin_kwargs = {}

    def is_repeat(self, group_id):
        """
        判断是否要复读
        :param group_id:
        :return:
        """
        repeat_msg = self.get_group_msg_prop(group_id, 'repeat_msg')
        allow_repeat = self.get_group_msg_prop(group_id, 'allow_repeat')

        # 当前群的状态是否可以复读
        if allow_repeat is not True:
            return False

        # 是否存在repeat_msg字段
        if repeat_msg is None:
            return False

        # 是否存在复读消息，消息小于等于0则不复读，
        repeat_count = len(repeat_msg)
        if repeat_count <= 0:
            return False

        # 根据当前已复读此处，决定本次复读的概率
        rate = self.get_rate(repeat_count)
        # 用随机数和给定概率，判断是否命中复读
        is_repeat = self.rand_repeat(rate)

        # 如果确定要复读，则这次的复读后面将不在参加，故，将 allow_repeat 设置为 False
        if is_repeat:
            self.set_group_msg_prop(group_id, 'allow_repeat', False)

        # 每次执行完复读判断后都要重置噪音的判断值
        self.is_noise = False

        return is_repeat

    def get_rate(self, repeat_count):
        """
        :param repeat_count:
        :return:
        """
        return rate_plugin.set_plugin(self.rand_plugin, repeat_count, *self.rand_plugin_args, **self.rand_plugin_kwargs)

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

    def push_group_msg(self, group_id, msg, run_repeat=True):
        """
        将用户消息放入复读列表
        :param group_id:
        :param msg:
        :param run_repeat:
        :return:
        """

        # 如果消息组不存在群，创建他
        if group_id not in self.group_msg.keys():
            self.group_msg[group_id] = {
                'allow_repeat': True,
                'repeat_msg': [],
                'noise_msg': [],
            }

        # 在执行插入操作前，先判定当前的复读的各项属性的状态，并根据情况重置他们
        if len(self.group_msg[group_id]['repeat_msg']) > 0:
            self.check_allow_repeat_status(group_id, msg)

        # 不是噪音的话，才插入复读列表
        if self.is_noise is False:
            self.group_msg[group_id]['repeat_msg'].append(msg)

        # 如果 run_repeat 为 True，则本方法结束后将自动调用 is_repeat 方法并返回复读的判断结果
        if run_repeat is True:
            return self.is_repeat(group_id)

    def get_group_msg_prop(self, group_id, prop):
        """
        获取 self.group_msg 的属性，属性不存在时，返回 None
        :param group_id:
        :param prop:
        :return:
        """
        if group_id not in self.group_msg.keys():
            return None

        if prop not in self.group_msg[group_id].keys():
            return None

        return self.group_msg[group_id][prop]

    def set_group_msg_prop(self, group_id, prop, value):
        """
        设置 self.group_msg 的属性值
        :param group_id:
        :param prop:
        :param value:
        :return:
        """
        if group_id not in self.group_msg.keys():
            return

        if prop not in self.group_msg[group_id].keys():
            return

        self.group_msg[group_id][prop] = value

    def set_group_msg_noise(self, group_id, noise_msg):
        """
        判断并设置复读噪音
        复读噪音：
        在别人复读的时候，有人乱入，打乱了队形，这些消息称之为：复读噪音
        :param group_id:
        :param noise_msg:
        :return:
        """
        # 将噪音消息插入，然后进行判断，如果噪音消息列表长度超过 self.max_noise_msg_len 则认为复读中断
        # 未中断，返回 True ，意味着插入噪音成功
        # 中断，返回 False，意味着插入噪音失败
        self.group_msg[group_id]['noise_msg'].append(noise_msg)
        noise_msg_list = self.get_group_msg_prop(group_id, 'noise_msg')
        if len(noise_msg_list) > self.max_noise_msg_len:
            return False
        else:
            return True

    def check_allow_repeat_status(self, group_id, current_msg):
        """
        确认复读队列的状态，依据情况复读队列可能会被重置一些属性
        :param group_id:
        :param current_msg:
        :return:
        """
        repeat_msg_list = self.get_group_msg_prop(group_id, 'repeat_msg')

        repeat_count = len(repeat_msg_list)
        if repeat_count > 0:
            repeat_msg = repeat_msg_list[0]
        else:
            return

        is_init = False
        if repeat_msg != current_msg:
            if repeat_count >= 2:
                is_out_of_noise_len = self.set_group_msg_noise(group_id, current_msg)
                is_init = not is_out_of_noise_len  # 超出上限返回 False，否则返回True，这里将结果取反赋值给is_init
                self.is_noise = True
            else:
                is_init = True
        else:
            # 如果还在噪音允许范围内，又一次出现了复读语句，那么认为复读被续命了，这时候清空噪音池
            self.set_group_msg_prop(group_id, 'noise_msg', [])

        if is_init:
            self.set_group_msg_prop(group_id, 'allow_repeat', True)
            self.set_group_msg_prop(group_id, 'repeat_msg', [])
            self.set_group_msg_prop(group_id, 'noise_msg', [])
