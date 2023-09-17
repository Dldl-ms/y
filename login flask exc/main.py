from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/static')

# Dummy user data for demonstration purposes.
# In a real application, you should use a database to store user information.
users = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'}
]

@app.route('/')
def home():
    return 'Welcome to the login page. <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        enetred = request.form['email']
        password = request.form['password']

        # Check if the username and password are valid.
        for user in users:
            if user['username'] == username and user['password'] == password:
                return f'Hello, {username}! You are logged in.'

        # If the credentials are not valid, display an error message.
        error = 'Invalid credentials. Please try again.'
        return render_template('index.html', error=error)

    # If the request method is GET, render the login form.
    return render_template('index.html', error='')

if __name__ == '__main__':
    app.run(debug=True)
'╔═╦╗╔╦╗╔═╦═╦╦╦╦╗╔═╗'
'║╚╣║║║╚╣╚╣╔╣╔╣║╚╣═╣'
'╠╗║╚╝║║╠╗║╚╣║║║║║═╣'
'╚═╩══╩═╩═╩═╩╝╚╩═╩═╝'