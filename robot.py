#coding=utf-8
import requests
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


API_KEY = 'fe78ead569e9491fb0a0095c3bd4dbbe'
raw_TULINURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % API_KEY

def ChatBot(word):
    url = 'http://www.tuling123.com/openapi/api'
    data = {'key':API_KEY,
            'info':word,
            'userid':'118022'}
    content = requests.post(url,data=data).content
    return eval(content).get('text')

if __name__ == "__main__":
    #record the voice
    record.my_record()

    #translate the voice to word
    content = listener.Listener('voice/output.wav')

    print 'content:  ',content
    #the robot get result

    result = ChatBot(content)
    print 'speak:  ',result

    #speak the result
    speaker.speak(result.decode('utf8'))

    #save the result_voice
    # speaker.baidu_speak(h.split(':')[1])

