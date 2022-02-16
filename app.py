import os
from flask import Flask

import config
from api.models import db
from api.routes.mutant import mutant_api
from api.routes.welcome import welcome


def create_app(testing_mode=False):
    app = Flask(__name__)

    # Se inicializa config a partir de fichero config y este a su vez de .env
    if testing_mode is True:
        app.config.from_object(config.ConfigTest)
    else:
        app.config.from_object(config.Config)

    app.register_blueprint(welcome, url_prefix='/')
    app.register_blueprint(mutant_api, url_prefix='/api')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=os.getenv('APP_HOST'), type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host=os.getenv('APP_HOST'), port=port)
