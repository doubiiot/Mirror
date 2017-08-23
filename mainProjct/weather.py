# -*- coding:utf-8 -*-
import urllib, urllib.request, sys
import json

def getWeather():
    host = 'https://free-api.heweather.com/v5/forecast?city=CN101120201&key=4f4aa9f984ad44c2b2fdd78280b31900'
    host_now = 'https://free-api.heweather.com/v5/now?city=CN101120201&key=4f4aa9f984ad44c2b2fdd78280b31900'
    # 下载数据
    content1 = loadData(host)
    content2 = loadData(host_now)
    #print(content_data)
    dic_data = json.loads(content1)['HeWeather5'][0]['daily_forecast']
    realtime_data = json.loads(content2)['HeWeather5'][0]['now']['tmp']
    i = 0
    threeday_data = []
    for key in dic_data:
        #print(key)
        i += 1
        if(i==1):
           today_data = storeData(key)
           threeday_data.append(today_data)
        elif(i==2):
            tmr_data = storeData(key)
            threeday_data.append(tmr_data)
        elif(i==3):
            dat_data = storeData(key)
            threeday_data.append(dat_data)
    threeday_data.append(realtime_data)
    #print(threeday_data)
    return threeday_data
def loadData(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    content_data = response.read().decode('utf-8')
    return content_data
def storeData(key):
    alldata = []
    alldata.append(key['cond']['txt_d'])
    alldata.append(key['date'])
    alldata.append(key['hum'])
    alldata.append(key['tmp']['max'])
    alldata.append(key['tmp']['min'])
    alldata.append(key['wind']['dir'])
    alldata.append(key['wind']['sc'])
    return alldata

getWeather()

'''
    # 解析JSON
    
    需要的数据：
    city\date\week\weather\temp\temphigh\templow\humidity\winddirect\windpower
    
    weather_data = {}
    dic_data = json.loads(content_data)['result']
    for key in dic_data:
        if (key == "city"):
            weather_data['city'] = dic_data['city']
        elif(key == "date"):
            weather_data['date'] = dic_data['date']
        elif (key == "week"):
            weather_data['week'] = dic_data['week']
        elif (key == "weather"):
            weather_data['weather'] = dic_data['weather']
        elif (key == "temp"):
            weather_data['temp'] = dic_data['temp']
        elif (key == "humidity"):
            weather_data['humidity'] = dic_data['humidity']
        elif (key == "winddirect"):
            weather_data['winddirect'] = dic_data['winddirect']
        elif (key == "windpower"):
            weather_data['windpower'] = dic_data['windpower']

    return weather_data
    '''
