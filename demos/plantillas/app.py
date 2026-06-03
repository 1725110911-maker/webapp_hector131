import web

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.Index()

if __name__ == "__main__":
    app.run()