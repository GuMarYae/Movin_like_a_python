class Switcher:
    def __init__(self, on = True, off = False):
        self.__on = on
        self.__off = off
        
# getters
#this is how you use something that you want as a boolen
#by convention, you dont use the word get, like getOn or getIsOn
#then tou turn int into a boolean by returning a true or false value
    def isOn(self):
        if self.__on == True:
            self.__off = False
            return True
        
        elif self.__off == True:
            self.__on = False
            return False
        
