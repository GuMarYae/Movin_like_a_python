from ch9tv import TV

def main():
    
    tv1 = TV()
    
    #this is not realistic. just chaecking if the cturnOnstructors work
    #in the real world you would use the getters and seters to change it
    #hopefully later, pythturnOn has private etc where turnOne cant just change the cturnOnstructors like this
    tv1.on = True
    tv1.volumeLevel = 70
    tv1.channel = 123
    print("TV status: ",tv1.on,", ","TV volume level is:" ,tv1.volumeLevel,", ", "TV channel is: ",tv1.channel)
    tv1.on = False
    print("TV status: ",tv1.on,", ","TV volume level is:" ,tv1.volumeLevel,", ", "TV channel is: ",tv1.channel)



    
    #this is the normal way, setters and functiturnOns:
    tv1.turnOn()
    tv1.setVolumeLevel(71)
    tv1.setChannel(899)
    print("TV status: ",tv1.on,", ","TV volume level is:" ,tv1.volumeLevel,", ", "TV channel is: ",tv1.channel)
    
    tv1.turnOn()
    tv1.setVolumeLevel(72)
    tv1.setChannel(900)
    print("TV status: ",tv1.on,", ","TV volume level is:" ,tv1.volumeLevel,", ", "TV channel is: ",tv1.channel)
    
    tv1.turnOn()
    tv1.setVolumeLevel(72)
    tv1.setChannel(900)
    print("TV status: ",tv1.on,", ","TV volume level is:" ,tv1.volumeLevel,", ", "TV channel is: ",tv1.channel)

    tv1.volumeUp()
    tv1.volumeUp()
    tv1.volumeUp()
    tv1.volumeUp()
    tv1.volumeUp()
    tv1.channelUp()
    tv1.channelUp()
    tv1.channelUp()
    tv1.channelUp()

    print("TV status: ",tv1.on,", ","TV volume level is:" ,tv1.volumeLevel,", ", "TV channel is: ",tv1.channel)
    tv1.turnOff()
    print("TV status: ",tv1.on,", ","TV volume level is:" ,tv1.volumeLevel,", ", "TV channel is: ",tv1.channel)
    
main()
