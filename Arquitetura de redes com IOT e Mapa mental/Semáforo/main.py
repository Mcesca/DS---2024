import machine
import time

vermelho = machine.Pin(12, machine.Pin.OUT)
amarelo = machine.Pin(14, machine.Pin.OUT)
verde = machine.Pin(27, machine.Pin.OUT)

while True:
    vermelho.value(1)
    time.sleep(5)
    vermelho.value(0)

    amarelo.value(1)
    time.sleep(1)
    amarelo.value(0)

    verde.value(1)
    time.sleep(3)
    verde.value(0)