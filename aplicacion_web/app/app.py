import web

urls = (
    '/', 'Index'
)

class Index:
    def GET(self):
        return "¡Hola desde Docker!"

app = web.application(urls, globals())

if _name_ == "_main_":
    web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 8080))