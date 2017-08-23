import time
def getTime():
    my_time = time.localtime(time.time())

    if my_time[3] < 10:
        hour = '0' + str(my_time[3])
    else:
        hour = str(my_time[3])
    if my_time[4] < 10:
        min = '0' + str(my_time[4])
    else:
        min = str(my_time[4])
    if my_time[5] < 10:
        second = '0' + str(my_time[5])
    else:
        second = str(my_time[5])

    return hour,min,second
