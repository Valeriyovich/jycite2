import sqlite3
import json
import time
import socketio
import os

from app import db, ts, mail, socketio
from datetime import datetime
from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, url_for, redirect, request, Response, abort, jsonify, render_template, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from config import Config
from forms import RegisterForm, LoginForm, ContactForm, EmailForm, PasswordForm, JyforumForm
from models import User, CommentLikes, Jyforum, Alerts, TickersData, Worldnews, AlchemyEncoder, HeatMap
from portfolio.utils import get_quotes
from utils.sendEmail import sendEmail
from utils.fundamentals import companyDividends, majorHolders, companyRevenues
from utils.rssDownload import stockNews
from flask_socketio import send, emit

main = Blueprint('main', __name__)

with open("%s/files/tickers_nasdaq.json" % Config.BASE_DIR, "r") as read_file:
    data1 = json.load(read_file)

with open("%s/files/tickers_nyse.json" % Config.BASE_DIR, "r") as read_file:
    data2 = json.load(read_file)

with open("%s/files/tickers_otc.json" % Config.BASE_DIR, "r") as read_file:
    data3 = json.load(read_file)


@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    form = ContactForm()
    if form.validate_on_submit():
        subject = 'Contact from main page'
        html = str(form.name.data) + str('   ') + str(form.email.data) + str('   ') + str(form.text.data)
        email = 'jy.services601@gmail.com'
        sendEmail(email, subject, html, mail)
        return 'Sent contact'
    news = Worldnews.query.all()


    return render_template('index.html', username=username, authenticated=authenticated, form=form, message='',
                           news=news, companyTicker='AAPL | Apple Inc.')


@main.route('/about')
def about():
    return "about us"


@main.route("/logout")
@login_required
def logout():
    authenticated = current_user.is_authenticated
    if authenticated:
        logout_user()
    return redirect('/')


@main.route('/login', methods=['GET', 'POST'])
@main.route('/clientportal', methods=['GET', 'POST'])
def login():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.emailConfirmed:
            if check_password_hash(user.password, form.password.data) and user.emailConfirmed:
                login_user(user, remember=True)
                return redirect(url_for('main.pricechart') + '?stock=AAPL%20|%20Apple')
            else:
                return render_template('client_portal.html', username=username, authenticated=authenticated,
                                       companyTicker='AAPL | Apple Inc.', form=form,
                                       message='Invalid username or password')
        else:
            return render_template('client_portal.html', username=username, authenticated=authenticated,
                                   companyTicker='AAPL | Apple Inc.', form=form, message='Invalid username or password')

    return render_template('client_portal.html', username=username, authenticated=authenticated,
                           companyTicker='AAPL | Apple Inc.', form=form, message='')


# drop-link

@main.route('/marketnews')
def market_news():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'

    try:
        conn = sqlite3.connect('database.db')
        mycursor = conn.cursor()
        mycursor.execute("select * from marketnews")
        marketNews = mycursor.fetchall()

        def wsj(string):
            return 'wallstreetjournal' in string

        def bbc(string):
            return 'bbc' in string

        def nytimes(string):
            return 'nytimes' in string

        def nasdaq(string):
            return 'nasdaq' in string

        def marketwatch(string):
            return 'marketwatch' in string

        def investing(string):
            return 'investing' in string

        wsj = [string for string in marketNews if wsj(string)][0:3]
        nytimes = [string for string in marketNews if nytimes(string)][0:3]
        bbc = [string for string in marketNews if bbc(string)][0:3]
        nasdaq = [string for string in marketNews if nasdaq(string)][0:3]
        marketwatch = [string for string in marketNews if marketwatch(string)][0:3]
        investing = [string for string in marketNews if investing(string)][0:3]
        return render_template('market_news.html', username=username, authenticated=authenticated, wsj=wsj,
                               bbc=bbc, nytimes=nytimes, nasdaq=nasdaq, marketwatch=marketwatch, investing=investing,
                               published=marketNews[0:3], companyTicker='AAPL | Apple Inc.')
    except:
        return render_template('market_news.html', username=username, authenticated=authenticated,
                               companyTicker='AAPL | Apple Inc.')


