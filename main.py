import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("web\calc.html")
    
    def post(self):
        one = self.get_argument("one")
        two = self.get_argument("two") 
        three = self.get_argument("three")
        four = self.get_argument("four")
        five = self.get_argument("five")
        six = self.get_argument("six")
        seven = self.get_argument("seven")
        eight = self.get_argument("eight")
        nine = self.get_argument("nine")
        zero = self.get_argument("zero")
        add = self.get_argument("add")
        minus = self.get_argument("minus")
        multiply = self.get_argument("multiply")
        divide = self.get_argument("divide")
        clear = self.get_argument("clear")
        erase = self.get_argument("erase")

        result = str(int(one) + int(two))

        # Write the result as plain text
        self.write(textarea%stextarea % result)

        # HTML content to be written to the pp element
        # content = "This is some content for the textarea element textarea."

        # Write the content to the response
        # self.write(textarea%stextarea % content)

def make_app():
    return tornado.web.Application([ 
        (r"/",MainHandler),
        (r"/web/static/(.*)", tornado.web.StaticFileHandler, {"path": "web\static"})
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(7894)
    print("somethin on port 7894")
    tornado.ioloop.IOLoop.current().start()
