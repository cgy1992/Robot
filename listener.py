#coding=utf-8

import wave
import urllib, urllib2, pycurl
import base64
import json
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '9905446'
API_KEY = 'Iu7DRbGRuLyClMuyzV5mbW6y'
SECRET_KEY = 'eefe042b38f9e60f53c1ffa27e6ceef9'

def Listener(wavFilePath):
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    return aipSpeech.asr(get_file_content('voice/output.wav'), 'pcm', 16000, {
        'lan': 'zh',
    }).get('result')[0]

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

if __name__ == "__main__":
    print Listener('voice/output.wav')
