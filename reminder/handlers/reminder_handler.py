import json
from datetime import datetime

from celery.decorators import task
from tornado.web import RequestHandler

from reminder.handlers.message_handler import EmailMessage


class ReminderHandler(RequestHandler):
    def post(self, *args, **kwargs):
        request = json.loads(self.request.body)
        date = request.get('date')
        time = request.get('time')
        message = request.get('message')
        channel = request.get('channel')
        email = request.get('email')
        mobile_phone = request.get('mobile_phone')
        try:
            eta = get_eta_from_datetime(date, time)
        except Exception as e:
            self.set_status(400)
            return self.write(json.dumps({'error': "Date Time format is not correct"}))
        if 'email' in channel:
            if email:
                send_email.apply_async(args=(message, email), queue='email-celery', routing_key='email-celery', eta=eta)
                # send_email(message, email)
            else:
                self.set_status(400)
                return self.write(json.dumps({'error': "Email is missing"}))


        elif 'sms' in channel:
            if mobile_phone:
                send_sms.apply_async(args=(message, mobile_phone), queue='sms-celery', routing_key='sms-celery', eta=eta)
            else:
                self.set_status(400)
                return self.write(json.dumps({'error': "Mobilephone is missing"}))

        else:
            self.set_status(400)
            return self.write(json.dumps({'success': "Only sms and email channel is supported"}))
        self.set_status(200)
        return self.write(json.dumps({'success': "Reminder has been scheduled"}))

@task
def send_email(message, email):
    EmailMessage(message, email).send()

@task
def send_sms(message):
    print("by sms celery")

def get_eta_from_datetime(date, time):
    date_object = datetime.strptime(date + time , '%m/%d/%Y%I:%M %p')
    return date_object