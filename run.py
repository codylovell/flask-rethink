from app import app
from app.views import index
from flask import render_template, url_for, redirect, g, request

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid credintials, Please try again."
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
	app.run(debug = True)
