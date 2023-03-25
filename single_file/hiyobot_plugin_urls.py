from hiyobot import Plugin,Matcher,Matchers
from re import findall
from lxml import html
from requests import get
AUTHOR="Maggie tanhanzesnd@gmail.com"
VERSION=(0,0,1)
plugin=Plugin()
@plugin.build_event(Matcher(Matchers.regex(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')))
def say_hi(session,data):
    links=findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',data.text)
    result=""
    if len(links) >5:
        session.bot.send("Holy wreck, too much URLs")
        return
    for i in links:
        try:
            resp=get(i,timeout=2)
            resp.encoding="utf-8"
            resp=resp.text
        except:
            pass
        data=html.fromstring(resp)
        awa=data.xpath("//title")
        if len(awa) == 0:
            continue
        result+=f">[{awa[0].text}]({i})\n{i}\n\n"
    if result != "":
        session.bot.send(result)
        
exports=plugin.build_exports()
