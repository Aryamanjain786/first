
df = pd.read_csv('coins.csv')

s = input("enter the symbol of company")
#print(df)
x = df[df['symbols']==s].index.values
x = int(x)
#print(x)
j = df['company'][x]
#print(j)

lmy = j.lower()
#print(lmy)

lmy = lmy.replace(" ","-")
#print(lmy)

link = "http://coinmarketcap.com/currencies/"+ lmy +"/"

#print(link)
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