import time
import tinydb
import random

#todo: check if vote exists and undo it for opposite voting
def add_vote(db, user, postID, kind):
    votes = db.table('votes')
    Vote = tinydb.Query()
    hasVoted = votes.search((Vote['user_id'] == user['id']) & (Vote['post_id'] == postID))
    if hasVoted:
        votes.remove((Vote['user_id'] == user['id']) & (Vote['post_id'] == postID))
    voteRecord = {
        'id':len(votes),
        'post_id':postID,
        'user_id':user['id'],
        'kind':kind
    }
    return votes.insert(voteRecord)


def getVotes( db, postID:int, kind:int ):
    VoteTable = db.table('votes')
    query = tinydb.Query()
    votes = VoteTable.search((query['post_id'] == postID) & (query['kind'] == kind))
    if len(votes):
        return votes
    return []
