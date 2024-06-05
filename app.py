from flask import Flask, render_template
import feedparser

app = Flask(__name__)

def get_bbc_news(rss_url):
    feed = feedparser.parse(rss_url)
    return feed.entries

@app.route('/')
def home():
    rss_url = "http://feeds.bbci.co.uk/news/rss.xml"
    news_entries = get_bbc_news(rss_url)
    return render_template('home.html', news=news_entries)

if __name__ == '__main__':
    app.run(debug=True)
