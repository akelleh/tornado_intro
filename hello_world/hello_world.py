from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop


class ChartHandler(RequestHandler):
    def get(self):
        data = {"data": [
                            {"label": "Bakersfield Central",
                             "value": "880000"},
                            {"label": "Garden Grove Harbour",
                             "value": "730000"}
                           ],
                  }
        self.write(data)


if __name__ == "__main__":
    handler_mapping = [
                       (r'/chart$', ChartHandler),
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()
