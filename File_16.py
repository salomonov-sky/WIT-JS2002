for cyfry in range(10):
    print(cyfry)



for liczby in range(10,21):
    print(liczby)



for liczby in range(3, 23, 4):
    print(liczby)



i = 0
while i < 10:
    print(i)
    i = i + 1



i = 10
while i < 21:
    print(i)
    i = i + 1



i = 3
while i < 20:
    print(i)
    i = i + 4



for i in "Warszawa":
    print(i)

miasto = "Warszawa"
i = 0
while i<len(miasto):
    print(miasto[i])
    i+=1



for i in range (10):
    for i in range (0,6):
        print(i)



username="Admin"
password="1234"

authenticated=False
while not authenticated:
    _username_=input("Enter username: ")
    _password_=input("Enter password: ")
    if username == _username_ and password == _password_:
        authenticated = True



a = 24
b = 36
x=0
nww =(x/a, x/b)
while (True)   :
    x +=1
    if x %a==0 and x %b==0:
        print(x)
        print ("Wynik dzielenia x/a, x/b")
        print (nww)
        break



wiek=int(input("Podaj swój wiek: "))
if wiek > 18 or wiek == 18:
    print("Jesteś pełnoletni")
else:
    print("Nie masz ukończonych 18 lat")



wiek=int(input("Podaj swój wiek: "))
if wiek > 18:
        print("Możesz prowadzić samochód oraz głosować w wyborach")
elif  16 < wiek > 18:
        print("Możesz prowadzić samochód")
else:
        print("Nie możesz prowadzić samochodu i głosować w wyborach")



inf = float(input("Podaj średnią prędkość pojazdu: "))
droga = 250
czas = 2.75
srednia_predkosc = droga/czas
if inf > srednia_predkosc:
    print("Twój samochód dojedzie szybciej niż pociąg")
elif inf == srednia_predkosc:
    print("Twój samochód dojedzie z taką samą prędkością jak pociąg")
else:
        print("Twój samochód dojedzie wolniej niż pociąg")



kapital_poczatkowy = float(input("Podaj swój kapitał początkowy: "))
okres_inwest_w_m = float(input("Podaj okres inwestowania w miesiącach: "))
pozadana_koncowa_wart_inwest = float(input("Podaj pożądaną, końcową wartość inwestycji: "))
ilosc_pieniedzy_po_upl_pod_l_mies = ((kapital_poczatkowy*(1 + 0.02)**okres_inwest_w_m))
if ilosc_pieniedzy_po_upl_pod_l_mies > pozadana_koncowa_wart_inwest:
    print ("Ilośc pieniędzy po upływie podanej liczby miesięcy jest większa niż pożądana wartość inwestycji")
    print(ilosc_pieniedzy_po_upl_pod_l_mies)
else:
    print("Ilośc pieniędzy po upływie podanej liczby miesięcy jest mniejsza niż pożądana wartość inwestycji")
    print(ilosc_pieniedzy_po_upl_pod_l_mies)


       

