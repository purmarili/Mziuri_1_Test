from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_main():
    return '<h1>Welcome to our Flask application</h1>'


@app.route('/<username>')
def get_user(username):
    return f'<h1>Hello {username}</h1>'


if __name__ == '__main__':
    app.run(host='127.0.0.2', port=5005)

