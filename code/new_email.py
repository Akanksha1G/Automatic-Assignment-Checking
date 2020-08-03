import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)

def email_fun(data):

    for studentdata in data:

        server.starttls()
        server.login("akanksha114jain@gmail.com","password")
        message="Hello"

        server.sendmail(studentdata[0],message)

server.quit()