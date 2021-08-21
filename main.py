import pywhatkit

# To individual 
def sendMessage(mobileNo, message, hour, minute):
    pywhatkit.sendwhatmsg(mobileNo, message, hour, minute, tab_close= True, wait_time= 15)


# Getting Input from User
# Message You Wanna Send
message = input('Enter the message: ').strip()
# Whatsapp Number
mobileNo = input("Enter valid receiver's Whatsapp Number with country code : ").strip()
print('Enter time in 24hours format')
# Time : Hour
hour = int(input('Hours: ').strip())
# Time : Minute
minute = int(input('Minutes: ').strip())


# Function Call
sendMessage(mobileNo,message,hour,minute)