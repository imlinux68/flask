from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!!! <h1>HELO FROM FLASK!!!</h1>"


@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show profile of current user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # shoe id with data, id - integer num
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    abort(401)
    # 401 access deny message
    this_is_never_executed()

if __name__ == "__main__"
    app.run()
