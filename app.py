import sentry_sdk

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from itsdangerous import URLSafeTimedSerializer
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_socketio import SocketIO
from sentry_sdk.integrations.flask import FlaskIntegration
from config import Config

sentry_sdk.init(
    dsn="https://4963b311c67b4e84812569fcc9224980@o518216.ingest.sentry.io/5627744",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)


app = Flask(__name__)
app.config.from_object(Config)
app.debug = True
Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)

mail = Mail(app)

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

from controllers import main

app.register_blueprint(main)


@app.errorhandler(404)
def pageNotFound(error):
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    return render_template('page404.html', username=username), 404
