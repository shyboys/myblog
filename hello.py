import web

urls = (
        '/(.*)', 'hello'
    )

render = web.template.render('templates')
db = web.database(dbn='mysql', user='root', pw='', db='myblog')
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        test = db.select('test')
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'
if __name__ == "__main__":
    app.run()
