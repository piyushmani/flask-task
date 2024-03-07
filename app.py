from flask import Flask
from database.db import initialize_db
from app.api_routes import api_bp

def create_app():
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://db:27017/mydatabase'}
    initialize_db(app)

    app.register_blueprint(api_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', debug=True)
