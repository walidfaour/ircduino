#Author: c0mrade
#irc.freenode.net 6667
#main channel ##robot

import socket
import serial
import sys
import datetime

#reload(sys)
#sys.setdefaultencoding('utf8')
com_port = raw_input("Enter COM port number: ")
comport = serial.Serial('COM' + com_port)
comport.baudrate = 9600
comport.bytesize = 8
comport.parity = 'N'
comport.stopbit = 1

LED = 1
LCD1 = 2
LCD2 = 3
LCDCLR = 4

channel = raw_input("Enter channel to join: ")

def ledController(msg):

	nick = msg[1:msg.find('!')]
	msg = msg[msg.find(':',1,len(msg))+1:len(msg)]
	args = len(msg.split(' ', 1))

	if args ==1:
		arg1 = ''
	else:
		arg1 = msg.split(' ',1)[1]

	if msg[:4] == '@LED': # if the string contains '@LED' 
		comport.write(str(LED) + msg[3:])
	if msg[:5] == '@LCD1':  
		comport.write(str(LCD1) + msg[5:])		
	if msg[:5] == '@LCD2': 
		comport.write(str(LCD2) + msg[5:])
	if msg[:7] == '@LCDCLR': 
		comport.write(str(LCDCLR))
	if msg[:5] == '@help':
		help()
	return data

#Control LED/LCD


#Help Menu
def help():
	data = -1
	s.send(str('PRIVMSG ' + channel + ' :IRC Arduino LCD/LED Control System v1.1:\n'))
	s.send(str('PRIVMSG ' + channel + ' :@help - to show this help menu.\n'))
	s.send(str('PRIVMSG ' + channel + ' :@LED<number> - to control LEDs.\n'))
	s.send(str('PRIVMSG ' + channel + ' :@LCD1<text> - Print to LCD, first line.\n'))
	s.send(str('PRIVMSG ' + channel + ' :@LCD2<text> - Print to LCD, second line.\n'))
	s.send(str('PRIVMSG ' + channel + ' :@LCDCLR - Clear the LCD.\n'))
	s.send(str('PRIVMSG ' + channel + ' :Available LEDs:.\n'))
	s.send(str('PRIVMSG ' + channel + ' :Green LED - Command: @LED1.\n'))
	s.send(str('PRIVMSG ' + channel + ' :Red LED - Command @LED2.\n'))
	s.send(str('PRIVMSG ' + channel + ' :Orange LED - Command @LED3.\n'))
	s.send(str('PRIVMSG ' + channel + ' :You can control multiple LEDs for ex: @LED123.\n'))
	return data

s = socket.socket()
s.connect(('irc.freenode.net',6667)) #connection to the irc server
bot_pass = raw_input("Enter bot password: ")
s.send('PASS ' + bot_pass + '\n')
s.send('NICK printbot\n')
s.send('USER printbot printbot printbot : printbot\n')
s.send('JOIN ' + channel + '\n')

while True:
	data = s.recv(1024) # reading from the socket
	if data.find('PRIVMSG ' + channel) > 0:
		ledController(data)
	if data.find('PING') != -1:
		s.send(str('PONG ' + data.split(':')[1] + '\n'))
