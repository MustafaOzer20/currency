from bs4 import BeautifulSoup
import requests

def currency():
        url = "https://www.doviz.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        cur_name = soup.find_all("span",{"class":"name"})
        cur_val = soup.find_all("span",{"class":"value"})
        currencyList = list()
        for name,value in zip(cur_name, cur_val):
            if(name.text == "DOLAR"):
                dolar = (name.text,value.text)
                currencyList.append(dolar)
            elif(name.text=="EURO"):
                euro = (name.text,value.text)
                currencyList.append(euro)
            elif (name.text == "GRAM ALTIN"):
                gold = (name.text, value.text)
                currencyList.append(gold)
            elif (name.text == "STERLİN"):
                sterlin = (name.text, value.text)
                currencyList.append(sterlin)
                break
        return currencyList