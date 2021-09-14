import hashlib
import requests

def run1(ssid):
    url="https://ringzer0ctf.com/challenges/13/"
    data=requests.get(url,cookies={"PHPSESSID":ssid}).text
    data=data[data.find('----- BEGIN MESSAGE -----<br />')+len('----- BEGIN MESSAGE -----<br />1234'):data.find('----- END MESSAGE -----')-10]
    print('[%s]'%data)
    data=hashlib.sha512(data.encode()).hexdigest()
    print('[%s]'%data)
    data=requests.get(url+data,cookies={"PHPSESSID":ssid}).text
    data=data[data.find('<div class="alert alert-info">')+len('<div class="alert alert-info">'):]
    data=data.split('</div>')[0]
    print(print('[%s]'%data))
    
def run2(ssid):
    url="https://ringzer0ctf.com/challenges/14/"
    data=requests.get(url,cookies={"PHPSESSID":ssid}).text
    data=data[data.find('----- BEGIN MESSAGE -----<br />')+len('----- BEGIN MESSAGE -----<br />1234'):data.find('----- END MESSAGE -----')-10]
    print('[%s]'%data)
    msg=''
    for i in range(0,len(data),8):
        msg=msg+chr(int(data[i:i+8],2))
    data = msg
    print('[%s]'%data)
    data=hashlib.sha512(data.encode()).hexdigest()
    print('[%s]'%data)
    data=requests.get(url+data,cookies={"PHPSESSID":ssid}).text
    data=data[data.find('<div class="alert alert-info">')+len('<div class="alert alert-info">'):]
    data=data.split('</div>')[0]
    print(print('[%s]'%data))
    
run1('<your cookie id>') #for Hash me if you can 
run2('<your cookie id>') #for Hash me again
