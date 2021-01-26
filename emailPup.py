import smtplib

server = smtplib.SMTP("smtp.mail.yahoo.com",587)
server.ehlo()
server.starttls()
server.login('fallingspam@yahoo.com', 'jlpctajrjsskpvlw')
server.sendmail('fallingspam@yahoo.com', '4thefalling@gmail.com', 'Subject: So long. \n\n Dear Alice, so long and thanks for all the fish. Sincerely, Bob')
server.quit()