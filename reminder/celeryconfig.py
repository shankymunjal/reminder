from __future__ import unicode_literals, print_function, division

BROKER_URL = "amqp://guest:guest@localhost:5672//"

BROKER_POOL_LIMIT=10
CELERY_ACKS_LATE = True
CELERY_IGNORE_RESULT = True
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = False

CELERYD_PREFETCH_MULTIPLIER = 1

CELERY_RESULT_BACKEND = 'amqp'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERY_DEFAULT_RATE_LIMIT = 1000
CELERYD_CONCURRENCY = 2
CELERY_IMPORTS = ('reminder.handlers.reminder_handler')

CELERY_DEFAULT_QUEUE = "sms-celery"
CELERY_QUEUES = {
    'email-celery': {
        'binding_key': 'email-celery'
    },
    'sms-celery': {
        'binding_key': 'sms-celery'
    },
}

CELERY_ROUTES = ({
                     'reminder.handlers.reminder_handler.send_email': {
                         'queue':'email-celery',
                         'routing_key': 'email-celery'
                     },
                     'reminder.handlers.reminder_handler.send_sms': {
                         'queue':'sms-celery',
                         'routing_key': 'sms-celery'
                     }},)


CELERYD_LOG_LEVEL = 'INFO'
CELERYD_HIJACK_ROOT_LOGGER= False
