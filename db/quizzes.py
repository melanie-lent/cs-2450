import time
import tinydb
import random

def insertQuestion(db, question):
    quizzes = db.table('questions')
    question['id'] = len(quizzes)
    inserted = quizzes.insert(question)
    return question

def insertChoices(db, answers):
    table = db.table('choices')
    qsID = answers["question_id"]
    opts = ["A","B","C","D"]
    A = answers['answers']
    for a in range(len(A)):
        item = {
            "id" : len(table),
            "choice": opts[a % len(opts)],
            "content": A[a],
            "question_id": int(qsID),
        }
        table.insert(item)
    return 

def getAnswers(db,quizID,user):
    table = db.table('answers')
    query = tinydb.Query() 
    existingAnswers = table.search((query['question_id'] == int(quizID)) & (query['username'] == user['username']) )
    if existingAnswers is None:
        return False
    return existingAnswers

def hasAnswers(db,quizID,user):
    table = db.table('answers')
    query = tinydb.Query() 
    existingAnswers = table.search((query['question_id'] == int(quizID)) & (query['username'] == user['username']) )
    # print(existingAnswers)
    return bool(len(existingAnswers))

def insertAnswers(db,answer):
    table = db.table('answers')
    answer['id'] = len(table)
    table.insert( answer )
    return

def getChoices(db,quizID,user):
    table = db.table('choices')
    query = tinydb.Query() 
    existing = table.search((query['question_id'] == int(quizID)) )
    print(existing)
    if not len(existing):
        return []
    return existing



def getQuizzes(db,user):
    question = db.table('questions')
    query = tinydb.Query() 
    allQuestions = question.all()
    unanswered = []
    for q in allQuestions:
        if not hasAnswers(db,q['id'],user):
            unanswered.append(q)
    return [{
                "question":e,
                "choices": getChoices(db,e['id'],user),
            } for e in unanswered]
        
        








# def get_posts(db, user):
#     posts = db.table('posts')
#     Post = tinydb.Query()
#     postsearch = posts.search(Post.username==user['username'])
#     if postsearch is None:
#         postsearch = []
#     votes = db.table('votes')
#     results = [
#         {
#             **post ,
#             **{
#             "upvotes"  : len(getVotes(db,int(post['id']),1)) ,
#             "downvotes": len(getVotes(db,int(post['id']),0)) ,
#             "comments" : getComments(db,post['id'])
#             }
#         }
#         for post in postsearch]
#     return results
