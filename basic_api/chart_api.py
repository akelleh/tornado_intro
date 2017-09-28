from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

from get_data import get_chart


class ChartHandler(RequestHandler):
    def set_default_headers(self):
        super(ChartHandler, self).set_default_headers()
        self.set_header('Access-Control-Allow-Origin', 'http://localhost:3000')
        self.set_header('Access-Control-Allow-Credentials', 'true')

    def get(self, chart_name):
        data = get_chart(chart_name)
        self.write(data)

if __name__ == "__main__":
    handler_mapping = [
                       (r'/chart/([a-zA-Z]+)$', ChartHandler),
                      ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()
