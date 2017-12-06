import time
import serial
import smtplib
     
#TO = 'mark.wogahn@gmail.com'
TO = '2035076514@txt.att.net'
GMAIL_USER = 'mark.wogahn@yale.edu'
GMAIL_PASS = 'freakJoB2011'
     
SUBJECT = 'Intrusion!!'
TEXT = 'Your PIR sensor detected movement'
      
ser = serial.Serial('/dev/ttyACM0', 9600)
  
def send_email():
	print("Sending Email")
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(GMAIL_USER, GMAIL_PASS)
	header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
	header = header + '\n' + 'Subject:' + SUBJECT + '\n'
	print header
	msg = header + '\n' + TEXT + ' \n\n'
	smtpserver.sendmail(GMAIL_USER, TO, msg)
	smtpserver.close()
        
while True:
	message = ser.readline()
	print(message)
	if message[0] == 'M' :
		send_email()
		time.sleep(0.5)
