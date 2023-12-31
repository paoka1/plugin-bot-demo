from plugin.handle import Bot
from plugin.plugin import end_with


# end_with 以特定短语结尾时触发
@end_with(match=["？", "?"], priority=5, block=True)
def talk_sep(bot: Bot, msg: str):
    bot.send_msg("嗯！" + msg[:-2] + "！")
