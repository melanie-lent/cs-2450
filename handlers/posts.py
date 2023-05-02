import flask
import tinydb
from db import posts, users, votes, comments

blueprint = flask.Blueprint("posts", __name__)

@blueprint.route('/create_quiz', methods=['POST'])
def create_quiz():
    """Allows a verified user to create a multiple-choice or open answer quiz, with one question."""
    db = tinydb.TinyDB('db.json')

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))

    if not get_permissions(db, user):
        flask.flash('You do not have permission to do that.', 'danger')
        return flask.redirect(flask.url_for('login.index'))

    quiz = flask.request.form.get('quiz')
    posts.add_post(db, user, quiz)

    """ok now how do we go about making the quiz?"""
    return flask.redirect(flask.url_for('login.index'))


@blueprint.route('/post', methods=['POST'])
def post():
    """Creates a new post."""
    db = tinydb.TinyDB('db.json')

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))

    post = flask.request.form.get('post')
    posts.add_post(db, user, post)

    return flask.redirect(flask.url_for('login.index'))

# @blueprint.route("/post/vote/<postID>/<kind>", methods=['POST'])
@blueprint.route("/post/vote/<kind>", methods=['POST'])
def vote(kind):
    kind = int(kind)
    if kind > 1:
        return  flask.redirect(flask.url_for('login.index'))
    else:
        db = tinydb.TinyDB('db.json')
        username = flask.request.cookies.get('username')
        password = flask.request.cookies.get('password')
        user = users.get_user(db,username,password)
        postID = int(flask.request.form.get('postID'))
        votes.add_vote(db, user, postID, kind)
    return flask.redirect(flask.url_for('login.index'))

@blueprint.route("/post/comment/", methods=['POST'])
def comment():
    db = tinydb.TinyDB('db.json')
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')
    user = users.get_user(db,username,password)

    postID = int(flask.request.form.get('postID'))
    comment = flask.request.form.get('comment')

    comments.Insert(db,user,postID,comment)
    return flask.redirect(flask.url_for('login.index'))
