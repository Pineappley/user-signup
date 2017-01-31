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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = """
        <h1>Signup</h1>
        <form method = 'post'>
            <label>Username: <input name="username" /> </label>
            <label>Password: <input type="password" name="password"/></label>
            <label>Verify Password: <input type="password" name="password"/></label>
            <label>Email: <input type="text" name="email"/> </label>
        <input type="submit" name="Submit"/>
        </form>
            """
        self.response.write(header)


    def post(self):
        header = """
        <h1>Signup</h1>
        <form method = 'post'>
            <label>Username: <input name="username" /> </label></br>
            <label>Password: <input type="password" name="password"/></label></br>
            <label>Verify Password: <input type="password" name="password"/></label></br>
            <label>Email: <input type="text" name="email"/> </label></br>
        <input type="submit" name="Submit"/>
        </form>
            """
        username = self.request.get("username")
        if valid_username(username) == None:
            error = "This is not a valid username."
            error_element = "<p class='error'>" + cgi.escape(error, quote=True) + "</p>"
            self.response.write(header + error_element)
        else:
            self.redirect("/here")



        # username = self.request.get("username")
        # for i in username:
        #     if i == " ":
        #         error = "Please enter a valid username"
        #         error_escaped = cgi.escape(error, quote=True)
        #         # redirect to homepage, and include error as a query parameter in the URL
        #         self.redirect("/?error=" + error_escaped)

class Welcome(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to my temporary success celebration page!")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    #('/validate', Validate)
], debug=True)
