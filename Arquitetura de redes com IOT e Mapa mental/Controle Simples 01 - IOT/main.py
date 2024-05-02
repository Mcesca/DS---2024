import machine
import ssd1306
from machine import Pin, I2C

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
botao = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
botao2 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
azul = machine.Pin(25, machine.Pin.OUT)
roxo = machine.Pin(27, machine.Pin.OUT)

largura = 128
altura = 64

tela = ssd1306.SSD1306_I2C(largura, altura, i2c)
while True:
    blue = botao.value()
    red = botao2.value()

    if blue == 0:
        azul.value(0), roxo.value(1)
        tela.fill(0)
        tela.text('A umidade da', 0, 0)
        tela.text('sala e: 20 graus', 0, 10)
        tela.show()

    if red == 0:
        azul.value(1), roxo.value(0)
        tela.fill(0)
        tela.text('A temperatura da', 0, 0)
        tela.text('sala e: 30 graus', 0, 10)
        tela.show()