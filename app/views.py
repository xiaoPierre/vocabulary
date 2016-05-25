from flask import render_template, flash, redirect, request
from app import app
from app.forms import LoginForm
from app.Crawler.crawlWord import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.Model.Word import *
from app.Model.User import *


# index view function suppressed for brevity
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title='Sign In',
        form=form)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/signuptreatement', methods=['GET', 'POST'])
def signuptreatement():
    firstName=request.form['firstName']
    lastName=request.form['lastName']
    email=request.form['email']
    password=request.form['password']
    passwordConfirm=request.form['passwordConfirm']
    assert(password == passwordConfirm)
    if (passwordConfirm != password):
        return render_template('index.html')
    engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    user = User(firstName=firstName, lastName=lastName,
                email=email, password=password)
    session.add(user)
    session.commit()
    session.close()
    return render_template('thanks.html', firstName=firstName, lastName=lastName)


@app.route('/lookup')
def lookup():
    word = request.args.get('q')
    definition = lookUpWord(word)
    engine = create_engine("postgresql://erkang:rrrrrrrr@localhost/test")
    Session = sessionmaker(bind=engine)
    session = Session()
    for element in session.query(Word).filter_by(ortho=word):
        print(element)
    print(definition)
    return render_template('word.html',
                           word=definition)