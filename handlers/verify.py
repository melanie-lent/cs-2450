import flask
import tinydb

from handlers import copy
from db import posts, users, verification

blueprint = flask.Blueprint("verify", __name__)

@blueprint.route('/verify', methods=['GET'])
def verify():
    """Adds 'verified' status to a user. Essentially lets them make quizzes."""
    db = tinydb.TinyDB('db.json')
    # make sure the user is logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')
    user = users.get_user(db, username, password)
    if username is None and password is None:
        return flask.redirect(flask.url_for('login.loginscreen'))
    return flask.render_template('verification.html')


@blueprint.route('/verify', methods=['POST'])
def submitRequest():
    """Allows a verified user to create a multiple-choice or open answer quiz, with one question."""
    db = tinydb.TinyDB('db.json')

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))
    data = {
        "username" : username,
        "firstName" : flask.request.form.get('firstName'),
        "lastName" : flask.request.form.get('lastName'),
        "university" : flask.request.form.get('university'),
        "studyField" : flask.request.form.get('studyField'),
        "experience" : flask.request.form.get('experience'),
    }
    if not verification.submitRequest(db,**data):
        flask.flash("You Already Have An Active Request",'error')

    """ok now how do we go about making the quiz?"""
    return flask.redirect(flask.url_for('login.index'))
