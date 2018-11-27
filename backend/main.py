import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define,options
from app.application import Application
from app.urls import urls
from app import config




define("port",type=int,default=8000,help="run server on the given port")


def main():
    # options.logging = "warning"debug message
    # options.log_file_prefix = config.log_path
    tornado.options.parse_command_line()
    app = Application(urls,**config.settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()



if __name__ == '__main__':
    main()
