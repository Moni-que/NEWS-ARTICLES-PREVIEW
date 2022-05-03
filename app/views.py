from flask import render_template
from pip import main
from app import app
from newsapi import NewsApiClient

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    newsapi = NewsApiClient(api_key='0ea4e8f58b09419abc487cf7d995bfc9')

    #top headline news
    top_headlines = newsapi.get_top_headlines(sources='bbc-news')


    #fetching all articles of top eadline news
    t_articles = top_headlines['articles']



    return render_template('index.html')