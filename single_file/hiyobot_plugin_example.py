from hiyobot import Plugin,Matcher,Matchers
from random import randint
AUTHOR="Maggie tanhanzesnd@gmail.com"
VERSION=(0,0,1)
plugin=Plugin()
@plugin.build_event(Matcher(Matchers.startswith("hello")))
def say_hi(session,data):
    session.bot.send("hi"*randint(1,9))
exports=plugin.build_exports()