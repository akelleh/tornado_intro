from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop


class StartHandler(RequestHandler):
    def get(self):
        customer_id = self.get_argument('customer_id')
        # completed = start_loyalty_account(customer_id)
        self.write('OK')
        self.finish()

if __name__ == "__main__":
    handler_mapping = [
                       (r'/start', StartHandler),
                      ]
    application = Application(handler_mapping)
    application.listen(7779)
    IOLoop.current().start()
