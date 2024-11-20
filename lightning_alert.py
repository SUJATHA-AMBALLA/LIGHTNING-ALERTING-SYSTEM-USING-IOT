from machine import Pin, UART
import utime, time
import math
GSMGPS = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
buff = bytearray(255)
buz=Pin(9,Pin.OUT)

def send_call(number):
    print('Calling...')
    cmd='AT\r\n'
    GSMGPS.write(cmd)
    time.sleep(2)

    cmd='ATD'+ str(number)+';\r\n'
    GSMGPS.write(cmd)
    time.sleep(50)
def send_sms(number):
    print("sending SMS..")
    cmd='AT\r\n'
    GSMGPS.write(cmd)
    time.sleep(2)
    
    cmd='AT+CMGF=1\r\n'
    GSMGPS.write(cmd)
    time.sleep(2)
                                           
    phno=str(number)                          
    cmd='AT+CMGS="'+str(phno)+'"\r\n'
    GSMGPS.write(cmd)
                          
    time.sleep(1)
    cmd="alert"
    GSMGPS.write(cmd)  # Message
   
    #ser.write(msg.encode())  # Message
    time.sleep(1)
    cmd = "\x1A"
    GSMGPS.write(cmd) # Enable to send SMS
    time.sleep(2)
    print('SMS Sent')
    time.sleep(6)



csvdata = []
delim = ','
with open('1.csv','r') as file:
    for line in file:
        csvdata.append(line.rstrip('\n').rstrip('\r').split(delim))
        
tlen=len(csvdata)
print(tlen)
for x in range (tlen):
    #print(csvdata[x][4])
    if(str(csvdata[x][4]) =="1"):
        print(csvdata[x][6])
        buz.value(1)
        time.sleep(1)
        buz.value(0)
        send_call(csvdata[x][6])
