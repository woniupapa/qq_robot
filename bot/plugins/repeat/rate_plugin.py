import random

MOD_1 = 'mod_1'     # 根据复读次数，概率指数级增长
MOD_2 = 'mod_2'     # 可以指定第一次复读几率，以及第二次以后的复读几率
MOD_3 = 'mod_3'     # 可以指定每一次复读的几率，并且可以设置一个未指定的次数的统一值

MOD_CUSTOM = 'mod_custom'   # 完全自定义一个随机函数


def default_plugin():
    return 'mode_1'


global_plugin = default_plugin()


def set_plugin(plugin=None, *args, **kwargs):
    """
    设置使用要使用的插件，不指定则使用默认插件
    :param plugin:
    :return:
    """
    arg_1 = plugin

    try:
        plugin = float(plugin)
    except ValueError:
        pass

    if type(plugin) is str:
        plugin_obj = globals().get(plugin)
        if callable(plugin_obj):
            use_default = False
        else:
            plugin_obj = globals().get(global_plugin)
            use_default = True
    else:
        plugin_obj = globals().get(global_plugin)
        use_default = True

    if use_default:
        rate = plugin_obj(arg_1, *args, **kwargs)
    else:
        rate = plugin_obj(*args, **kwargs)

    # 防止复读几率大于1
    while rate > 1.0:
        rate = rate / 10

    return rate


def mode_1(repeat_count, max_rate=0.8, base_point1=0.99, base_point2=10):
    """
    根据已重复的次数，计算复读的几率，最大的复读几率是 80%
    :param repeat_count:
    :param max_rate 最大复读概率
    :param base_point1: # 复读概率基准参数1
    :param base_point2: # 复读概率基准参数2
    :return: float
    """
    if repeat_count < 1:
        return 0

    p1 = base_point1
    for c in range(1, repeat_count + 1):
        p1 = p1 + 0.9 / (10 ** (1 + c))
    p2 = base_point2 ** (2 * repeat_count - 1)
    rate = 1 - (p1 ** p2)

    # 最大复读概率 80%
    if rate > max_rate:
        return max_rate

    return rate


def mod_2(repeat_count, first=0.05, other=0.7):
    """
    只有两个几率，第一次复读，以及非第一个复读
    :param repeat_count:
    :param first: 作为第一个复读机的几率
    :param other: 作为非第一恶复读机的几率
    :return: float
    """
    if repeat_count < 1:
        return 0

    if repeat_count == 1:
        return first

    return other


def mod_3(repeat_count, *args, **kwargs):
    """
    指定每一次的复读几率，无法调过某个次数
    :param repeat_count:
    other 非指定的复读次数的几率, 不指定的话，就是指定的最后一次的复读几率，如果没有任何指定，始终使用一个预设值
    :return:
    """
    if repeat_count < 1:
        return 0

    default_rate = 0.5

    for times, rate in enumerate(args):
        if repeat_count == times + 1:
            return rate

    if 'other' in kwargs.keys():
        return kwargs['other']
    elif len(args) > 0:
        return args[-1]
    else:
        return default_rate


def mod_custom(repeat_count, custom_func=None, *args, **kwargs):
    """
    自定义一个复读函数
    :param repeat_count:
    :param custom_func:
    :return:
    """
    if not callable(custom_func):
        def default_func(rep_count, *args, **kwargs):
            if rep_count < 1:
                return 0
            r = random.randint(1, 10)
            r = r / 10
            return r

        custom_func = default_func

    return custom_func(repeat_count, *args, **kwargs)
