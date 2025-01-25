from MicroPie import Server


class MyApp(Server):
    def index(self):
        # Pass data to the template for rendering
        return self.render_template(
            "index.html", title="Welcome", message="Hello from MicroPie!"
        )


app = MyApp()
wsgi_application = app.wsgi_app