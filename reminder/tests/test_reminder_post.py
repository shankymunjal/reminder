import json

from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application

from reminders.reminder import ReminderHandler


class TestHelloApp(AsyncHTTPTestCase):
    def get_app(self):
        return Application(
                [
                    (r"/reminder", ReminderHandler),
                ])

    def test_incorrect_date(self):
        response = self.fetch('/reminder', method="POST", body=json.dumps({
            "date":"14/18/2016",
            "time": "12:34pm",
            "message": "This is shanky",
            "channel": "email",
            "email": "shanky.munjal@quovantis.com"
        }))
        self.assertEqual(response.code, 400)
        self.assertEqual(json.loads(response.body)['error'], 'Date Time format is not correct')

    def test_incorrect_time(self):
        response = self.fetch('/reminder', method="POST", body=json.dumps({
            "date":"11/05/2016",
            "time": "13:34pm",
            "message": "This is shanky",
            "channel": "email",
            "email": "shanky.munjal@quovantis.com"
        }))
        self.assertEqual(response.code, 400)
        self.assertEqual(json.loads(response.body)['error'], 'Date Time format is not correct')

    def test_set_reminder(self):
        response = self.fetch('/reminder', method="POST", body=json.dumps({
            "date":"11/05/2016",
            "time": "11:34pm",
            "message": "This is shanky",
            "channel": "email",
            "email": "shanky.munjal@quovantis.com"
        }))
        self.assertEqual(response.code, 200)
        self.assertEqual(json.loads(response.body)['success'], 'Reminder has been scheduled')

    def test_incorrect_channel(self):
        response = self.fetch('/reminder', method="POST", body=json.dumps({
            "date":"11/05/2016",
            "time": "11:34pm",
            "message": "This is shanky",
            "channel": "appmail",
            "email": "shanky.munjal@quovantis.com"
        }))
        self.assertEqual(response.code, 400)
        self.assertEqual(json.loads(response.body)['error'], 'Only sms and email channel is supported')

    def test_by_not_passing_email(self):
        response = self.fetch('/reminder', method="POST", body=json.dumps({
            "date":"11/05/2016",
            "time": "11:34pm",
            "message": "This is shanky",
            "channel": "email"
        }))
        self.assertEqual(response.code, 400)
        self.assertEqual(json.loads(response.body)['error'], 'Email is missing')