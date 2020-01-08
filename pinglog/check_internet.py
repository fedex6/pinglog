# -*- coding: utf-8 -*-
#        _             _                 
#       (_)           | |                
#  _ __  _ _ __   __ _| |     ___   __ _ 
# | '_ \| | '_ \ / _` | |    / _ \ / _` |
# | |_) | | | | | (_| | |___| (_) | (_| |
# | .__/|_|_| |_|\__, \_____/\___/ \__, |
# | |             __/ |             __/ |
# |_|            |___/             |___/ 
#                                       v0.5
#                                       
#   Telegram: @fedex6
#   
#   Importante: Hay que isntalar pingparsing
#   ~/: pip install pingparsing
#
#-------------------------------------------------------#

## Basic imports & configuration
import os
import sys
import time
import json
import pingparsing

## LOG
log = open("ping_log.txt", "a") ## Abrir el log al principio

## Variables
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%d/%m/%Y %H:%M", named_tuple)
ping_parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()
transmitter.destination = "1.1.1.1"
transmitter.count = 1
result = transmitter.ping()
pingueo =  str(result).split("data.")[1].split("---")[0].replace("\\n","") ## Ejemplo 64 bytes from 1.1.1.1: icmp_seq=1 ttl=57 time=1.90 ms
r_pingueo = str(result).split("data.")[1].split("---")[2].replace("\\n","").split("rtt")[0] ## Ejemplo: 1 packets transmitted, 1 received, 0% packet loss, time 0ms

## Hacer Ping y guardar los resultados en el log
log.write( time_string + ' >>> ' + pingueo + ' // ' + r_pingueo + '\n')

## End
log.close() ## Cerrar el LOG
exit()