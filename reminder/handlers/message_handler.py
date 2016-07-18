#!/usr/bin/python

import smtplib
sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

class Message():
    def __init__(self, message, to):
        self.message = message
        self.to = to


class EmailMessage(Message):

    def send(self):
        SUBJECT = "Reminder Message"
        TEXT = self.message
        FROM = 'remindermessage10@gmail.com'
        PASSWORD = "!QAZxsw2"
        self.message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(self.to), SUBJECT, TEXT)
        smtpObj = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
        smtpObj.login(FROM, PASSWORD)
        smtpObj.sendmail(FROM, self.to, self.message)
        smtpObj.quit()


class SMSMessage(Message):

    def send(self):
        return