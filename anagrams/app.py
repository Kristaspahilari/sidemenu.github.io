from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/wordss")
def wordss():
    f = open('words.txt')
    wordss = f.read().splitlines()
    return render_template('words.html', word_list=wordss)

@app.route("/words/<word>")
def words(word):
    f = open('words.txt')
    wordss = f.read().splitlines()

    words = []
    
    for w in wordss:
        if sorted(word.upper()) == sorted(w):
            words.append(w)
               
    return render_template('words.html', word_list=words)

