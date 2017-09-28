from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

from customer import create_customer

class CustomerHandler(RequestHandler):
    def get(self):
        message = create_customer(self)
        pub(message)  # send the message out!
        self.write('OK')
        self.finish()

if __name__ == "__main__":
    handler_mapping = [
                       (r'/enroll', CustomerHandler),
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()
