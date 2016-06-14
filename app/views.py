from flask import render_template, flash, redirect, request, jsonify
from app import app
from app.Exercise.ExerciseGenerator import *
from app.Model.User import *
from app.BDD.connectBDD import *
from app.Dictionary.dictionary import *
from app.Crawler.crawlArticle import *
from app.Exercise.ExerciseGenerator import *
from app.Exercise.LevelTest import getLevelTests
from app.Article.analyseArticle import *


# index view function suppressed for brevity
@app.route('/')
@app.route('/index')
def index():
    test = TotalRandomExerciseGenerator().generateRandomExercise()
    article = crawlRandomArticle()
    return render_template('index.html', test = test, article = article)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html',
        title='Sign In')



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
        return render_template('base.html')
    with connectBDD() as session:
        user = User(firstName=firstName, lastName=lastName,
                    email=email, password=password)
        session.add(user)
        session.commit()
    return redirect('levelTest')


@app.route('/lookup')
def lookup():
    word = request.args.get('q')
    wordObj = crawlWord(word)
    testObj = RandomExerciseGenerator().generateExercise(word)
    return render_template('word.html',
                           word=wordObj,
                           test=testObj)

@app.route('/findPrefix', methods=['GET'])
def findPrefix():
    pre = request.args.get('prefix', '', type=str)
    return jsonify(result=suggestWord(pre))

@app.route('/analyseArticle', methods=['POST', 'GET'])
def analyse():
    texte = "Le dernier, Albus, est confronté à l’héritage de son père et aux forces de l’obscurité.La pièce de théâtre sera jouée à Londres, au Palace Theatre"
    return jsonify(result=analyseArticle(texte))


@app.route('/levelTest')
def levelTest():
    tests = getLevelTests()
    return render_template('levelTest.html', levelTest=tests)

@app.route('/getRandomTest')
def getRandomTest():
    test = TotalRandomExerciseGenerator().generateRandomExercise()
    topic = test.topic
    choices = test.choices
    answer = test.answer
    image = test.isImageExo
    return jsonify(topic = topic, choices = choices, answer = answer, image=image)




'''
@app.route('/loginTreatment'):
def loginTreatment():
    email=request.form['email']
    password = request.form['password']
    with connectBDD() as session:
        user = session.query(User).filter(User.email==email)
        if user.password == password:
            pass
'''