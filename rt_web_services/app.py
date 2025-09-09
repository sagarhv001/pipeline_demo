from flask import Flask, render_template_string, Blueprint, request
import requests
from requests.exceptions import JSONDecodeError
app = Flask(__name__)



login_form = '''
<!doctype html>
    <html>
    <head><title>Login page</title></head>
    <body>
	<h2>Login page</h2>
	<form method="post">
		Username: <input type="text" name="username"><br>
		Password: <input type="password" name="password"><br>
		<input type="submit" value="Login">
	</form>
	{% if message %}<p>{{ message }}</p>{% endif %}
</body>
</html>
'''

register_form = '''
    <!doctype html>
	<html>
	<head><title>Register page</title>
	</head>
	<body>
	<h2>Register page</h2>
	<form method="post" action="">
	Username: <input type="text" name="username"><br>
	Password: <input type="password" name="password"><br>
	<input type="submit" value="Register">
	</form>
	{%if message %}<p>{{message}}</p>{% endif %}
	</body>
	</html>
'''


@app.route('/new_user', methods=['GET', 'POST'])
def user():
    message = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        try:
            req = requests.post('http://backend:5000/new_user', json={"username": username, "password": password})
            try:
                data = req.json()
            except Exception:
                message = f"Invalid response: {req.text}"
                return render_template_string(register_form, message=message)
            if data.get('success'):
                message = 'Registered Successfully!'
            else:
                message = 'Could not Enter data!'
        except Exception as e:
            message = f'Error: {e}'
    return render_template_string(register_form, message=message)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            resp = requests.post('http://backend:5000/user', json={"username": username, "password": password})
            try:
                data = resp.json()
            except Exception:
                message = f"Invalid response: {resp.text}"
                return render_template_string(login_form, message=message)
            if data.get('success'):
                message = 'Login successful!'
            else:
                message = 'Invalid credentials.'
        except Exception as e:
            message = f'Error: {e}'
    return render_template_string(login_form, message=message)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=3000)