def compTick(reqargs):
    if len(reqargs) == 0:
        ticker = 'aapl'
        companyTicker = 'AAPL | Apple Inc.'

    if len(reqargs) == 1:
        ticker = ''
        id = request.args.get('stock')
        if str(id) != 'None':
            ticker = str(id).split(' | ')[0]
            companyTicker = str(id)

    if len(reqargs) > 1:
        id = request.args.get('stock')
        ticker = ''
        company = ''
        for arg in request.args:
            if arg != 'stock':
                company = company + arg
        ticker = id.split(' | ')[0]

        companyTicker = id.split(' | ')[0] + str(' | ') + id.split(' | ')[1] + str('&') + company

    return (ticker, companyTicker)


@main.route('/marketnews/<namecompany>', methods=['GET', 'POST'])
def market_news_page(namecompany):
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'

    try:
        conn = sqlite3.connect('database.db')
        mycursor = conn.cursor()
        mycursor.execute("select * from marketnews")
        marketNews = mycursor.fetchall()
        x = f'{namecompany}'

        def searchNews(string):
            return x in string

        news = [string for string in marketNews if searchNews(string)]
        return render_template('market_news_page.html', username=username, authenticated=authenticated,
                               string=news, companyTicker='AAPL | Apple Inc.')
    except:
        return render_template('market_news_page.html', username=username, authenticated=authenticated,
                               companyTicker='AAPL | Apple Inc.')


@main.route('/tradingcalendar')
def trading_calendar():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    conn = sqlite3.connect('database.db')
    mycursor = conn.cursor()
    mycursor.execute("select * from marketnews")
    marketNews = mycursor.fetchall()
    return render_template('trading_calendar.html', username=username, authenticated=authenticated,marketnews=marketNews,
                           companyTicker='AAPL | Apple Inc.')


def getTickerComments(ticker, cur_user):

    messages = Jyforum.query.filter_by(reply=0, ticker=ticker)

    comments = []

    for message in messages:
        message_dict = message.__dict__
        message_dict['username'] = User.query.filter_by(id=message_dict['user']).first().username
        message_dict['replies'] = []
        message_dict['likes'] = CommentLikes.query.filter_by(likes=1, commentid=message_dict['id']).count()
        if cur_user.is_authenticated:
            message_dict['liked'] = CommentLikes.query.filter_by(likes=1, commentid=message_dict['id'],
                                                                 userid=cur_user.get_id()).first()
        replies = Jyforum.query.filter_by(reply=message_dict['id'], ticker=ticker)
        for r in replies:
            r_dict = r.__dict__
            r_dict['username'] = User.query.filter_by(id=message_dict['user']).first().username
            r_dict['likes'] = CommentLikes.query.filter_by(likes=1, commentid=r_dict['id']).count()
            if cur_user.is_authenticated:
                r_dict['liked'] = CommentLikes.query.filter_by(likes=1, commentid=r_dict['id'],
                                                               userid=cur_user.get_id()).first()
            message_dict['replies'].append(r.__dict__)
        comments.append(message_dict)
    return comments


@main.route('/stocks', methods=["GET", "POST"])
@main.route('/stocks/', methods=["GET", "POST"])
def stocks():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'

    tickers_nsdq = HeatMap.query.filter_by(indice="NSDQ").all()
    tickers_sp = HeatMap.query.filter_by(indice="SP").all()
    tickers_dj = HeatMap.query.filter_by(indice="DJ").all()

    return render_template('stocks/stocks.html', companyTicker='AAPL | Apple Inc.', username=username,
                           authenticated=authenticated, tickers_nsdq=tickers_nsdq, tickers_sp=tickers_sp,
                           tickers_dj=tickers_dj)


@main.route('/stocks/pricechart', methods=["GET", "POST"])
def pricechart():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    ct = compTick(request.args)
    ticker = ct[0]
    companyTicker = ct[1]
    return render_template('/stocks/stocksPricechart.html', username=username, ticker=ticker,
                           companyTicker=companyTicker, authenticated=authenticated,
                           tickerPosts=getTickerComments(ticker, current_user))


