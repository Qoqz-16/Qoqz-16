from flask import Flask
import random

app = Flask(__name__)
n = random.randint(0,9)
colors = "orange", "red", "blue", "green", "yellow", "purple"

color = random.choice(colors)

@app.route('/')
def home():
    return("<h1 style='text-align: center'>Higher or Lower?</h1>"
           "<p style = 'text-align: center'>Use the URL bar to guess the number i'm thinking of between 1 and 9!</p>")

def text_format(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        return f"<h1 style='text-align:center; text-color: {color}'><b>{response}</b></h1>"
    return wrapper

@text_format
@app.route("/<int:number>")
def higher_lower(number):
    if number > n:
        return f"{number} is Higher, try again with a lower number."
    if number < n:
        return f"{number} is Lower, guess again with a higher number."
    else:
        return f"{number} is correct!!! Well done, you win!"

if __name__ == "__main__":
    app.run(debug=True)