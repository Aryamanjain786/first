import requests
from bs4 import BeautifulSoup
from csv import writer

with open('coint.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['s.no','company','symbols','url']
    csv_writer.writerow(headers)

    url = "https://coinmarketcap.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    count = 0
    while(count < 10):
    
     # subs = soup.find(class_= 'sc-1eb5slv-0 etpvrL').get_text()
      #print(subs)

      div = soup.find(class_= 'sc-1eb5slv-0 iJjGCS')
      subject = soup.find(class_= 'sc-1eb5slv-0 iJjGCS').get_text()
     # print(subject)

      sub = soup.find(class_= 'sc-1eb5slv-0 gGIpIK coin-item-symbol').get_text()
      #print(sub)
  

      ok = "coinmarketcap.com/currencies/"+subject+"/"
     # print(ok)

      csv_writer.writerow([count,subject,ok])
      count += 1