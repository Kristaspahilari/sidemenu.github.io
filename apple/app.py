from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Apple"
    picture = "/static/first.png"
    text = """While walking home from school you meet an old lady who offers you an apple."""

    choices = [
        ('accept',"You accept the apple."),
        ('reject',"You say you are allergic to apples.")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices, picture=picture)



@app.route("/accept")
def accept():
    title = "She gives you the apple.."
    picture = "/static/second.jpg"
    text = """... This is the sweetest apple you've ever eaten in your whole life. """

    choices = [
        ('keepeating',"You keep eating the apple."),
        ('reject',"You stop eating the apple.")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices, picture=picture)

@app.route("/reject")
def reject():
    title = "You reject the apple!"
    text = """You keep walking home like every other day."""
    picture = "/static/forth.png"
    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices,  picture=picture)



@app.route("/keepeating")
def keepeating():
    title = "You keep eating the apple."
    picture = "/static/third.png"
    text = """The apple is poisonous. You turn into a worm. Now you will live a life with no worries inside an apple! :)"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, picture=picture)