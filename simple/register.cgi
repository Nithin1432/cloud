#!/usr/bin/python
import cgi, cgitb
import MySQLdb

webForm = cgi.FieldStorage()

firstname = webForm.getvalue('fname')
lastname = webForm.getvalue('lname')
email = webForm.getvalue('email')
username = webForm.getvalue('Username')
mypass = webForm.getvalue('psw')


db= MySQLdb.connect("localhost","julakann1","38sfi7","julakann1_db") 

myCursor = db.cursor()

sql = "INSERT INTO Userpass2 VALUES ('%s','%s','%s','%s','%s');" %(firstname,lastname,email,username,mypass)

try:
        myCursor.execute(sql)
        db.commit()
except:
        db.rollback()
db.close()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title> REGISTRATION FORM</title>"
print "</head>"
print "<body>"
print "<h2> Congratulations! You Have Successfully Register With UserName = %s </h2>" %(username)
print "</body>"
print "</html>"
