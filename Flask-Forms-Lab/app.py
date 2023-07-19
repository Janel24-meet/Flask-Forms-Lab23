from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

accounts = {"jan": "jej", "siwarha": "123", "majd": "majaj", "sergey": "ytcff", "Daniel": "5523"}
username = "siwarha"
password = "123"
facebook_friends=["Jan", "Daniel", "Majd", "Shams", "Nour", "Ghadir", "Sam", "Celine", "Jihad"]


@app.route('/', methods=['GET', 'POST']) # '/' for the default page 
def login():

	if request.method == 'GET':
		return render_template('login.html')
	else: 
		name = request.form['username']
		passw = request.form['password']

		if (name in accounts and accounts[name]==passw):
		  return redirect(url_for('home'))
		else:
		  return render_template('login.html')

@app.route('/home')  
def home():
	return render_template('home.html', friend=facebook_friends)

@app.route('/friend_exists/<string:name>')
def exist(name):
	return render_template('friend_exists.html', status = name in facebook_friends)
 				
  	  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