@main.route('/stocks/pricechart/large', methods=["GET"])
def pricechart_large():
    authenticated = current_user.is_authenticated
    ct = compTick(request.args)
    ticker = ct[0]
    companyTicker = ct[1]
    return render_template('/stocks/stocksPricechart_large.html', authenticated=authenticated, ticker=ticker,
                           companyTicker=companyTicker)


@main.route('/stocks/tradingideas', methods=["GET", "POST"])
def tradingideas():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    ct = compTick(request.args)
    ticker = ct[0]
    companyTicker = ct[1]

    return render_template('/stocks/stocksTradingideas.html', username=username, authenticated=authenticated,
                           ticker=ticker, companyTicker=companyTicker,
                           tickerPosts=getTickerComments(ticker, current_user))


@main.route('/stocks/news', methods=["GET", "POST"])
def stocksNews():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    ct = compTick(request.args)
    ticker = ct[0]
    companyTicker = ct[1]
    news = stockNews(ticker)

    return render_template('/stocks/stocksNews.html', username=username, authenticated=authenticated,
                           ticker=ticker, companyTicker=companyTicker, news=news,
                           tickerPosts=getTickerComments(ticker, current_user))


@main.route('/stocks/dividends', methods=["GET", "POST"])
def dividends():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    ct = compTick(request.args)
    ticker = ct[0]
    companyTicker = ct[1]

    div = companyDividends(ticker)

    return render_template('/stocks/stocksDividends.html', username=username, authenticated=authenticated,
                           ticker=ticker, companyTicker=companyTicker, dividend=div,
                           tickerPosts=getTickerComments(ticker, current_user))


@main.route('/stocks/majorholders', methods=["GET", "POST"])
def majorholders():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    ct = compTick(request.args)
    ticker = ct[0]
    companyTicker = ct[1]
    holders = majorHolders(ticker)

    return render_template('/stocks/stocksMajorholders.html', username=username, authenticated=authenticated,
                           ticker=ticker, holders=holders, companyTicker=companyTicker,
                           tickerPosts=getTickerComments(ticker, current_user))


@main.route('/stocks/financials', methods=["GET", "POST"])
def financials():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    ct = compTick(request.args)
    ticker = ct[0]
    companyTicker = ct[1]
    revenues = companyRevenues(ticker)
    return render_template('/stocks/stocksFinancials.html', username=username, authenticated=authenticated,
                           ticker=ticker, companyTicker=companyTicker, revenues=revenues,
                           tickerPosts=getTickerComments(ticker, current_user))


@main.route('/stocks/jyforum', methods=["POST"])
def jyforum():
    form = JyforumForm()
    if current_user.is_authenticated:
        username = current_user.username

        if form.validate_on_submit():
            ct = compTick(request.args)
            ticker = request.form['ticker']
            companyTicker = ct[1]
            current_time = time.strftime("%H:%M:%S", time.localtime(time.time()))
            actTime = str(datetime.utcnow().date()) + ' ' + str(current_time)
            text = request.form['message_forum']
            jyforum = Jyforum(acttime=actTime, user=current_user.get_id(), ticker=ticker.upper(), post=text,
                              reply=request.form['reply'])
            db.session.add(jyforum)
            db.session.commit()
            return jsonify(status='ok'), 200
        else:
            return jsonify(status='fail'), 400


@main.route('/allcompany', methods=['GET'])
def allcompany():
    # csv_data = csv.reader(open('files/generic.csv'))

    # list_company = data
    # for element in list_company:
    #     data_ticker = data[element]

    data_1 = []
    data_2 = []

    for i in data1:
        sorted(i)
        for key, value in i.items():
            if key == 'ticker':
                data_1.append(value)
            if key == 'company':
                data_2.append(value)
            else:
                continue

    for i in data2:
        sorted(i)
        for key, value in i.items():
            if key == 'ticker':
                data_1.append(value)
            if key == 'company':
                data_2.append(value)
            else:
                continue

    for i in data3:
        sorted(i)
        for key, value in i.items():
            if key == 'ticker':
                data_1.append(value)
            if key == 'company':
                data_2.append(value)
            else:
                continue

    # conn = sqlite3.connect('database.db')
    # mycursor = conn.cursor()
    # mycursor1 = conn.cursor()
    # mycursor.execute("SELECT symbol FROM company")
    # mycursor1.execute("SELECT company FROM company")
    # my1 = mycursor.fetchall()
    # my2 = mycursor1.fetchall()
    resultsCompany = []
    resultsCompany2 = []
    resultsCompany3 = []
    # for information in my1:
    #     resultsCompany += information
    # for information2 in my2:
    #     resultsCompany2 += information2
    resultsCompany3.append(data_1)
    resultsCompany3.append(data_2)
    return Response(json.dumps(resultsCompany3), mimetype='application/json')


