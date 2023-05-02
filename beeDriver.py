import time
import random
import unittest, tinydb, time, verifyUsers

from pathlib import Path
from handlers import copy, friends, login, posts, quizzes, verify
from db import comments, posts, quizzes, users, verification, votes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

USER = "YouStoleMyToastt"
PASS = "passwords123"
url = "http://localhost:5000/"

db = tinydb.TinyDB('db.json')

# def get_login_buttons():
#     loginButton = driver.find_element_by_id("LoginButton")
#     createButton = driver.find_element_by_id("CreateAccountButton")
#     return loginButton,createButton
#
# def test_login():
#     username = driver.find_element_by_name("username")
#     password = driver.find_element_by_name("password")
#     username.send_keys(USERNAME)
#     password.send_keys(PASSWORD)
#     loginButton, createButton = get_login_buttons()
#     loginButton.click()

class Test(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument('log-level=3')
        self.driver = webdriver.Chrome(executable_path="./operadriver.exe",options=options)
        # self.driver.get(url)

    def tearDown(self):
        self.driver.close()

    def getQuizElements(self):
        elements = ["question"] + [ "choice" + str(i) for i in range(1,5)] + ["submit"]
        res = []
        for el in elements:
            try:
                res.append(self.driver.find_element_by_name(el))
            except NoSuchElementException:
                self.fail("Expected Quiz Elements, Found None")
        return res


    def findLoginElements(self,create=False):
        try:
            username = self.driver.find_element_by_name("username")
        except NoSuchElementException:
            self.fail("No Username Element")
        try:
            password = self.driver.find_element_by_name("password")
        except NoSuchElementException:
            self.fail("No Password Element")
        if create:
            try:
                button = self.driver.find_element_by_id("CreateAccountButton")
            except NoSuchElementException:
                self.fail("No account creation button")
        else:
            try:
                button = self.driver.find_element_by_id("LoginButton")
            except NoSuchElementException:
                self.fail("No login button")
        return username,password,button

    def handleVerificationFields(self):
        try:
            fn = self.driver.find_element_by_name("firstName")
        except NoSuchElementException:
            self.fail("No firstName Element")
        try:
            ln = self.driver.find_element_by_name("lastName")
        except NoSuchElementException:
            self.fail("No lastName Element")
        try:
            university = self.driver.find_element_by_name("university")
        except NoSuchElementException:
            self.fail("No university Element")
        try:
            field = self.driver.find_element_by_name("studyField")
        except NoSuchElementException:
            self.fail("No studyField Element")
        try:
            experience = self.driver.find_element_by_name("experience")
        except NoSuchElementException:
            self.fail("No experience Element")
        return fn,ln,university,field,experience

    def handleLoginCreate(self, user, pw, create=False):
        self.driver.get(url)
        username,password,button = self.findLoginElements(create)
        username.send_keys(user)
        password.send_keys(pw)
        button.click()



    def handleSubmitVerificationForm(self):
        fn,ln,university,field,experience = self.handleVerificationFields()
        fn.send_keys("ver")
        ln.send_keys("test")
        university.send_keys("dixie state university")
        field.send_keys("computers")
        experience.send_keys("3")
        try:
            submit = self.driver.find_element_by_id("submit")
        except NoSuchElementException:
            self.fail("No submit Element")

        submit.click()

    def handleFindVerificationLink(self):
        try:
            verification_link = self.driver.find_element_by_id("verification-link")
            return verification_link
        except NoSuchElementException:
            self.fail("No verification link")

    def exists(self,kind="id",field=None):
        if kind == "id":
            f = self.driver.find_element_by_id
        else:
            f = self.driver.find_element_by_name
        try:
            f(field)
            return True
        except NoSuchElementException:
            return False

    def verifyQuestionCreated(self,question):
        table = db.table('questions')
        query = tinydb.Query()
        existing = table.search((query['question'] == question) )
        return bool(len(existing))

    def submitQuiz(self,question,withInput=True):
        q,i1,i2,i3,i4,button = self.getQuizElements()
        q.send_keys(question)
        if withInput:
            i1.send_keys("This Is My Input")
            i2.send_keys("This Is My Input")
            i3.send_keys("This Is My Input")
            i4.send_keys("This Is My Input")
        button.click()
        return

    def verifyVerificationRequested(self,username):
        table = db.table('verificationRequests')
        query = tinydb.Query()
        existing = table.search((query['username'] == username) )
        return bool(len(existing))


    def test_verification_submission(self):
        unverifiedUser = ["Hell","World"]
        self.handleLoginCreate(*unverifiedUser)
        time.sleep(1)
        self.assertTrue(self.exists("id","verification-link"),"Checking Verification Is Available")
        link = self.handleFindVerificationLink()
        link.click()
        time.sleep(1)
        self.handleSubmitVerificationForm()
        self.assertTrue(self.exists("id","titleText"),"Checking For Redirect After Submission")
        self.assertTrue(self.verifyVerificationRequested(unverifiedUser[0]),"Checking For Verification Data In Database")

    def handleCreateEmptyQuiz(self):
        q,i1,i2,i3,i4,button = self.getQuizElements()
        i1.send_keys("This Is My Input")
        i2.send_keys("This Is My Input")
        i3.send_keys("This Is My Input")
        i4.send_keys("This Is My Input")
        button.click()
        return

    def test_verified_user_creates_quiz_without_question(self):
        existing_user = ["YouStoleMyToast","passwords123"]
        self.handleLoginCreate(*existing_user)
        self.assertTrue(self.exists("id","quiz-link"),"Login")
        self.driver.find_element_by_id("quiz-link").click()
        time.sleep(.5)
        self.handleCreateEmptyQuiz()
        time.sleep(.5)
        self.assertFalse(self.exists("id","titleText"),"Verifying Redirect After Submission")
        self.assertFalse(self.verifyQuestionCreated(''),"Checking Database For Question")

    def test_verified_user_creates_quiz_with_options(self):
        existing_user = ["YouStoleMyToast","passwords123"]
        self.handleLoginCreate(*existing_user)
        self.assertTrue(self.exists("id","quiz-link"),"Login")
        self.driver.find_element_by_id("quiz-link").click()
        time.sleep(.5)
        question = f"This Is My Question {random.randint(1,10000000)}"
        self.submitQuiz(question, True)
        time.sleep(.5)
        self.assertTrue(self.exists("id","titleText"),"Verifying Redirect After Submission")
        self.assertTrue(self.verifyQuestionCreated(question),"Checking Database For Question")

    def test_verified_user_creates_quiz_without_options(self):
        existing_user = ["YouStoleMyToast","passwords123"]
        self.handleLoginCreate(*existing_user)
        self.assertTrue(self.exists("id","quiz-link"),"Login")
        self.driver.find_element_by_id("quiz-link").click()
        time.sleep(.5)
        question = f"This Is My Question {random.randint(1,10000000)}"
        self.submitQuiz(question, False)
        time.sleep(.5)
        self.assertTrue(self.exists("id","titleText"),"Verifying Redirect After Submission")
        self.assertTrue(self.verifyQuestionCreated(question),"Checking Database For Question")

    def test_authentication_valid(self):
        existing_user = ["YouStoleMyToast","passwords123"]
        self.handleLoginCreate(*existing_user)
        self.assertTrue(self.exists("id","titleText"),"Login ")

    def test_authentication_invalid_password(self):
        existing_user = ["YouStoleMyToast","passws123"]
        self.handleLoginCreate(*existing_user)
        self.assertFalse(self.exists("id","titleText"),"Login ")

    def test_account_create(self):
        not_existing = ["Hell","World",True]
        self.handleLoginCreate(*not_existing)
        self.assertFalse(self.exists("id","titleText"),"Invalid Login")

    def test_authentication_invalid(self):
        not_existing = ["Hllo","World"]
        self.handleLoginCreate(*not_existing)
        self.assertFalse(self.exists("id","titleText"),"Invalid Login")


    def handleCreatePost(self):
        try:
            textField = self.driver.find_element_by_name('post')
            textField.send_keys('test')
        except NoSuchElementException:
            self.fail("No post input box")
        try:
            submitButton = self.driver.find_element_by_name('post-submit')
            submitButton.click()
        except NoSuchElementException:
            self.fail("No post submit button")

    def handleUpvote(self):
        try:
            upButton = self.driver.find_element_by_name('upvote')
            upButton.click()
        except NoSuchElementException:
            self.fail("No upvote button")

    def handleDownvote(self):
        try:
            downButton = self.driver.find_element_by_name('downvote')
            downButton.click()
        except NoSuchElementException:
            self.fail("No downvote button")

    def handleGetUpvoteCount(self):
        try:
            counter = self.driver.find_element_by_id('up-count')
            return counter.get_attribute('innerText')
        except NoSuchElementException:
            self.fail('No upvote count')

    def handleGetDownvoteCount(self):
        try:
            counter = self.driver.find_element_by_id('down-count')
            return counter.get_attribute('innerText')
        except NoSuchElementException:
            self.fail('No downvote count')

    def checkPostsExist(self):
        try:
            post = self.driver.find_elements_by_class_name('post')
            if len(post) > 0:
                return True
            else:
                return False
        except NoSuchElementException:
            self.fail('No elements with class post')

    def test_create_post(self):
        existing_user = ['YouStoleMyToast', 'passwords123']
        self.handleLoginCreate(*existing_user)
        self.handleCreatePost()
        self.assertTrue(self.checkPostsExist())

    def test_upvote(self):
        existing_user = ['YouStoleMyToast', 'passwords123']
        self.handleLoginCreate(*existing_user)
        self.handleCreatePost()
        before = self.handleGetUpvoteCount()
        self.handleUpvote()
        after = self.handleGetUpvoteCount()
        self.assertNotEqual(before, after)

    def test_downvote(self):
        existing_user = ['YouStoleMyToast', 'passwords123']
        self.handleLoginCreate(*existing_user)
        self.handleCreatePost()
        before = self.handleGetDownvoteCount()
        self.handleDownvote()
        after = self.handleGetDownvoteCount()
        self.assertNotEqual(before, after)


    def createComment(self):
        try:
            commentField = self.driver.find_element_by_name('comment')
            commentField.send_keys('test')
        except NoSuchElementException:
            self.fail('No comment field')
        try:
            submitButton = self.driver.find_element_by_name('submit-comment')
            submitButton.click()
        except NoSuchElementException:
            self.fail('No comment button')

    def getCommentCount(self):
        comments = self.driver.find_elements_by_class_name('comment-text')
        return len(comments)

    def test_comment(self):
        existing_user = ['YouStoleMyToast', 'passwords123']
        self.handleLoginCreate(*existing_user)
        self.handleCreatePost()
        before = self.getCommentCount()
        self.createComment()
        after = self.getCommentCount()
        self.assertNotEqual(before, after)

    def handleGetUserPermissions(self, username):
        return users.get_permissions_by_name(db, username)

    def test_verified_user_permissions(self):
        unverified_user = ['newww', 'user']
        self.handleLoginCreate(*unverified_user)

        print(users.get_user_by_name(db, unverified_user[0]))

        before = self.handleGetUserPermissions(unverified_user[0])
        link = self.handleFindVerificationLink()
        link.click()
        time.sleep(1)
        self.handleSubmitVerificationForm()
        verifyUsers.approveUser(db, unverified_user[0])
        after = self.handleGetUserPermissions(unverified_user[0])
        self.assertNotEqual(before, after)



if __name__ == "__main__":
    unittest.main()
