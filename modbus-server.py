#!/bin/bash/python3

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

server = ModbusServer(host="192.168.1.2", port=8000, no_block=True)

try:
	print("Iniciando servidor...")
	server.start()
	print("Servidor ligado!")
	state = [0]
	while True:
		DataBank.set_words(0, [int(uniform(0, 100))])
		if state != DataBank.get_words(1):
			state = DataBank.get_words(1)
			print("Valor do Registrador 1 mudou para " + str(state))
			sleep(0.5)
except:
	print("Desligando servidor...")
	server.stop()
	print("Servidor desligado!")
