import math, random

class Randomiser:
        
    def __init__(self): 
      
    def mixer(int passLength):
        # this would work but need to give user option of which char types to use, so need to select them individually.
        upperVal = ''
        lowerVal = ''
        symVal = ''
        numVal = '' 
        
            
        if(Interface.upperVal == true):
            upperVal = 'string.ascii_lowercase'
        if(Interface.lowerVal == true):
            lowerVal = 'string.ascii_uppercase'
        if(Interface.symVal == true):
            symVal = 'string.digits'
        if(Interface.numVal == true):
            numVal = 'string.punctuation'
        
        # not sure what this will do if one of these options isn't selected.
        password_characters = upperVal + lowerVal + symVal + numVal
        return ''.join(random.choice(password_characters) for i in  range(passLength))   
      

class Generator:
    
    def __init__(self):

    def getLen():
        return len = Interface.lengthVal.get()
        
    def getUpper():
        upper = Interface.upperVal.get()
        if(upper == true):
            return true
        else return false
        
    
    def getLower():
        lower = Interface.lowerVal.get()
        if(lower == true):
            return true
        else return false

    def getSym():
        sym = Interface.symVal.get()
            if(sym == true):
                return true
            else return false

    def getNum():
        num = Interface.numVal.get()
        if(num == true):
            return true
        else return false
