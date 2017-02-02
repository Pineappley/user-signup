#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)

def build_page(textarea_content):
    header = "<h1>Signup</h1>"
    signup_form = """
    <form method = 'post'>
      <label>Username: <input name="username"/></label></br>
      <label>Password: <input type="password" name="password"/></label></br>
      <label>Verify Password: <input type="password" name="verifypassword"/></label></br>
      <label>Email: <input type="text" name="email"/> </label></br>
    <input type="submit" name="Submit"/>
    </form>
        """
    return header + signup_form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)


    def post(self):
        content = """
        <h1>Signup</h1>
        <form method = 'post'>
            <label>Username: <input type = "text" name="username" value = "{}"></label>{}</br>
            <label>Password: <input type="password" name="password"/></label>{}</br>
            <label>Verify Password: <input type="password" name="verifypassword"/></label>{}</br>
            <label>Email: <input type="text" name="email" value = "{}"> </label>{}</br>
        <input type="submit" name="Submit"/>
        </form>
            """
        username = self.request.get("username")
        if username == "":
            error = "Please enter a username."
            user_error_element = "<p class='error'>" + cgi.escape(error, quote=True) + "</p>"
        elif valid_username(username) == None:
            error = "This is not a valid username."
            user_error_element = "<p class='error'>" + cgi.escape(error, quote=True) + "</p>"
        else:
            username = username
            user_error_element = ""

        password = self.request.get("password")
        if password == "":
            error = "Please enter a password."
            pass_error_element = "<p class='error'>" + cgi.escape(error, quote=True) + "</p>"
        elif valid_password(password) == None:
            error = "This is not a valid password."
            pass_error_element = "<p class='error'>" + cgi.escape(error, quote=True) + "</p>"
        else:
            pass_error_element = ""

        verifypassword = self.request.get("verifypassword")
        if verifypassword == "":
            error = "Please verify your password."
            verify_error_element = "<p class='error'>" + cgi.escape(error, quote=True) + "</p>"
        elif verifypassword == password:
            verify_error_element = ""
        else:
            error = "Your passwords do not match."
            verify_error_element = "<p class='error'>" + cgi.escape(error, quote=True) + "</p>"

        email = self.request.get("email")
        if email == "":
            error = "Please enter your email."
            email_error_element = "<p class='error'>" + cgi.escape(error, quote=True) + "</p>"
        elif valid_email(email) == None:
            error = "This is not a valid email."
            email_error_element = "<p class='error'>" + cgi.escape(error, quote=True) + "</p>"
        else:
            email = email
            email_error_element = ""

        all_elements = user_error_element + pass_error_element + verify_error_element + email_error_element
        if all_elements == "":
            self.redirect("/here")
        else:
            self.response.write(content.format(username, user_error_element, pass_error_element, verify_error_element, email, email_error_element))


class Welcome(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        username = self.request.get("username")
        hello = "Welcome" + username
        self.response.write(hello)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/here', Welcome),
    #('/validate', Validate)
], debug=True)
