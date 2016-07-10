from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Python Flask!'

@app.route('/yolo')
def yolo():
    return '<h2> You Only Live Once!</h2>'

@app.route('/profile/<username>')
def profile(username):
    return '<h3>Hey there %s' % username

@app.route('/phone/<int:number>')
def phone(number):
    return '<h3>Your Phone number is: %d' % number


if __name__ == '__main__':
    app.run(debug=True)

    