@main.route('/likee', methods=['POST'])
def likee():
    if current_user.is_authenticated:
        user_id = current_user.get_id()
        comment_id = request.form['comment_id']
        likes = CommentLikes.query.filter_by(userid=user_id, commentid=comment_id).first()
        if likes:
            if likes.likes:
                likes.likes = 0
            else:
                likes.likes = 1
        else:
            likes = CommentLikes(userid=user_id, likes=1, commentid=comment_id)
        db.session.add(likes)
        db.session.commit()

        like_count = CommentLikes.query.filter_by(likes=1, commentid=comment_id).count()
        return jsonify(like_count=like_count, liked=likes.likes)
    else:
        return 'Sign in please'


@main.route('/commodities')
def commodities():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    return render_template('commodities.html', username=username, authenticated=authenticated,
                           companyTicker='AAPL | Apple Inc.')


@main.route('/currencies')
def currencies():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    return render_template('currencies.html', username=username, authenticated=authenticated, message='',
                           companyTicker='AAPL | Apple Inc.')


@main.route('/test_ws', methods=['POST', 'GET'])
def test_ws():
    return render_template('ws_test.html')


@main.route('/test_2/<symbol>', methods=['POST', 'GET'])
def test_ws2(symbol):
    symbol = symbol.replace('_', '/')
    tickers = json.dumps(TickersData.query.filter_by(symbol=symbol).first(), cls=AlchemyEncoder)
    socketio.emit('message', tickers, broadcast=True)

    return 'Ok'


@socketio.on('message')
def handle_message(data):
    send('received message: ' + data)



@main.route('/portfolio', methods=['POST', 'GET'])
def portfolio():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
        u_id = current_user.get_id()
        ct = compTick(request.args)
        ticker = ct[0]

        tickers = db.session.query(Alerts, TickersData).filter(Alerts.symbols==TickersData.symbol, Alerts.user==u_id)

        form = request.form

        if request.method == 'POST':

            rid = form.get('id')
            if rid:
                row = Alerts.query.get(rid)
                if form.get('enabled'):
                    row.enabled = int(form.get('enabled'))
                if form.get('analytics'):
                    row.enabled = int(form.get('analytics'))
                if form.get('news'):
                    row.enabled = int(form.get('news'))
            else:
                m = Alerts()

                symbols = form.get('symbols')
                alerts = Alerts.query.filter_by(user=u_id, symbols=symbols)
                t_model = TickersData.query.filter_by(symbol=symbols).first()
                now_ts = int(datetime.now().timestamp())
                if not t_model:
                    quote = get_quotes(symbols)
                    t_model = TickersData()
                    t_model.symbol = symbols
                    t_model.last_price = quote[1]['price']
                    t_model.value_change = quote[0]['change']
                    t_model.percent_change = quote[0]['percent_change']
                    t_model.date_changed = now_ts

                elif t_model and (now_ts - t_model.date_changed) > 60:
                    quote = get_quotes(symbols)
                    t_model.last_price = quote[1]['price']
                    t_model.value_change = quote[0]['change']
                    t_model.percent_change = quote[0]['percent_change']
                    t_model.date_changed = now_ts
                db.session.add(t_model)
                db.session.commit()

                if alerts.first():
                    return 'This ticker already was added'
                else:
                    m.user = u_id
                    m.symbols = form.get('symbols')
                    m.analytics = form.get('analytics')
                    m.news = form.get('news')
                    m.enabled = form.get('enabled')
                    db.session.add(m)
            db.session.commit()
            return 'Done'
        return render_template('portfolio.html', form=form, tickers=tickers,
                               companyTicker='AAPL | Apple Inc.', username=username, authenticated=authenticated,
                               ticker=ticker, userID=current_user.get_id())
    else:
        return redirect('/')


