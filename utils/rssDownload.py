import pandas as pd
import feedparser
from datetime import datetime
from sqlalchemy import create_engine

import sentry_sdk
sentry_sdk.init(
    "https://4963b311c67b4e84812569fcc9224980@o518216.ingest.sentry.io/5627744",
    traces_sample_rate=1.0
)

def stockNews(ticker):
    url = 'https://www.nasdaq.com/feed/rssoutbound?symbol='+ticker
    maxNews = 30

    allNews = pd.DataFrame(columns=['source','published','title','link','description'])

    feed = feedparser.parse(url)
    for news in feed.entries[0:maxNews]:
        published = datetime.strptime(news.published[0:-6], "%a, %d %b %Y %H:%M:%S")
        published = published.strftime("%d %b, %H:%M")                
        allNews = allNews.append({"source": "nasdaq", "description": news.description, "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)

    allNews.sort_values(by=['source', 'published'],ascending=False, inplace=True)
    allNews.set_index('source',inplace=True)
    return allNews

def marketNews():
    bbc = ['http://feeds.bbci.co.uk/news/business/rss.xml#']
    investing = ['https://www.investing.com/rss/news_25.rss']
    nasdaq = ['https://www.nasdaq.com/feed/rssoutbound?category=Stocks']
    marketwatch = ['http://feeds.marketwatch.com/marketwatch/marketpulse/']
    wallstreetjournal = ['https://feeds.a.dj.com/rss/RSSMarketsMain.xml']
    nytimes = ['https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml']

    maxNews = 20

    allNews = pd.DataFrame(columns=['source','published','title','link'])

    for url in bbc:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published, "%a, %d %b %Y %H:%M:%S %Z")
            published = published.strftime("%d %b, %H:%M")            
            allNews = allNews.append({"source": "bbc", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)

    for url in investing:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published, "%Y-%m-%d %H:%M:%S")
            published = published.strftime("%d %b, %H:%M")              
            allNews = allNews.append({"source": "investing", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)
            
    for url in nasdaq:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published[0:-6], "%a, %d %b %Y %H:%M:%S")
            published = published.strftime("%d %b, %H:%M")               
            allNews = allNews.append({"source": "nasdaq", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)

    for url in marketwatch:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published, "%a, %d %b %Y %H:%M:%S %Z")
            published = published.strftime("%d %b, %H:%M")               
            allNews = allNews.append({"source": "marketwatch", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)

    for url in wallstreetjournal:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published[0:-6], "%a, %d %b %Y %H:%M:%S")
            published = published.strftime("%d %b, %H:%M")               
            allNews = allNews.append({"source": "wallstreetjournal", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)
            
    for url in nytimes:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published[0:-6], "%a, %d %b %Y %H:%M:%S")
            published = published.strftime("%d %b, %H:%M")               
            allNews = allNews.append({"source": "nytimes", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)
    
    allNews.sort_values(by=['source', 'published'],ascending=False, inplace=True)
    allNews.set_index('source',inplace=True)
    #allNews.to_csv('../files/marketnews.csv',sep=';')
    return (allNews)

def worldNews():
    bbc = ['http://feeds.bbci.co.uk/news/world/rss.xml']
    investing = ['https://www.investing.com/rss/news_287.rss']
    nasdaq = ['https://www.nasdaq.com/feed/rssoutbound?category=Nasdaq']
    marketwatch = ['http://feeds.marketwatch.com/marketwatch/bulletins']
    wallstreetjournal = ['https://feeds.a.dj.com/rss/RSSWorldNews.xml']
    nytimes = ['https://rss.nytimes.com/services/xml/rss/nyt/World.xml']
    yahoo = ['https://finance.yahoo.com/news/rss']
    google = ['https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en']
    maxNews = 20

    allNews = pd.DataFrame(columns=['source','published','title','link'])

    for url in bbc:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published, "%a, %d %b %Y %H:%M:%S %Z")
            published = published.strftime("%d %b, %H:%M")            
            allNews = allNews.append({"source": "bbc", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)

    for url in investing:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published, "%Y-%m-%d %H:%M:%S")
            published = published.strftime("%d %b, %H:%M")               
            allNews = allNews.append({"source": "investing", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)
            
    for url in nasdaq:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published[0:-6], "%a, %d %b %Y %H:%M:%S")
            published = published.strftime("%d %b, %H:%M")                
            allNews = allNews.append({"source": "nasdaq", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)

    for url in marketwatch:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published, "%a, %d %b %Y %H:%M:%S %Z")
            published = published.strftime("%d %b, %H:%M")               
            allNews = allNews.append({"source": "marketwatch", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)

    for url in wallstreetjournal:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published[0:-6], "%a, %d %b %Y %H:%M:%S")
            published = published.strftime("%d %b, %H:%M")               
            allNews = allNews.append({"source": "wallstreetjournal", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)
            
    for url in nytimes:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published[:-6], "%a, %d %b %Y %H:%M:%S")
            published = published.strftime("%d %b, %H:%M")               
            allNews = allNews.append({"source": "nytimes", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)

    for url in yahoo:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published[:-1].replace('T',' '), "%Y-%m-%d %H:%M:%S")
            published = published.strftime("%d %b, %H:%M")              
            allNews = allNews.append({"source": "yahoo", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)
                
    for url in google:
        feed = feedparser.parse(url)
        for news in feed.entries[0:maxNews]:
            published = datetime.strptime(news.published, "%a, %d %b %Y %H:%M:%S %Z")
            published = published.strftime("%d %b, %H:%M")   
            allNews = allNews.append({"source": "google", "published": published,"title": news.title.replace(";", ","),"link": news.link},ignore_index=True)
            
    allNews.sort_values(by=['source', 'published'],ascending=False, inplace=True)
    allNews.set_index('source',inplace=True)
    #allNews.to_csv('../files/worldnews.csv',sep=';')
    return (allNews)

if __name__ == "__main__":
    #engine = create_engine('sqlite:///../database.db', echo=True)
    engine = create_engine('sqlite:////home/budik/JYproduction/database.db', echo=True)
    #engine = create_engine('sqlite:////home/jan/JYproduction/database.db', echo=True)
    sqlite_connection = engine.connect()
    marketnews = marketNews()
    worldnews = worldNews()
    marketnews.to_sql("marketnews", sqlite_connection, if_exists='replace')
    worldnews.to_sql("worldnews", sqlite_connection, if_exists='replace')
    sqlite_connection.close()
