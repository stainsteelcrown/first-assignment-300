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

def escape_html(s):
    return cgi.escape(s, quote = True)

form="""
<form method="post">
    What is your birthday?
    <br>
    <label> Month
        <input type="text" name="month"> 
    </label>

    <label> Day
        <input type="text" name="day">
    </label>
    
    <label> Year
        <input type="text" name="year">
    </label>
    <div style="color: red">%(error)s</div>    
    <br>
    <br>
    <input type="submit">
</form>
"""

months = ['January', 'February','March','April','May','June','July',
 'August','September','October','November','December']

def valid_month(month):
    if month:
        month = month.capitalize()
    if(month in month):
        return month

def valid_day(day):
    try:
        d = int(day)
        if 1 <= d <= 31:
            return d
    except ValueError:
            pass
    return None

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
    if year > 1900 and year < 2020:
        return year


class MainHandler(webapp2.RequestHandler):
    def write_form(self, error=""):
        self.response.out.write(form % {"error": error})

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')
        
        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not(month and day and year)
            self.write_form("That doesn't look valid to me, friend.")
        else:
            self.response.out.write("Thanks!  That's a totally valid day!")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
