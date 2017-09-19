#coding:utf-8
import win32com.client
import time
import pyaudio

# 引入Speech SDK
from aip import AipSpeech

def speak(word):
    spk = win32com.client.Dispatch("SAPI.SpVoice")
    spk.Speak(word)

def baidu_speak(word):
    # 定义常量
    APP_ID = '9960219'
    API_KEY = 'fYX4rsU7SkPlTOj7RU2H8sqM'
    SECRET_KEY = 'If4aP0dcn3kEenGaUKmoMcgpEGz0vhCs '

    # 初始化AipSpeech对象
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = aipSpeech.synthesis(word, 'zh', 1, {
        'vol': 5,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
    pass

if __name__ == '__main__':
#   speak(u'I\'m siri')
    baidu_speak('a')

