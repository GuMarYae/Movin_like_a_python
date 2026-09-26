class TV:
    # pythons way of a default constructor and constructor in one
    #remember, init is a key word in python and its two __init__ not _init_
    #self is not a keyword but by convintion, use it
    #the values are default, if you make an argment in main.py 
    #python uses the same constructor but overrides with the values entered by the user
    
    def __init__(self): # local instant parameter
        print("Default constructor is called")
        # so here, you can make variable names as youre initializing it
        # theyre instance variables
        # so here, we're declaring variables so the can be used in the class
        self.channel = 1 # default constructor is set to 1
        self.volumeLevel = 1 # default construtor to set volume at 1
        self.on = False
    
    ## BETTER VERSION:
    # This one __init__ works as both a default and parameterized constructor.
    # If no arguments are passed, Python uses the default values: 1, 1, False.
    # If arguments are passed, those values replace the defaults.
    # This means we only need ONE __init__ instead of trying to make two constructors.
    # Python does not overload constructors like Java. If we define __init__ twice,
    # the second definition replaces the first one.
    def __init__(self, channel = 1, volumeLevel = 1, on = False):
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = on
  ####################################################################################      
   # functions   
    def turnOn(self):  # local instant parameter
        self.on = True
        
    def turnOff(self):
        if (self.on == True):
           self.on = False
   #################################################################################### 
    #getters
    def getChannel(self):
         if (self.on == True):
            return self.channel
    def getVolumelevel(self):
        return self.volumeLevel
    ####################################################################################
   #setters 
    def setVolumeLevel(self, volumeLevel):
        if (self.on):
            if isinstance(volumeLevel, int) and volumeLevel < 101 and volumeLevel > 0:
                self.volumeLevel = volumeLevel
            else:
                print("Invalid entry") 
            
    def setChannel(self, channel):
        if self.on:
            #self means if the number entered is of an integer, less than 1000 and bigger than 0
                if isinstance(channel, int) and channel < 1000 and channel > 0:
                    self.channel = channel
                else:
                    print("Invalid entry")
    ####################################################################################        
    #functions
    def channelUp(self):
        if self.on == True:
        #so if we were on 999, channel++ makes it 1000
        #from there it sees if channel >= 1000
        #if so that syt goes back to channel 1
            self.channel = self.channel + 1
            if self.channel >= 1000:
                self.channel = 1
    def channelDown(self):
        if self.on == True:
            self.channel -= 1
            if self.channel == 0:
                self.channel = 999
    def volumeUp(self):
        if self.on == True:
            self.volumeLevel = self.volumeLevel + 1
    def volumeDown(self):
        if self.on == True:
            self.volumeLevel -= 1