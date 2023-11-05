from plugin.handle import Bot
from plugin.plugin import on_keyword
from plugin.plugin import full_match


@on_keyword(match=["hello"], priority=1, block=True)
def helloworld(bot: Bot, _):
    bot.send_msg("hello")


@on_keyword(match=["bye"], priority=1, block=True)
def goodbye(bot: Bot, _):
    bot.send_msg("goodbye~")
    exit()


@full_match(match=["who are you"], priority=1, block=True)
def whoami(bot: Bot, _):
    bot.send_msg("I am " + bot.name)
