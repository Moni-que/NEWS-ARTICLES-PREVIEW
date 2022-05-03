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

    #making a list of contents to store the values on that list
    news = []
    desc = []
    image_url = []
    p_date = []
    url = []

    #fetch all the contents of articles by looping
    for i in range(len(t_articles)):
        main_articles = t_articles[i]

        #appending contents into each list
        news.append(main_articles['title'])
        desc.append(main_articles['description'])
        image_url.append(main_articles['urlToImage'])
        p_date.append(main_articles['publishedAt'])
        url.append(main_articles['url'])



    return render_template('index.html')