@main.route('/portfolio/delete/<alert_id>', methods=['GET'])
def delete_alert(alert_id):
    if current_user.is_authenticated:
        u_id = current_user.get_id()
        alerts = Alerts.query.filter_by(user=u_id, id=alert_id)
        if alerts.first():
            db.session.delete(alerts.first())
            db.session.commit()
            return 'Deleted'
        else:
            return abort(404)
    else:
        return redirect('/')


@main.route('/user/watchlist')
def watchlist():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    return render_template('/user/watchlist.html', username=username, authenticated=authenticated)


@main.route('/user/setting', methods=['POST', 'GET'])
def user_setting():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'

    if request.method == 'POST':
        current_user.email = request.form.get('email')
        current_user.city = request.form.get('city')
        if not current_user.f_name or not current_user.l_name:
            current_user.f_name = request.form.get('f_name')
            current_user.l_name = request.form.get('l_name')
        current_user.phone = request.form.get('phone')
        current_user.about = request.form.get('about')
        current_user.zip = request.form.get('zip')
        current_user.address = request.form.get('address')
        current_user.username = request.form.get('username')
        db.session.add(current_user)
        db.session.commit()

    return render_template('user/setting.html', username=username, user=current_user,
                           authenticated=authenticated, companyTicker='AAPL | Apple Inc.')


@main.route('/user/setting/image', methods=['POST', 'GET'])
def change_image():
    if current_user.is_authenticated:
        if 'file' not in request.files:
            return 'fail'
        file = request.files['file']
        if file.filename == '':
            return 'fail'
        if file:
            filename = secure_filename(file.filename)
            current_user.avatar_link = filename
            db.session.add(current_user)
            db.session.commit()
            file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            return '/user/image/' + filename
    return 'fail'


@main.route('/user/image/<filename>')
def user_image(filename):
    return send_from_directory(Config.UPLOAD_FOLDER, filename)


# dropdown services
@main.route('/worldnews')
def worldnews():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'

    try:
        conn = sqlite3.connect('database.db')
        mycursor = conn.cursor()
        mycursor.execute("select * from worldnews")
        marketNews = mycursor.fetchall()

        def wsj(string):
            return 'wallstreetjournal' in string

        def bbc(string):
            return 'bbc' in string

        def nytimes(string):
            return 'nytimes' in string

        def nasdaq(string):
            return 'nasdaq' in string

        def marketwatch(string):
            return 'marketwatch' in string

        def investing(string):
            return 'investing' in string

        wsj = [string for string in marketNews if wsj(string)][0:3]
        nytimes = [string for string in marketNews if nytimes(string)][0:3]
        bbc = [string for string in marketNews if bbc(string)][0:3]
        nasdaq = [string for string in marketNews if nasdaq(string)][0:3]
        marketwatch = [string for string in marketNews if marketwatch(string)][0:3]
        investing = [string for string in marketNews if investing(string)][0:3]
        return render_template('world_news.html', username=username, authenticated=authenticated, wsj=wsj,
                               bbc=bbc, nytimes=nytimes, nasdaq=nasdaq, marketwatch=marketwatch, investing=investing,
                               published=marketNews[0:3], companyTicker='AAPL | Apple Inc.')
    except:
        return render_template('world_news.html', username=username, authenticated=authenticated,
                               companyTicker='AAPL | Apple Inc.')


