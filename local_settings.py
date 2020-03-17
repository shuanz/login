class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = "\x1e\x94\xfbe`\\\xee\xb6\x0fwv.\x98o\x99}\xe9V\x86\xcbVG\xc7\xdc"

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'    # File-based SQL database
    CSRF_ENABLED = True

    # Flask-User settings
    USER_APP_NAME = "Indicadores"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False        # Enable email authentication
    USER_ENABLE_USERNAME = True    # Disable username authentication

    #: Corporation name displayed in page template footers.
    USER_CORPORATION_NAME = 'Sisop'

    #: Copyright year displayed in page template footers.
    USER_COPYRIGHT_YEAR = 2020