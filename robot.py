#-*-coding=utf-8-*-
import listener
import win32com.client
import time
import json
import speaker
import sys
import record
import urllib,urllib2
reload(sys)
sys.setdefaultencoding('utf8')


def chating(word,d={}):
    d = {}
    d[u'你好，'] = u'你好'
    d['hello'] = 'hello'
    d['what\'s your name'] = u'siri'
    d[u'天气怎么样，'] = u'晴天哦'
    d['error'] = u'错误'
    try:
#    print word
        reply = d[word.decode('utf-8')].decode('utf-8')
    except:
        reply = u'我不知道你在说什么'
    return reply



API_KEY = 'fe78ead569e9491fb0a0095c3bd4dbbe'
raw_TULINURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % API_KEY

def result(word):
    for i in range(1,100):
        queryStr = word
        TULINURL = "%s%s" % (raw_TULINURL,urllib2.quote(queryStr))
        req = urllib2.Request(url=TULINURL)
        result = urllib2.urlopen(req).read()
        hjson=json.loads(result)
        length=len(hjson.keys())
        content=hjson['text']

        if length==3:
            return 'robots:' +content+hjson['url']
        elif length==2:
            return 'robots:' +content

if __name__ == "__main__":
    record.my_record()
    token = listener.get_token()
    listener.use_cloud('output.wav',token)
    with open('data.txt','rb') as f:
        content = f.read()[:]
    print 'content:  ',content
    h = result(content)
    print 'speak:  ',h
    speaker.speak(h.decode('utf-8').split(':')[1])
    speaker.baidu_speak(h.split(':')[1])

