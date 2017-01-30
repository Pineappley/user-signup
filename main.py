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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Signup</h1>"
        screenname_form = """
            <form>
                <label>
                    Username
                    <input type="text" name="username"/>
                </label>
            </form>
            """
        password_form = """
            <form>
                <label>
                    Password
                    <input type="password" name="password"/>
                </label>
            </form>
            """
        verify_passform = """
            <form>
                <label>
                    Verify Password
                    <input type="password" name="password"/>
                </label>
            </form>
            """
        email_form = """
            <form>
                <label>
                    Email
                    <input type="text" name="email"/>
                </label>
            </form>
        """
        sub_button = """
            <input type="submit" value="Submit"/>
            """
    

        allforms = screenname_form + password_form + verify_passform + email_form
        self.response.write(header + allforms + sub_button)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
