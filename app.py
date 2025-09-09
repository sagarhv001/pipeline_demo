from flask import Flask
from rt_backend_services.app import backend_bp
from rt_web_services.app import web_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(backend_bp, url_prefix='/backend')
app.register_blueprint(web_bp, url_prefix='/web')


if __name__ == '__main__':
    app.run(debug=True)