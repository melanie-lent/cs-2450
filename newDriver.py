#!/usr/bin/env python3
import unittest, tinydb

from handlers import copy, friends, login, posts, quizzes, verify
from db import comments, posts, quizzes, users, verification, votes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
# from seleniumrequests import

USERNAME = "YouStoleMyToast"
PASSWORD = "passwords123"
url = "http://localhost:5000/"

# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# driver = webdriver.Chrome(executable_path="./operadriver.exe")
#
# # driver.get(url)
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
        self.driver = webdriver.Chrome(executable_path="./operadriver.exe",options=options)
        self.driver.get(url)

    def tearDown(self):
        self.driver.close()

    def get_login_buttons(self):
        loginButton =  self.driver.find_element_by_id("LoginButton")
        createButton = self.driver.find_element_by_id("CreateAccountButton")
        return (loginButton,createButton)

    def get_login_inputs(self):
        try:
            username = self.driver.find_element_by_name("username")
            password = self.driver.find_element_by_name("password")
            return (username, password)
        except NoSuchElementException:
            self.fail("No username/password elements found")
        except Exception as e:
            self.fail(f"Caught Unknown Exception {e}")


    # def test_login(self):
    #     username_input, password_input = self.get_login_inputs()
    #     loginButton, createButton = self.get_login_buttons()
    #     try:
    #         username_input.send_keys(USERNAME)
    #         password_input.send_keys(PASSWORD)
    #         createButton.click()
    #     except Exception as e:
    #         self.fail(f"Unknown Exception When Logging In")

        # try:
        #     element = WebDriverWait(driver, 10).until(
        # self.driver.presence_of_element_located((By.name, "post")))
        # finally:
        #     pass


    # def get_post_elements(self):
    #     try:
    #         post_input = self.driver.find_element_by_name("post")
    #         post_submit_button = self.driver.find_element_by_name("post-submit")
    #         post_upvote_button = self.driver.find_element_by_name('upvote')
    #         post_downvote_button = self.driver.find_element_by_name('downvote')
    #         return (post_input, post_submit_button, post_upvote_button, post_downvote_button)
    #     except NoSuchElementException:
    #         self.fail("No post input/submit elements found")
    #     except Exception as e:
    #         self.fail(f"Caught Unknown Exception {e}")
    #
    # def test_post(self):
    #     post_input, post_submit, post_upvote, post_downvote = self.get_post_elements()
    #     post_input.send_keys("Post Message")
    #     try:
    #         post_submit.click()
    #     except Exception as e:
    #         self.fail(f"Caught Unknown Exception Creating A Post: {e}")

    # def test_upvote(self):
    #     post_input, post_submit, post_upvote, post_downvote = self.get_post_elements()
    #     return

    def test_verify(self):
        try:
            # Branch 1: Approve user

            db = tinydb.TinyDB('db.json')

            # Case 1: User experience greater than 2
            # username_input, password_input = self.get_login_inputs()
            # user = users.new_user(db, 'vtest_user_1', 'test')
            # loginButton, createButton = self.get_login_buttons()
            USERNAME, PASSWORD = 'vtest_user_1', 'test'
            # username_input.send_keys(USERNAME)
            # password_input.send_keys(PASSWORD)
            # loginButton.click()
            response = driver.get('POST', 'http://localhost:5000/login', data={'username': USERNAME, 'password': PASSWORD})
            # verificationLink = self.driver.find_element_by_id("verification-link")
            # login.login()

            # # Case 2: User experience equal to or less than 2
            # user = new_user(db, 'verification_test_user_2', 'test')
            #
            # # Case 3: User experience not supplied
            # user = new_user(db, 'verification_test_user_3', 'test')
        except Exception as e:
            self.fail(f"Caught Unknown Exception Verifying: {e}")






if __name__ == "__main__":
    unittest.main()
