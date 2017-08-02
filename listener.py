#-*-coding=utf-8-*-

import wave
import urllib, urllib2, pycurl
import base64
import json
## get access token by api key & secret key

def get_token():
    apiKey = "Iu7DRbGRuLyClMuyzV5mbW6y"
    secretKey = "eefe042b38f9e60f53c1ffa27e6ceef9"

    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;

    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']

def dump_res(buf):
    with open('data.txt','wb') as f:
        print buf
        buf = eval(buf)
        if 'result' in buf:
            f.write(buf['result'][0])
        else:
            f.write('error')
#    print buf


## post audio to server
def use_cloud(filename,token):
    fp = wave.open(filename, 'rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)

    cuid = "12:31:c3:81:c5:06" #my xiaomi phone MAC
    srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
    http_header = [
        'Content-Type: audio/pcm; rate=16000',
        'Content-Length: %d' % f_len
    ]

    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url)) #curl doesn't support unicode
    #c.setopt(c.RETURNTRANSFER, 1)
    c.setopt(c.HTTPHEADER, http_header)   #must be list, not dict
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, dump_res)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform() #pycurl.perform() has no return val

if __name__ == "__main__":
    token = get_token()
    use_cloud('vad_0.wav',token)