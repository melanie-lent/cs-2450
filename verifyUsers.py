import time
import tinydb
import os,sys


def getRequests(db):
    table = db.table('verificationRequests')
    active_requests = table.all()
    print(active_requests)
    return active_requests

def approveUser(db,username):
    table = db.table('users')
    query = tinydb.Query()
    table.update({"permissions":1},query['username'] == username)
    return True

def deleteRequest(db,username):
    table = db.table('verificationRequests')
    query = tinydb.Query()
    table.remove(query['username'] == username)
    return True


def scanUsers(db,activeRequests,auto=False):
    for i in activeRequests:
        for key in i:
            print(f"{key}\t{i[key]}")
        if not auto:
            try:
                approve = input("Approve This User?").upper()[0] == "Y"
            except:
                approve = False
        else:
            approve = int(i["experience"]) > 2
        if approve:
            approveUser(db,i["username"])
        deleteRequest(db,i["username"])
    return


def main(args):
    if len(args) > 1:
        auto=bool(int(args[1]))
    db = tinydb.TinyDB('db.json')
    rq = getRequests(db)
    scanUsers(db,rq,True)


if __name__ == "__main__":
    main(sys.argv)

# usage
#  python3 verifyUsers.py 1
