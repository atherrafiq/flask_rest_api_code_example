from api import create_app

class PrefixMiddleware(object):

    def __init__(self, app, *prefix):
        self.app = app
        self.prefixes = []

        for i in prefix:
            self.prefixes.append(i)


    def __call__(self, environ, start_response):

        for i in self.prefixes:
            if environ['PATH_INFO'].startswith(i):
                environ['PATH_INFO'] = environ['PATH_INFO'][len(i):]
                environ['SCRIPT_NAME'] = i
                return self.app(environ, start_response)

        start_response('404', [('Content-Type', 'text/plain')])
        return ["This url does not belong to the app.".encode()]

app = create_app()
app.wsgi_app = PrefixMiddleware(app.wsgi_app, '/TendersPythonAPI')

if __name__ == "__main__":
    app.run()