@main.route('/worldnews/<namecompany>', methods=['GET', 'POST'])
def world_news_page(namecompany):
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'

    try:
        conn = sqlite3.connect('database.db')
        mycursor = conn.cursor()
        mycursor.execute("select * from worldnews")
        marketNews = mycursor.fetchall()
        x = f'{namecompany}'

        def searchNews(string):
            return x in string

        news = [string for string in marketNews if searchNews(string)]
        return render_template('market_news_page.html', username=username, authenticated=authenticated,
                               string=news, companyTicker='AAPL | Apple Inc.')
    except:
        return render_template('market_news_page.html', username=username,
                               authenticated=authenticated, companyTicker='AAPL | Apple Inc.')


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(username=form.email.data).first()

        if user or email:
            form.username.errors.append('This username or email is already taken')
            return render_template('sign_up.html', form=form, message='')
        else:
            if form.password.data == form.passwordConfirm.data:
                hashedPassword = generate_password_hash(form.password.data, method='sha256')
                newUser = User(username=form.username.data, email=form.email.data, password=hashedPassword,
                               emailConfirmed=False, role='client', country=form.country.data)
                db.session.add(newUser)
                db.session.commit()

                ### send token to email
                subject = "Confirm your email"
                token = ts.dumps(form.email.data, salt='email-confirm-key')

                confirmUrl = url_for('main.confirmEmail', token=token, _external=True)
                html = render_template('email/activate.html', confirmUrl=confirmUrl)

                link = str('https://jy.com.ua/confirm/') + str(token)

                html = "Your J&Y Invest account was successfully created. Please click the link below to confirm your email address and activate your account:<br><br>" + str(
                    link) + "<br><br>J&Y INVESTMENT<br>Trust. Growth. Experience."
                sendEmail(form.email.data, subject, html, mail)

                return render_template('sign_up.html', form=form,
                                       message='Registration completed, please check your email')
            else:
                return render_template('sign_up.html', form=form, message='')
    authenticated = current_user.is_authenticated

    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    return render_template('sign_up.html', username=username, authenticated=authenticated, form=form, message='')


@main.route('/confirm/<token>')
def confirmEmail(token):
    try:
        email = ts.loads(token, salt="email-confirm-key", max_age=86400)
    except:
        return render_template('invalid_token.html')

    user = User.query.filter_by(email=email).first()
    user.emailConfirmed = True
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('main.login'))


@main.route('/resetpassword', methods=['GET', 'POST'])
def resset_pass():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    form = EmailForm()
    if form.validate_on_submit():
        subject = "Password reset"

        token = ts.dumps(form.email.data, salt='recover-key')

        recover_url = url_for('main.reset_with_token', token=token, _external=True)

        html = render_template('email/resetPassword.html', username=username, recover_url=recover_url)

        sendEmail(form.email.data, subject, html, mail)

        return "Your password has been reseted, check your email"

    return render_template('reset_pass.html', username=username, authenticated=authenticated, form=form, message='')


@main.route('/reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
    try:
        email = ts.loads(token, salt="recover-key", max_age=86400)
    except:
        abort(404)

    form = PasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first_or_404()

        new_password = form.password.data
        new_password_hash = generate_password_hash(new_password, method='sha256')

        user.password = new_password_hash

        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('reset_with_token.html', form=form, token=token)


@main.route('/admin', methods=['GET', 'POST'])
def admin():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
        if not current_user.role == 'admin':
            return redirect('/')
    else:
        return redirect('/')
    if request.method == "POST":
        userName = request.form['userName']
        userEmail = request.form['userEmail']
        userPassword = request.form['userPassword']
        hashedPassword = generate_password_hash(userPassword, method='sha256')
        newUser = User(username=userName, email=userEmail, password=hashedPassword)
        try:
            db.session.add(newUser)
            db.session.commit()
            return render_template('admin.html', username=username, authenticated=authenticated,
                                   items=User.query.all(), companyTicker='AAPL | Apple Inc.')
        except:
            return "error"

    else:
        return render_template('admin.html', username=username, authenticated=authenticated,
                               items=User.query.all(), companyTicker='AAPL | Apple Inc.')


@main.route('/admin/delete/<int:id>', methods=['GET', 'POST'])
def adminDeleteUser(id):
    obj = User.query.get_or_404(id)
    try:
        db.session.delete(obj)
        db.session.commit()
        return redirect('/admin')
    except:
        return "Whith delete data for database error"


@main.route('/admin/addTicker', methods=['GET', 'POST'])
def addTicker():
    authenticated = current_user.is_authenticated
    if authenticated:
        username = current_user.username
    else:
        username = 'go to registration'
    return render_template('addticker.html', username=username, authenticated=authenticated)