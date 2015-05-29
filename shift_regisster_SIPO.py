#    This program control a SIPO Shift Register
#--------------------------------------------------
#    For this example I used a DM74164 CI which is a 8-bits SIPO Shift Register
#    Because he use two data inputs with a AND gate I put one of then in HIGH

import pingo

board = pingo.detect.MyBoard()

data = board.pins[40] #define data pin
clk = board.pins[38] #define clock pin
clr = board.pins[37] #define clear pin
  
#sets pins as outputs
data.mode = pingo.OUT
clk.mode = pingo.OUT
clr.mode = pingo.OUT

#sets all pin low
data.lo()
clk.lo()
clr.hi() #HIGH becouse in 74164 if clear pin is LOW all outputs is LOW

def pulse(a):    #This function pulse a pin
    a.toggle()
    a.toggle()

def write(a):    #receives a string and sets the pins
    for i in a:
        data.lo() if i == '0' else data.hi()
        pulse(clk)

def clear(): #sets all outputs LOW
    pulse(clr)
