import pywhatkit

# To individual 
def sendMessage(mobileNo, message, hour, minute):
    pywhatkit.sendwhatmsg(mobileNo, message, hour, minute, tab_close= True, wait_time= 15)

message = input('Enter the message: ').strip()
mobileNo = input('Enter valid Whatsapp No with country code : ').strip()
print('Enter time in 24hours format')
hour = int(input('Hours: ').strip())
minute = int(input('Minutes: ').strip())


sendMessage(mobileNo,message,hour,minute)
