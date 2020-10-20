from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'hola mundo'

@app.route('/about')
def about():
    return 'about'

@app.route('/posts')
def posts():
    return 'posts'

@app.route('/post/<int:id>')
def post(id):
    return f'este post {id}'

if __name__ == "__main__":
    app.run(debug=True)
