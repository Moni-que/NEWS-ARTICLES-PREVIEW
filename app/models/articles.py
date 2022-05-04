from flask import render_template
from newsapi import NewsApiClient
from app import app

class Articles:
    def __init__(self, news_all,desc_all,image_url_all,p_date_all,url_all ):
        self.news_all = news_all
        self.desc_all = desc_all
        self.image_url_all = image_url_all
        self.p_date_all = p_date_all
        self.url_all = url_all

    def a_articles(self):

        news_all = []
        desc_all = []
        image_url_all = []
        p_date_all = []
        url_all = []

        newsapi = NewsApiClient(api_key='0ea4e8f58b09419abc487cf7d995bfc9')
        all_articles = newsapi.get_everything(sources='bbc-news')
        a_articles = all_articles['articles']
    #fetch all the contents of articles by looping
        for i in range(len(a_articles)):
            a_article = a_articles[i]

        #appending contents into each list
            news_all.append(a_article['title'])
            desc_all.append(a_article['description'])
            image_url_all.append(a_article['urlToImage'])
            p_date_all.append(a_article['publishedAt'])
            url_all.append(a_article['url'])

            all = zip(news_all,desc_all,image_url_all,p_date_all,url_all)
        return render_template('index.html', all=all)