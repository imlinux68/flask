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

if __name__ == "__main__"
    app.run()
