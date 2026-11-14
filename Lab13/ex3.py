# Create a simple HTML Flask application that displays a meme from https://meme-api.com/gimme/wholesomememes
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://meme-api.com/gimme/wholesomememes"
    response = requests.request("GET", url, timeout=10)
    response.raise_for_status()
    meme = response.json()
    return render_template(
        'index1.html',
        meme_url=meme['url'],
        subreddit=meme['subreddit'],
    )

if __name__ == '__main__':
    app.run(debug=True)