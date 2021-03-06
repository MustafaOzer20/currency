from screen import window
from datetime import datetime
from data import currency

try:
    myList = currency()

    #print(myList) [('GRAM ALTIN', '411,42'), ('DOLAR', '7,5345'), ('EURO', '8,9835'), ('STERLİN', '10,4404')]

    gold_value = myList[0][1]
    dolar_value = myList[1][1]
    euro_value = myList[2][1]
    sterlin_value = myList[3][1]

    now = datetime.now()
    control=1

except:
    control=0


window(control, now, gold_value, dolar_value, euro_value, sterlin_value)
