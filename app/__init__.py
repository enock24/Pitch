from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

mail = Mail()

photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)
    configure_uploads(app,photos)
    mail.init_app(app)
    #...
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
