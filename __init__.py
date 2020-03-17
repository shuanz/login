from flask_user.forms import RegisterForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from .local_settings import ConfigClass
from flask_babel import Babel
from flask_user import SQLAlchemyAdapter, UserManager, login_required, roles_required
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

# Initialize ConfigClass
ConfigClass = ConfigClass()

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()


# Extend registration form
class MyRegisterForm(RegisterForm):
    first_name = StringField('First name', validators=[DataRequired('First name is required')])
    last_name = StringField('Last name',  validators=[DataRequired('Last name is required')])
    #roles = SelectField('Role', choices=[(2, 'Viewer'), (1, 'Admin')], validators=[DataRequired('Role is required')])
    roles = SelectField('Role', choices=[('viewer', 'Viewer'), ('admin', 'Admin')], validators=[DataRequired('Role is required')])


def create_app():

    # Create Flask app load app.config
    app = Flask(__name__)
    app.config.from_object(__name__+'.ConfigClass')

    db.init_app(app)

    # Initialize Flask-BabelEx
    babel = Babel(app)

    # Setup Flask-User and specify the User data-model
    from .models.models import User

    # Setup Flask-User
    db_adapter = SQLAlchemyAdapter(db, User)
    user_manager = UserManager(db_adapter, app, register_form=MyRegisterForm)

    # The Home page is accessible to anyone
    @app.route('/')
    def home_page():
        return render_template('index.html')

    # The Members page is only accessible to authenticated users
    @app.route('/members')
    @login_required
    def member_page():
        return render_template('member.html')

    # The Admin page is only accessible to admin users
    # The Members page is only accessible to authenticated users
    @app.route('/admin')
    @roles_required('admin')
    def admin_page():
        return render_template('admin.html')

    return app