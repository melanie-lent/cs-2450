import flask
import tinydb

from handlers import copy
from db import posts, users, quizzes

blueprint = flask.Blueprint("login", __name__)

@blueprint.route('/loginscreen')
def loginscreen():
    """Present a form to the user to enter their username and password."""
    db = tinydb.TinyDB('db.json')

    # First check if already logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    if username is not None and password is not None:
        if users.get_user(db, username, password):
            # If they are logged in, redirect them to the feed page
            flask.flash('You are already logged in.', 'warning')
            return flask.redirect(flask.url_for('login.index'))

    return flask.render_template('login.html', title=copy.title,
            subtitle=copy.subtitle)

@blueprint.route('/login', methods=['POST'])
def login():
    """Log in the user.

    Using the username and password fields on the form, create, delete, or
    log in a user, based on what button they click.
    """
    db = tinydb.TinyDB('db.json')

    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    resp = flask.make_response(flask.redirect(flask.url_for('login.index')))
    resp.set_cookie('username', username)
    resp.set_cookie('password', password)

    submit = flask.request.form.get('type')
    if submit == 'Create':
        if users.new_user(db, username, password) is None:
            resp.set_cookie('username', '', expires=0)
            resp.set_cookie('password', '', expires=0)
            flask.flash('Username {} already taken!'.format(username), 'danger')
            return flask.redirect(flask.url_for('login.loginscreen'))
        flask.flash('User {} created successfully!'.format(username), 'success')
    elif submit == 'Delete':
        if users.delete_user(db, username, password):
            resp.set_cookie('username', '', expires=0)
            resp.set_cookie('password', '', expires=0)
            flask.flash('User {} deleted successfully!'.format(username), 'success')

    return resp

@blueprint.route('/logout', methods=['POST'])
def logout():
    """Log out the user."""
    db = tinydb.TinyDB('db.json')

    resp = flask.make_response(flask.redirect(flask.url_for('login.loginscreen')))
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    return resp

@blueprint.route('/')
def index():
    """Serves the main feed page for the user."""
    db = tinydb.TinyDB('db.json')

    # make sure the user is logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')
    if username is None and password is None:
        return flask.redirect(flask.url_for('login.loginscreen'))
    user = users.get_user(db, username, password)
    if not user:
        flask.flash('Invalid credentials. Please try again.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))

    # get the info for the user's feed
    friends = users.get_user_friends(db, user)
    all_posts = []
    for friend in friends + [user]:
        all_posts += posts.get_posts(db, friend)

    # sort posts
    sorted_posts = sorted(all_posts, key=lambda post: post['time'], reverse=True)

    return flask.render_template('feed.html', title=copy.title,
            subtitle=copy.subtitle, user=user, username=username,
            friends=friends, posts=sorted_posts)





@blueprint.route('/quiz/Create', methods=['GET'])
def quizCreate():
    """Adds 'verified' status to a user. Essentially lets them make quizzes."""
    db = tinydb.TinyDB('db.json')
    # make sure the user is logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')
    user = users.get_user(db, username, password)
    if username is None and password is None:
        return flask.redirect(flask.url_for('login.loginscreen'))
    return flask.render_template('quizCreate.html')

@blueprint.route('/quiz/Create', methods=['POST'])
def createQuiz():
    """Adds 'verified' status to a user. Essentially lets them make quizzes."""
    db = tinydb.TinyDB('db.json')
    # make sure the user is logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')
    user = users.get_user(db, username, password)
    if username is None and password is None:
        return flask.redirect(flask.url_for('login.loginscreen'))
    question = {
        "user_id"      : int(user['id']),
        "username"     : username,
        "question"     : flask.request.form.get('question'),
    }
    qs = quizzes.insertQuestion(db,question)
    print(qs)
    if flask.request.form.get('choice1'):
        answers = [
            flask.request.form.get('choice1'),
            flask.request.form.get('choice2'),
            flask.request.form.get('choice3'),
            flask.request.form.get('choice4'),
        ]
        answerEntry = {
            "question_id": int(qs['id']),
            "answers" : answers,
        }
        quizzes.insertChoices(db,answerEntry)


    return flask.redirect(flask.url_for('login.index'))


@blueprint.route('/quizzes', methods=['GET'])
def quizView():
    """Adds 'verified' status to a user. Essentially lets them make quizzes."""
    db = tinydb.TinyDB('db.json')
    # make sure the user is logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')
    user = users.get_user(db, username, password)
    if username is None and password is None:
        return flask.redirect(flask.url_for('login.loginscreen'))
    qui=quizzes.getQuizzes(db,user)
    if not len(qui):
        flask.flash("There are no quizzes available at this time",'warning')
        return flask.redirect(flask.url_for('login.index'))
    return flask.render_template('quiz.html',quizzes=qui)



@blueprint.route('/quiz/answers', methods=['POST'])
def quizAnswer():
    """Adds 'verified' status to a user. Essentially lets them make quizzes."""
    db = tinydb.TinyDB('db.json')
    # make sure the user is logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')
    user = users.get_user(db, username, password)
    if username is None and password is None:
        return flask.redirect(flask.url_for('login.loginscreen'))
    answer = {
        "user_id" : user['id'],
        "username": username,
        "question_id" : int(flask.request.form.get('quizID')),
        "value" : flask.request.form.get('answer'),
    }
    quizzes.insertAnswers(db,answer)
    qui=quizzes.getQuizzes(db,user)
    if not len(qui):
        flask.flash("There are no quizzes available at this time",'warning')
        return flask.redirect(flask.url_for('login.index'))
    return flask.render_template('quiz.html',quizzes=qui)


