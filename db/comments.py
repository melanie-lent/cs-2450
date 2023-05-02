import time
import tinydb
import random


def Insert(db,user,postID,comment):
    commentsTable = db.table("comments")
    query = tinydb.Query() 
    commentObj = {
        "id":len(commentsTable) + 1,
        "post_id" : postID,
        "user_id" : user['id'],
        "username" : user['username'],
        "content" : comment,
    }
    commentsTable.insert(commentObj)
    return True


def getComments(db,postID):
    commentsTable = db.table("comments")
    query = tinydb.Query() 
    data = commentsTable.search(query["post_id"] == postID)
    return data if data is not None else []
















