import time
# This will store current time in timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

if( hour>=0 and hour<12):
    print('Good Morning Sir!')
elif(hour>=12 and hour<=18):
    print('Good AfterNoon SIr!')
elif(hour>18 and hour<24):
    print('Good Night Sir!')
