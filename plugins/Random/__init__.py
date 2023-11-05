import random

from plugin.handle import Bot
from plugin.plugin import full_match
from plugin.plugin import start_with


@full_match(match=["guess", "猜数字"], priority=1, block=True)
def guess_num(bot: Bot, _):
    my_random = random.randint(1, 10)
    bot.send_msg("一个数生成在1到10之间，请猜测这个数：")
    your_num = bot.rec_msg()
    if not your_num.isdigit():
        bot.send_msg("你输入的不是数字，不和你玩了")
    elif my_random == int(your_num):
        bot.send_msg("你猜对啦")
    else:
        bot.send_msg(f"你猜错了，这个数字是{my_random}")


@full_match(match=["random"], priority=5, block=True)
def random_num(bot: Bot, _):
    bot.send_msg("random num is " + str(random.randint(1, 100)))


# start_with 以特定短语开头时触发
@start_with(match=["hhh", "哈哈哈", "啦啦啦"], priority=10, block=True)
def random_reply(bot: Bot, _):
    reply = ["好", "你说得对", "xs, hhh...", "真的吗？", "哈哈哈"]
    bot.send_msg(random.choice(reply))
