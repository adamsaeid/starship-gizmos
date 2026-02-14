from machine import Pin
from picozero import LED, Button

dataPIN = 13
latchPIN = 15
clockPIN = 14

up_button = Button(16)
down_button = Button(17)

dataPIN=Pin(dataPIN, Pin.OUT)
latchPIN=Pin(latchPIN, Pin.OUT)
clockPIN=Pin(clockPIN, Pin.OUT)


def shift_update(input,data,clock,latch):
  #put latch down to start data sending
  latch.value(0)
  
  #load data
  for i in range(8):
    clock.value(0)
    data.value(int(input[i]))
    clock.value(1)

  #put latch up to store data on register
  latch.value(1)
  latch.value(0)

def handle_up_press():
    global bit_string
    bit_string = bit_string[1:] + str(1)
    shift_update(bit_string,dataPIN,clockPIN,latchPIN)
    
def handle_down_press():
    global bit_string
    bit_string = str(0) + bit_string[:-1]
    shift_update(bit_string,dataPIN,clockPIN,latchPIN)

up_button.when_pressed = handle_up_press
down_button.when_pressed = handle_down_press

bit_string="00000011"
shift_update(bit_string,dataPIN,clockPIN,latchPIN)
