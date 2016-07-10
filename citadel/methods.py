from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Method is %s ' % request.method

@app.route('/chicken', methods=['GET', 'POST'])
def chicken():
    if request.method == 'POST':
        return 'User is on POST Method'
    else:
        return 'User is on GET Method'



if __name__ == '__main__':
    app.run(debug=True)