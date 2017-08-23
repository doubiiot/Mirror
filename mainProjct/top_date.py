import urllib, urllib.request, sys
import json
def getDate():
    '''
    host_city = 'http://jisutqybmf.market.alicloudapi.com'
    path_city = '/weather/city'
    method = 'GET'
    appcode = '7355c8fabd674079adf1afaadb2012f6'
    querys = ''
    bodys = {}
    url = host_city + path_city

    request_city = urllib.request.Request(url)
    request_city.add_header('Authorization', 'APPCODE ' + appcode)
    response_city = urllib.request.urlopen(request_city)
    content_city = response_city.read().decode('utf-8')
    cityinfo = json.loads(content_city)
    for x in cityinfo['result']:
        if(x['city'] == "青岛"):
            print(x)
    '''
    host = 'http://jisutqybmf.market.alicloudapi.com'
    path = '/weather/query'
    method = 'GET'
    appcode = '7355c8fabd674079adf1afaadb2012f6'
    querys = 'citycode=101120201&cityid=283&ip=ip&location=location'
    bodys = {}
    url = host + path + '?' + querys

    request = urllib.request.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urllib.request.urlopen(request)
    content_date = response.read().decode('utf-8')
    mydate = json.loads(content_date)['result']
    week = mydate['week'][2]
    if week == "一":
        week = "Monday"
    elif week == "二":
        week = "Tuesday"
    elif week == "三":
        week = "Wednesday"
    elif week == "四":
        week = "Thursday"
    elif week == "五":
        week = "Friday"
    elif week == "六":
        week = "Saturday"
    else :
        week = "Sunday"
    month = mydate['date'][5:7]
    if month == "01":
        month = "January"
    elif month == "02":
        month = "February"
    elif month == "03":
        month = "March"
    elif month == "04":
        month = "April"
    elif month == "05":
        month = "May"
    elif month == "06":
        month = "June"
    elif month == "07":
        month = "July"
    elif month == "08":
        month = "August"
    elif month == "09":
        month = "September"
    elif month == "10":
        month = "October"
    elif month == "11":
        month = "November"
    elif month == "12":
        month = "December"
    spell = week + ',' + month + ' ' + mydate['date'][8:10] + ',' + mydate['date'][0:4]
    return spell
