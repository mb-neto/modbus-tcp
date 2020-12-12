#!/bin/bash/python3

import sys
from pyModbusTCP.client import ModbusClient
from time import sleep
from random import uniform

def start_machines(components, client):
    print('Ligando'+ components[4] + '...')
    client.write_single_coil(components[0],True)
    print(components[4] + 'ligado!')
    while True:
        client.write_single_register(components[1],int(uniform(components[2],components[3])))
        sleep(1)

def stop_machines(components, client):
    client.write_single_register(components[1], components[2])
    client.write_single_coil(components[0],False)
    return

def open_kitchen(host, port):
    client = ModbusClient(host=str(host), port=port)
    client.open()
    forno=(1,40001,0,250, 'Forno'); batedeira=(2,40002,0,10, 'Batedeira'); lavaloucas=(3,40003,0,10, 'Lava-louças')
    try:
        start_machines(forno, client)
    except:
        print('Desligando todos os componentes...')
        stop_machines(forno, client)
        print('Até mais!')
        return

def close_kitchen(host, port):
    client = ModbusClient(host=host, port=port)
    client.close()

def main(state, host, port):
    if state == 'open':
        print('\n\n')
        print('Boulos Chocolateria, Natal/RN \nRua '+ host +', \nNúmero '+ port + ', \n CEP DCA0130, \nComplemento: Turma 01')
        print('\n\n')
        print('Iniciando componentes da cozinha...\n')
        open_kitchen(host, port)
    else:
        close_kitchen(host, port)
        print('Cozinha fechada!')

main(sys.argv[1], sys.argv[2], sys.argv[3])