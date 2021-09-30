import requests
from bs4 import BeautifulSoup
import pandas as pd
import feedparser
from selenium import webdriver
from bs4 import BeautifulSoup

import sentry_sdk
sentry_sdk.init(
    "https://4963b311c67b4e84812569fcc9224980@o518216.ingest.sentry.io/5627744",
    traces_sample_rate=1.0
)

def companyDividends(ticker):
    URLstatistics = 'https://finance.yahoo.com/quote/'+str(ticker)+'/key-statistics?p='+str(ticker)

    dataDividendsSplits = pd.DataFrame (columns = ['fund','value'])
 
    pageStatistics = requests.get(URLstatistics)
    resultsStatistics = BeautifulSoup(pageStatistics.content, 'html.parser')
    tablesStatistics = resultsStatistics.find_all('table')

    if str(resultsStatistics.find_all(id='quote-nav')).find('Statistics') != -1:    
            
        rowsStatistics = tablesStatistics[3].find_all('tr')
        for row in rowsStatistics[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataDividendsSplits = dataDividendsSplits.append(pd. Series(cols, index = dataDividendsSplits.columns), ignore_index = True)
        #dataDividendsSplits = dataDividendsSplits.set_index('fund')
    return (dataDividendsSplits)


def majorHolders(ticker):
    URLholders = 'https://finance.yahoo.com/quote/'+str(ticker)+'/holders?p='+str(ticker)
    pageHolders = requests.get(URLholders)
    resultsHolders = BeautifulSoup(pageHolders.content, 'html.parser')
    tablesHolders = resultsHolders.find_all('table')

    dataMajorHolders = pd.DataFrame (columns = ['pct','holder'])
    dataTopInstitutional = pd.DataFrame (columns = ['holder','shares','date','pct','value'])
    dataTopMutual = pd.DataFrame (columns = ['holder','shares','date','pct','value'])    

    ln = len(tablesHolders)
    if ln >= 1:
        for i in range(0, ln):
            if i == 0:
                rowsHolders = tablesHolders[0].find_all('tr')
                if len(rowsHolders) == 4: 
                    for row in rowsHolders[1:]:
                        cols = row.find_all('td')
                        cols = [ele.text.strip() for ele in cols]
                        dataMajorHolders = dataMajorHolders.append(pd. Series(cols, index = dataMajorHolders.columns), ignore_index = True)

            if i == 1:
                rowsHolders = tablesHolders[1].find_all('tr')
                for row in rowsHolders[1:]:
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    dataTopInstitutional = dataTopInstitutional.append(pd. Series(cols, index = dataTopInstitutional.columns), ignore_index = True)

            if i == 2:
                rowsHolders = tablesHolders[2].find_all('tr')
                for row in rowsHolders[1:]:
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    dataTopMutual = dataTopMutual.append(pd. Series(cols, index = dataTopMutual.columns), ignore_index = True)    

    return (dataMajorHolders, dataTopInstitutional, dataTopMutual)


'''
def majorHolders(ticker):
    URLholders = 'https://finance.yahoo.com/quote/'+str(ticker)+'/holders?p='+str(ticker)
    pageHolders = requests.get(URLholders)
    resultsHolders = BeautifulSoup(pageHolders.content, 'html.parser')
    tablesHolders = resultsHolders.find_all('table')

    dataMajorHolders = pd.DataFrame (columns = ['pct','holder'])
    dataTopInstitutional = pd.DataFrame (columns = ['holder','shares','date','pct','value'])
    dataTopMutual = pd.DataFrame (columns = ['holder','shares','date','pct','value'])    

    rowsHolders = tablesHolders[0].find_all('tr')
    if len(rowsHolders) == 4: 
        for row in rowsHolders[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataMajorHolders = dataMajorHolders.append(pd. Series(cols, index = dataMajorHolders.columns), ignore_index = True)

        
        rowsHolders = tablesHolders[1].find_all('tr')
        for row in rowsHolders[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataTopInstitutional = dataTopInstitutional.append(pd. Series(cols, index = dataTopInstitutional.columns), ignore_index = True)
      
            
        rowsHolders = tablesHolders[2].find_all('tr')
        for row in rowsHolders[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataTopMutual = dataTopMutual.append(pd. Series(cols, index = dataTopMutual.columns), ignore_index = True)    

    return (dataMajorHolders, dataTopInstitutional, dataTopMutual)
'''
def companyRevenues(ticker):
    URLanalysis = 'https://finance.yahoo.com/quote/'+str(ticker)+'/analysis?p='+str(ticker)    
    dataEarningsEstimate = pd.DataFrame (columns = ['fund','qtr1','qtr2','qtr3','qtr4'])
    dataRevenueEstimate = pd.DataFrame (columns = ['fund','qtr1','qtr2','qtr3','qtr4'])

    pageAnalysis = requests.get(URLanalysis)
    resultsAnalysis = BeautifulSoup(pageAnalysis.content, 'html.parser')
    tablesAnalysis = resultsAnalysis.find_all('table')
    
    rowsAnalysis = tablesAnalysis[0].find_all('tr')
    if len(rowsAnalysis) == 6:    
        
        for row in rowsAnalysis[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]        
            dataEarningsEstimate = dataEarningsEstimate.append(pd. Series(cols, index = dataEarningsEstimate.columns), ignore_index = True)
             
        rowsAnalysis = tablesAnalysis[1].find_all('tr')
        for row in rowsAnalysis[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataRevenueEstimate = dataRevenueEstimate.append(pd. Series(cols, index = dataRevenueEstimate.columns), ignore_index = True)
        
    return (dataEarningsEstimate, dataRevenueEstimate)
            
'''
def fundamentals(ticker):
    URLstatistics = 'https://finance.yahoo.com/quote/'+str(ticker)+'/key-statistics?p='+str(ticker)
    URLprofile = 'https://finance.yahoo.com/quote/'+str(ticker)+'/profile?p='+str(ticker)
    URLanalysis = 'https://finance.yahoo.com/quote/'+str(ticker)+'/analysis?p='+str(ticker)
    URLholders = 'https://finance.yahoo.com/quote/'+str(ticker)+'/holders?p='+str(ticker)

    dataShareStatistics = pd.DataFrame (columns = ['fund','value'])
    dataDividendsSplits = pd.DataFrame (columns = ['fund','value'])
    dataKeyExecutives = pd.DataFrame (columns = ['name','position','pay','excercised','born'])
    dataDescription = []
    dataEarningsEstimate = pd.DataFrame (columns = ['fund','qtr1','qtr2','qtr3','qtr4'])
    dataRevenueEstimate = pd.DataFrame (columns = ['fund','qtr1','qtr2','qtr3','qtr4'])
    dataMajorHolders = pd.DataFrame (columns = ['pct','holder'])
    dataTopInstitutional = pd.DataFrame (columns = ['holder','shares','date','pct','value'])
    dataTopMutual = pd.DataFrame (columns = ['holder','shares','date','pct','value'])

    pageStatistics = requests.get(URLstatistics)
    resultsStatistics = BeautifulSoup(pageStatistics.content, 'html.parser')
    tablesStatistics = resultsStatistics.find_all('table')

    pageProfile = requests.get(URLprofile)
    resultsProfile = BeautifulSoup(pageProfile.content, 'html.parser')
    tablesProfile = resultsProfile.find_all('table')

    pageAnalysis = requests.get(URLanalysis)
    resultsAnalysis = BeautifulSoup(pageAnalysis.content, 'html.parser')
    tablesAnalysis = resultsAnalysis.find_all('table')

    pageHolders = requests.get(URLholders)
    resultsHolders = BeautifulSoup(pageHolders.content, 'html.parser')
    tablesHolders = resultsHolders.find_all('table')

    if str(resultsStatistics.find_all(id='quote-nav')).find('Statistics') != -1:    
        rowsStatistics = tablesStatistics[2].find_all('tr')
        for row in rowsStatistics[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataShareStatistics = dataShareStatistics.append(pd. Series(cols, index = dataShareStatistics.columns), ignore_index = True)
        #dataShareStatistics = dataShareStatistics.set_index('fund')
            
        rowsStatistics = tablesStatistics[3].find_all('tr')
        for row in rowsStatistics[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataDividendsSplits = dataDividendsSplits.append(pd. Series(cols, index = dataDividendsSplits.columns), ignore_index = True)
        #dataDividendsSplits = dataDividendsSplits.set_index('fund')
        
        rowsProfile = tablesProfile[0].find_all('tr')
        for row in rowsProfile[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataKeyExecutives = dataKeyExecutives.append(pd. Series(cols, index = dataKeyExecutives.columns), ignore_index = True)
        #dataKeyExecutives = dataKeyExecutives.set_index('name')
            
        dataDescription = resultsProfile.find_all('p')[2].text

   
        rowsAnalysis = tablesAnalysis[0].find_all('tr')
        for row in rowsAnalysis[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]        
            dataEarningsEstimate = dataEarningsEstimate.append(pd. Series(cols, index = dataEarningsEstimate.columns), ignore_index = True)
        #dataEarningsEstimate = dataEarningsEstimate.set_index('fund')        
            
        rowsAnalysis = tablesAnalysis[1].find_all('tr')
        for row in rowsAnalysis[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataRevenueEstimate = dataRevenueEstimate.append(pd. Series(cols, index = dataRevenueEstimate.columns), ignore_index = True)
        #dataRevenueEstimate = dataRevenueEstimate.set_index('fund')   
            
        rowsHolders = tablesHolders[0].find_all('tr')
        for row in rowsHolders[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataMajorHolders = dataMajorHolders.append(pd. Series(cols, index = dataMajorHolders.columns), ignore_index = True)
        #dataMajorHolders = dataMajorHolders.set_index('pct')   
        
        rowsHolders = tablesHolders[1].find_all('tr')
        for row in rowsHolders[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataTopInstitutional = dataTopInstitutional.append(pd. Series(cols, index = dataTopInstitutional.columns), ignore_index = True)
        #dataTopInstitutional = dataTopInstitutional.set_index('holder')           
            
        rowsHolders = tablesHolders[2].find_all('tr')
        for row in rowsHolders[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            dataTopMutual = dataTopMutual.append(pd. Series(cols, index = dataTopMutual.columns), ignore_index = True)    
        #dataTopMutual = dataTopMutual.set_index('holder')   


    #chartmill news feed
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(str('https://www.chartmill.com/stock/quote/')+str(ticker)+str('/news'))
    
    driver.refresh()
    driver.implicitly_wait(5)

    feeddfChartmill = pd.DataFrame(columns=['Title','Link','Img'])

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    result = soup.find_all('div',{'class','elem ng-star-inserted'})
    
    for res in result:
        resText = res.find('p')
        resImg = res.find('img')

        if resText != None:
            title = res.find('p').getText()
        else:
            title = res.find_all('a', href=True)[0].getText()
    
        link = str('https://www.chartmill.com') + str(res.find_all('a', href=True)[0]['href'])

        if "http" in resImg['src']:
            img = resImg['src']
        else:
            img = str('https://www.chartmill.com/') + resImg['src']

        feeddfChartmill = feeddfChartmill.append({"Title": title,"Link": link,"Img": img},ignore_index=True)

    #return (dataShareStatistics, dataDividendsSplits, dataKeyExecutives, dataDescription, dataEarningsEstimate, dataRevenueEstimate, dataMajorHolders, dataTopInstitutional, dataTopMutual, feeddfChartmill)
    return (dataShareStatistics, dataDividendsSplits, dataKeyExecutives, dataDescription, dataEarningsEstimate, dataRevenueEstimate, dataMajorHolders, dataTopInstitutional, dataTopMutual)
'''