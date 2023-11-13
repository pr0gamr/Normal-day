"""
This simple app demonstrates how cards can automatically advance to another
card after a certain amount of time. The auto_advance can either be a string
containing the name of the next card, or a function to call that returns the
name of the next card.
"""
from pypercard import App, Card
import random


def auto_func(app, card):
    """
    Called while transitioning from card 2, to card 3.
    """
    count = app.datastore.setdefault("counter", 0)
    count += 1
    app.datastore["counter"] = count
    return "card3"


# The templates for these cards can be found in pypercard.html.
cards = [
    Card("startcard"),
    Card("intro1"),
    Card("intro2"),
    Card("begin"),
    Card("forest1"),
]


# Create the app while ensuring the counter is reset.
carousel_app = App(
    name="PyperCard carousel", datastore={"counter": 0}, cards=cards
)

#start button
@carousel_app.transition("startcard", "click", "start")
def reset(app, card):
    return "intro1"
#end start

#Intro start
@carousel_app.transition("intro1", "click", "next")
def reset(app, card):
    return "intro2"

@carousel_app.transition("intro2", "click", "next")
def reset(app, card):
    return "begin"
#intro end

#first choices
@carousel_app.transition("begin", "click", "forest")
def reset(app, card):
    return "forest1"

@carousel_app.transition("begin", "click", "inside")
def reset(app, card):
    return "intro1"

@carousel_app.transition("begin", "click", "town")
def reset(app, card):
    return "intro1"
#end of first choices

#forest choices

#end of forest choices

#start card
carousel_app.start("startcard")
