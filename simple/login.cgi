#!/usr/bin/python

import cgi, cgitb
import MySQLdb

myForm = cgi.FieldStorage()

nick = myForm.getvalue('email')
secret = myForm.getvalue('psw')

db= MySQLdb.connect("localhost","julakann1","38sfi7","julakann1_db") 

myCursor = db.cursor()

sql="SELECT email from Userpass2 WHERE email = '%s' "(nick)

sql = "SELECT passcode from Userpass2 WHERE email = '%s' "%(nick)

try:
  myCursor.execute(sql)
  output = myCursor.fetchone()

  for row in output:
     sWord  = row
except:
  print "Error: unable to fetch data"
db.close()

if secret == sWord:
  print "Content-type:text/html\r\n\r\n"
  print "<html>"
  print "<head>"
  print "<title>Confirm</title>"
  print "</head>"
  print "<body>"
  print "<h2> WELCOME Back %s !</h2>" %(nick)
  print "</body>"
  print "</html>"
else:
  print "Content-type:text/html\r\n\r\n"
  print "Wrong Password or Username !"
  print "</html>"
