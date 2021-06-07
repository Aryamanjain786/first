import requests
from bs4 import BeautifulSoup
from csv import writer
import pandas as pd

url = "https://coinmarketcap.com/coins/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')


get_coins()

def get_coins():


 with open('coins.csv','w') as csv_file:
     csv_writer = writer(csv_file)
     headers = ['s.no','company','symbols','url']
     csv_writer.writerow(headers)

     div = soup.find('tbody')

     count = 0
     while(count < 50):
      link = div.find_all('p')[(7*count)+0]
      sno = link.get_text()
    #   print(sno)
 
      link = div.find_all('p')[(7*count)+1]
      sub = link.get_text()
    #   print(sub)

      link = div.find_all('p')[(7*count)+2]
      sym = link.get_text()
    #   print(sym)
      lsub = sub.lower()
      lsub = lsub.replace(" ","-")
      ur = "coinmarketcap.com/currencies/"+ lsub +"/"
    #   print(ur)

      csv_writer.writerow([sno,sub,sym,ur])
      count += 1


    
coin_symbol = input("")

get_coin_data(coin_symbol)


def get_coin_data(coin_symbol):
  
  df = pd.read_csv('coins.csv')

  x = df[df['symbols']==coin_symbol].index.values
  x = int(x)

  j = df['company'][x]

  lmy = j.lower()

  lmy = lmy.replace(" ","-")

  link = "http://coinmarketcap.com/currencies/"+ lmy +"/"

  res = requests.get(link)
  soup = BeautifulSoup(res.text,'html.parser')

  ak = soup.find(class_='nameSymbol___1arQV').get_text()
  print(ak)

  print(j)

  div = soup.find(class_='sc-16r8icm-0 cCqhlo')
  lap = div.find_all('div')[2]
  ak = lap.get_text()
  print(ak)

  print(link)

  ak = soup.find(class_='sc-16r8icm-0 dPtrpY').get_text()
  print(ak)

  ak = soup.find(class_='priceValue___11gHJ').get_text()
  print(ak)

  div = soup.find('tbody')
  aks = div.find_all('td')[4]
  ak = aks.get_text()
  print(ak)

  aks = div.find_all('td')[5]
  ak = aks.get_text()
  print(ak)

  aks = div.find_all('td')[6]
  ak = aks.get_text()
  print(ak)

  ak = soup.find(class_='statsItemRight___yJ5i-').get_text()
  print(ak)

  ak = soup.find("h2", {"id" : "what-is-ethereum-eth"}).get_text()
  print(ak)

  div = soup.find(class_='sc-1lt0cju-0 srvSa')
  aks = div.find_all('p')[0]
  ak = aks.get_text()
  print(ak)

  div = soup.find(class_='sc-1lt0cju-0 srvSa')
  aks = div.find_all('p')[1]
  ak = aks.get_text()
  print(ak)

  div = soup.find(class_='sc-1lt0cju-0 srvSa')
  aks = div.find_all('p')[2]
  ak = aks.get_text()
  print(ak)
