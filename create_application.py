from flask import Flask
from flask_assets import Environment
from backend_modules.routing.configure_test import application_routing


class CreatorApplication(object):

    def __init__(self):
        self.application = Flask(__name__, template_folder='templates', static_folder='static')
        self.debug = None
        self.reloader = None
        self.host = None
        self.port = None

    def _create_app(self):
        self.application.config["SECRET_KEY"] = 'secret!'
        assets = Environment(self.application)
        assets.url = self.application.static_url_path

        self.application.config.from_object('settings')
        self.application.register_blueprint(application_routing)
        self.debug = self.application.config.get('DEBUG', True)
        self.reloader = self.application.config.get('RELOADER', True)
        self.host = self.application.config.get('HOST')
        self.port = self.application.config.get('PORT')
        with open("routing.dat", "w") as file:
            for i in self.application.url_map.iter_rules():
                file.writelines(str(i) + "\n")
        with open("methods_routing.dat", "w") as file:
            for i in self.application.url_map.iter_rules():
                file.writelines(str(i.endpoint) + "\n")

    def start_app(self):
        self._create_app()
        self.application.run(
            use_reloader=self.reloader,
            debug=self.debug,
            threaded=True,
            host=self.host,
            port=self.port
        )

        # server = WSGIServer(bind_addr=("0.0.0.0", 2001), wsgi_app=self.application, numthreads=100)
        # try:
        #     server.start()
        # except KeyboardInterrupt:
        #     server.stop()
