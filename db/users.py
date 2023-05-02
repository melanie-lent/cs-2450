import tinydb
import random

def new_user(db, username, password):
    users = db.table('users')
    User = tinydb.Query()
    id = len(users)
    if users.get(User.username == username):
        return None
    userRecord = {
        'username': username,
        'password': password,
        'friends': [],
        'id': id,
        'permissions': 0
    }
    # permissions change to 1 when user is verified
    return users.insert(userRecord)

def get_user(db, username, password):
    users = db.table('users')
    User = tinydb.Query()
    return users.get((User.username == username) & (User.password == password))

def get_user_by_name(db, username):
    users = db.table('users')
    User = tinydb.Query()
    return users.get(User.username == username)

def delete_user(db, username, password):
    users = db.table('users')
    User = tinydb.Query()
    return users.remove((User.username == username) & (User.password == password))

def add_user_friend(db, user, friend):
    users = db.table('users')
    User = tinydb.Query()
    if friend not in user['friends']:
        if users.get(User.username == friend):
            user['friends'].append(friend)
            users.upsert(user, (User.username == user['username']) &
                    (User.password == user['password']))
            return 'Friend {} added successfully!'.format(friend), 'success'
        return 'User {} does not exist.'.format(friend), 'danger'
    return 'You are already friends with {}.'.format(friend), 'warning'

def remove_user_friend(db, user, friend):
    users = db.table('users')
    User = tinydb.Query()
    if friend in user['friends']:
        user['friends'].remove(friend)
        users.upsert(user, (User.username == user['username']) &
                (User.password == user['password']))
        return 'Friend {} successfully unfriended!'.format(friend), 'success'
    return 'You are not friends with {}.'.format(friend), 'warning'

def get_user_friends(db, user):
    users = db.table('users')
    User = tinydb.Query()
    friends = []
    for friend in user['friends']:
        friends.append(users.get(User.username == friend))
    return friends

def verify(db, user):
    users = db.table('users')
    User = tinydb.Query()
    user.update({ 'permissions': 1 }, User.id == user['id'])
    return 'Congratulations, you are now verified. You can now make quizzes.'

def get_permissions(db, user):
    users = db.table('users')
    User = tinydb.Query()
    user_perms = users.get(User.username == user['username'])
    return user_perms['permissions']

def get_permissions_by_name(db, name):
    users = db.table('users')
    User = tinydb.Query()
    print("NAME:", name)
    user_perms = users.get(User.username == name)
    print("USER_PERMS:", user_perms)
    return user_perms['permissions']
