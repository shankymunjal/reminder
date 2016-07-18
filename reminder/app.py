from __future__ import unicode_literals, print_function, division

import logging

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from reminder.handlers.reminder_handler import ReminderHandler

define("port", default=8889, help="run on the given port", type=int)
define("loglevel", default=None, help="provide your logging level", type=str)

logger = logging.getLogger(__name__)

sms_handlers = [
    (r"/reminder", ReminderHandler),
]

application = tornado.web.Application(sms_handlers, debug=True)

def main():
    tornado.options.parse_command_line()
    server = tornado.httpserver.HTTPServer(application)

    logger.info("Starting reminder app on port:{0}".format(options.port))
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()