import time
import tinydb
import random
from .votes import getVotes
from .comments import getComments

def add_post(db, user, text):
    posts = db.table('posts')
    Post = tinydb.Query()
    postRecord = {
     'username': user['username'],
     'text': text,
     'time': time.time(),
     'id': len(posts),
    }
    # Can't insert empty posts
    if postRecord['text'] == '':
        return
    inserted = posts.insert(postRecord)
    return inserted



def get_posts(db, user):
    posts = db.table('posts')
    Post = tinydb.Query()
    postsearch = posts.search(Post.username==user['username'])
    if postsearch is None:
        postsearch = []
    votes = db.table('votes')
    results = [ 
        {
            **post , 
            **{
            "upvotes"  : len(getVotes(db,int(post['id']),1)) ,
            "downvotes": len(getVotes(db,int(post['id']),0)) ,
            "comments" : getComments(db,post['id'])
            }
        }
        for post in postsearch]
    return results




# def get_post(db, post): #I have no idea if this works
#     posts = db.table('posts')
#     Post = tinydb.Query()
#     searched = posts.search(Post.username==user['username'] & Post.text==post['text'])
#     print('get post:', searched)
#     return searched
