


SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jeru@localhost/pitch'
 UPLOADED_PHOTOS_DEST ='app/static/photos'
 email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")