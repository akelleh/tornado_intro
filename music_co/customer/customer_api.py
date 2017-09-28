from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

from email_client import send_email
from loyal_client import enroll

class CustomerHandler(RequestHandler):
    def get(self):
        create_customer(self)  # create the database entry
        customer_id = self.get_argument('customer_id')
        email_address = self.get_argument('email_address')
        email_sent = send_email(email_address)
        enrolled = enroll(customer_id)
        self.write('OK')
        self.finish()

if __name__ == "__main__":
    handler_mapping = [
                       (r'/enroll', CustomerHandler),
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()
