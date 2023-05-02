import time
import tinydb
import random


def submitRequest(db,username,firstName,lastName,university,studyField,experience):
    table = db.table("verificationRequests")
    query = tinydb.Query()

    if table.search(query['username'] == username):
        return False
    data = {
        "username"  :  username,
        "firstName"  :  firstName,
        "lastName"  :  lastName,
        "university"  :  university,
        "studyField"  :  studyField,
        "experience"  :   experience,
    }
    table.insert(data)
    return True