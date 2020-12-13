#!/bin/bash/python3

import sys
from pyModbusTCP.client import ModbusClient
from time import sleep
from random import uniform

def start_machines(components, client):
    print('Máquinas ligadas!\n')
    while True:
        for machine in components:
            client.write_single_coil(machine[0],True)
            client.write_single_register(machine[1],int(uniform(machine[2],machine[3])))
        sleep(3)

def stop_machines(components, client):
    for machine in components:
        client.write_single_register(machine[1], machine[2])
        client.write_single_coil(machine[0],False)
        print('\n'+ machine[4] + ' desligado(a)!')
    return

def open_kitchen(host, port):
    client = ModbusClient(host=str(host), port=port)
    client.open()
    forno=(1,40001,0,250, 'Forno'); batedeira=(2,40002,0,10, 'Batedeira'); lavaloucas=(3,40003,0,10, 'Lava-louças')
    try:
        print('Ligando as máquinas da cozinha...\n')
        start_machines([forno, batedeira,lavaloucas], client)
    except:
        print('\n\nDesligando todos os componentes...')
        stop_machines([forno, batedeira,lavaloucas], client)
        print('\nAté mais!')
        return

def close_kitchen(host, port):
    client = ModbusClient(host=host, port=port)
    client.close()

def main(state, host, port):
    if state == 'open':
        print('\nSeja bem-vindo a nossa cozinha inteligente!\n')
        print('Boulos Chocolateria, Natal/RN \nRua '+ host +', \nNúmero '+ port + ', \nCEP DCA0130, \nComplemento: Turma 01')
        print('\n')
        print('Iniciando componentes da cozinha...\n')
        open_kitchen(host, port)
    else:
        close_kitchen(host, port)
        print('Cozinha fechada!')

main(sys.argv[1], sys.argv[2], sys.argv[3])