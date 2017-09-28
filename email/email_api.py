from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop


class WelcomeHandler(RequestHandler):
    def get(self):
        email_address = self.get_argument('email_address')
        completed = send_email(email_address)
        if completed:
            self.write('OK')
        else:
            self.write('Failed.')
        self.finish()

if __name__ == "__main__":
    handler_mapping = [
                       (r'/welcome', WelcomeHandler),
                      ]
    application = Application(handler_mapping)
    application.listen(7778)
    IOLoop.current().start()
