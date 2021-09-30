import pandas as pd
from sqlalchemy import create_engine
import ftplib 

import sentry_sdk
sentry_sdk.init(
    "https://4963b311c67b4e84812569fcc9224980@o518216.ingest.sentry.io/5627744",
    traces_sample_rate=1.0
)

def downloadTickers():
    server = 'ftp.nasdaqtrader.com'
    directory = 'symboldirectory'
    file1 = 'otherlisted.txt'
    file2 = 'nasdaqlisted.txt'

    ftp = ftplib.FTP(server)
    ftp.login()
    ftp.cwd(directory)

    ftp.retrbinary("RETR {}".format(file1), open(file1, 'wb').write)
    ftp.retrbinary("RETR {}".format(file2), open(file2, 'wb').write)
    ftp.quit()
    
    nasdaqlisted = pd.read_csv('nasdaqlisted.txt', delimiter='|')
    otherlisted = pd.read_csv('otherlisted.txt', delimiter='|')
    
    nasdaqlisted.set_index('Symbol', inplace=True)
    nasdaqlisted = nasdaqlisted[nasdaqlisted.columns[:-6]]
    nasdaqlisted = nasdaqlisted.iloc[:-1]
    
    otherlisted.rename(columns={'NASDAQ Symbol':'Symbol'},inplace=True)
    otherlisted.set_index('Symbol', inplace=True)
    otherlisted.drop(['ACT Symbol'], axis=1, inplace=True)
    otherlisted = otherlisted[otherlisted.columns[:-5]]
    otherlisted = otherlisted.iloc[:-1]    
    
    allTicker = nasdaqlisted.append(otherlisted)
    allTicker.sort_values(by=['Symbol'],ascending=True, inplace=True)
    allTicker['Security Name'] = allTicker['Security Name'].replace(" - Common Stock", "", regex=True)
    allTicker['Security Name'] = allTicker['Security Name'].replace("Common Stock", "", regex=True)
    allTicker.rename(columns={'Security Name':'company'}, inplace=True)
    return allTicker
    
engine = create_engine('sqlite:////home/budik/JYproduction/database.db', echo=True)
sqlite_connection = engine.connect()
company = downloadTickers()
company.to_sql("company", sqlite_connection, if_exists='replace')
sqlite_connection.close()   