import json
from app import db, login_manager
from flask_login import UserMixin

from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    emailConfirmed = db.Column(db.Boolean)
    password = db.Column(db.String(80))
    role = db.Column(db.String(80))
    f_name = db.Column(db.String(80))
    l_name = db.Column(db.String(80))
    city = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    country = db.Column(db.String(80))
    zip = db.Column(db.String(8))
    about = db.Column(db.String(255))
    address = db.Column(db.String(80))
    avatar_link = db.Column(db.String(80))


class CommentLikes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    likes = db.Column(db.Integer)
    userid = db.Column(db.Integer)
    commentid = db.Column(db.Integer)


class Jyforum(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acttime = db.Column(db.String(30))
    user = db.Column(db.Integer())
    ticker = db.Column(db.String(50))
    post = db.Column(db.String(1000))
    reply = db.Column(db.Integer())


class Alerts(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    symbols = db.Column(db.String(20))
    analytics = db.Column(db.Boolean(), default=False)
    news = db.Column(db.Boolean(), default=False)
    enabled = db.Column(db.Boolean(), default=False)


class TickersData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(20), unique=True)
    last_price = db.Column(db.Float)
    value_change = db.Column(db.Float)
    percent_change = db.Column(db.Float)
    date_changed = db.Column(db.Integer)
    heat_map = db.relationship('HeatMap', backref='ticker', lazy=True)
    close_price = db.Column(db.Float)
    close_price_updated = db.Column(db.Integer)


class Marketnews(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    source = db.Column(db.String(80))
    published = db.Column(db.String(15))
    title = db.Column(db.String(255))
    link = db.Column(db.String(255))


class Worldnews(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    source = db.Column(db.String(80))
    published = db.Column(db.String(15))
    title = db.Column(db.String(255))
    link = db.Column(db.String(255))


class Company(db.Model):
    symbol = db.Column(db.String(10), primary_key=True)
    company = db.Column(db.String(80))


class HeatMap(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    ticker_id = db.Column(db.Integer, db.ForeignKey('tickers_data.id'), nullable=False, autoincrement=True)
    indice = db.Column(db.String(10))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
