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

    #all main articles
    all_articles = newsapi.get_everything(sources='bbc-news')


    #fetching all articles of top eadline news
    t_articles = top_headlines['articles']


    #fetching all articles of all news articles
    a_articles = all_articles['articles']


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


    #making a list of contents to store the values on that list
    news_all = []
    desc_all = []
    image_url_all = []
    p_date_all = []
    url_all = []

    #fetch all the contents of articles by looping
    for i in range(len(a_articles)):
        a_article = a_articles[i]

        #appending contents into each list
        news_all.append(a_article['title'])
        desc_all.append(a_article['description'])
        image_url_all.append(a_article['urlToImage'])
        p_date_all.append(a_article['publishedAt'])
        url_all.append(a_article['url'])

        
        #making a zip for finding contents directly and shortly
        contents = zip(news,desc,image_url,p_date,url)
        all = zip(news_all,desc_all,image_url_all,p_date_all,url_all)


    return render_template('index.html', contents=contents,all=all)