import flask
import tinydb
from db import users

# blueprint = flask.Blueprint("quizzes", __name__)

# @blueprint.route('/quizzes', methods=['GET'])
# def quizCreate():
#     """Adds 'verified' status to a user. Essentially lets them make quizzes."""
#     db = tinydb.TinyDB('db.json')
#     # make sure the user is logged in
#     username = flask.request.cookies.get('username')
#     password = flask.request.cookies.get('password')
#     user = users.get_user(db, username, password)
#     if username is None and password is None:
#         return flask.redirect(flask.url_for('login.loginscreen'))
#     return flask.render_template('quizCreate.html')

