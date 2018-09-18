## HW 1
## SI 364 F18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment
# AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".

# I worked with Nicole Greenburg

 # - I used the first_flask_app.py from lecture
 # https://www.w3schools.com/html/html_forms.asp
 # http://flask.pocoo.org/docs/1.0/tutorial/templates/



## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications.
## Edit the code so that once you run this application locally and go
## to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask, request
import requests
import json
import html

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
		return 'Hello!'

# new route: /class
@app.route('/class')
def welcometo():
		return 'Welcome to SI 364!'

@app.route('/movie/<movname>')
def movnamefunc(movname):
		baseurl = "https://itunes.apple.com/search"
		params_diction = {}
		params_diction["term"] = movname
		resp = requests.get(baseurl, params=params_diction)
		text = resp.text
		python_obj = json.loads(text)
		return str(python_obj)

@app.route('/question')
def questfunc():
	htmlstring = '''
		<html>
			<body>
				<div>
					<form action = "http://localhost:5000/result" method = "GET">
						Please enter your favorite number: <br> <br>
							<input type= "text" name = "number" value="0">
							 <input type = "submit" value = "Submit">
				<div>
			</form>
		</htm>'''
	return htmlstring

@app.route('/result', methods=["GET","POST"])
def resultfunc():
	if request.method == "GET":
		try:
			n = request.args.get('number', 'not found') # FROM views_app.py
			convertedn = int(n)
			response = "Double your favorite number is "
			final = response + str(2*convertedn)
			return final
		except:
			return "Something appears to be going wrong. Check that you are only entering numbers and try again."




## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>'
# you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille',
# you should see something like the data shown in the included file sample_ratatouille_data.txt,
# which contains data about the animated movie Ratatouille. However, if you go to the url
# http://localhost:5000/movie/titanic, you should get different data, and if you go to the url
# 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question,
# you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that
# says "Double your favorite number is <number>". For example, if you enter 2 into the form, you
# should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.


## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in
# the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

@app.route('/problem4form')
def qFour():
	formstring = """+++++++++++++++++++++++++++++++++++++++++<br>
	<h1>Star Wars People Search</h1>
	+++++++++++++++++++++++++++++++++++++++++<br>
	<br> <br>
	Enter a name to look up: <br>
	<form action="http://localhost:5000/problem4form" method='GET'>
	<input type="text" name="phrase">
	<input type="submit" value="Submit">
	</form> <br>
	How much do you like Star Wars?<br>
	<input type="radio" name="dislike"> I don't like Star Wars at all<br>
	<input type="radio" name="meh"> I feel eh about Star Wars<br>
	<input type="radio" name="kinda"> I kinda like Star Wars<br>
	<input type="radio" name="love"> I love Star Wars<br>
	<br>
	<input type="submit" value="Submit"></form><br>
	"""
	baseurl = "https://swapi.co/api/people/?"
	searchterm = str(request.args.get('phrase'))

	params_diction = {}
	params_diction["search"] = searchterm
	makereq = requests.get(baseurl, params = params_diction)

	txt = makereq.text
	python_obj = json.loads(txt)
	pname = python_obj['results'][0]["name"]
	phair = python_obj['results'][0]["hair_color"]
	pgender = python_obj['results'][0]["gender"]
	pworld = python_obj['results'][0]["homeworld"]

	personstring = '<br>-- TOP PERSON RESULT --<br>Name: {}<br>Hair Color: {}<br>Gender: {}<br>Homeworld (link!): {}'.format(pname, phair, pgender, pworld)

	if request.method == "GET":
		try:
			if request.args.get('dislike'):
				return(formstring + '<br> If you do not like Star Wars, I guess you have no use for this app then! Find another one! <br>')
			if request.args.get('meh'):
				return(formstring + '<br> Show a bit more enthusiasm, please! <br>')
			if request.args.get('kinda'):
				return(formstring + personstring)
			if request.args.get('love'):
				return(formstring + '<br> WHOOO! A STAR WARS FAN!! <br>' + personstring)
			else:
				return(formstring + '<br> you need to select an answer! <br>')
		except:
			return(formstring + '<br> SOMETHING IS GOING WRONG. Make sure you spelled everything correctly.')

	return formstring

	# params_diction = {}
	# params_diction["Accept"] = "application/json"
	# params_diction["app_id"] = "aa397b2c"
	# params_diction["app_key"] = "9a8c2f87bb0e376774a74f1763331be7"
	# print(request.args.get('phrase'))
	# fullurl = baseurl + str(request.args.get('phrase'))
	# print(fullurl)
	# makereq = requests.get(fullurl, params = params_diction)
	# return str(formstring) + str(python_obj)
	# text = makereq.text
	# python_obj = json.loads(text)
	# return formstring + str(python_obj)


if __name__ == '__main__':
		app.run(debug=True)

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends
# upon the data entered into the submission form and is readable by humans
# (more readable than e.g. the data you got in Problem 2 of this HW).
# The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps:
# if you think going slowly and carefully writing out steps for a simpler data transaction,
# like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect
# in your form; you do not need to handle errors or user confusion.
# (e.g. if your form asks for a name, you can assume a user will type a reasonable name;
# if your form asks for a number, you can assume a user will type a reasonable number; if your
# form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.
