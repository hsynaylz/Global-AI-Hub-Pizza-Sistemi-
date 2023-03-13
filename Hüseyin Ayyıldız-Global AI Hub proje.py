# Hüseyin Ayyıldız 
# Global AI Hub  proje 
# hsyncuce@gmail.com

import datetime
import csv
dosya=open("Menu.txt","w",encoding="utf-8")
dosya.write("Lütfen Bir Pizza Tabanı Seçiniz:\n"
           "Klasik\n"
           "Margaritan\n"
           "TürkPizza\n"
           "Sade Pizza\n"
           "* ve seçeceğiniz sos:\n"
           "Zeytin\n"
           "Mantarlar\n"
           "Keçi Peyniri\n"
           "Et\n"
           "Soğan\n"
           "Mısır\n"
           "Teşekkür ederiz!\n")

dosya= open("Menu.txt", "r",encoding="utf-8")


liste=dosya.readlines()
pizza_türleri=liste[1:5]
pizza_sosları=liste[6:12]



pizza_türleri_fiyat= {
    "Klasik\n": 105,
    "Margaritan\n": 107,
    "TürkPizza\n": 110,
    "Sade Pizza\n":100 
}

class Pizza():
    def __init__(self, cesit):
        self.cesit = cesit

    def set_cesit(self, cesit):
        self.cesit = cesit

    def get_cesit(self):
        return self.cesit()

    def get_fiyat(self):
        return pizza_türleri_fiyat[self.cesit]



class Siparis():
    def __init__(self):
        self.pizzas = []

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getTotal(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.get_fiyat()
        return total

# start processing the order
Siparis = Siparis()


def run():
    print("\nHangi pizzayı almak istersiniz?(numarasını giriniz)\n\n\
    _____________________________________________________________\n\
    | 1:Klasik  | 2:Margarita |  3: TürkPizza  |  4: Sade Pizza |\n\
    |    105₺   |     107₺    |        110₺    |      100₺      |\n\
    |___________|_____________|________________|________________|\n\
    \n- Pizza tercihinizi yaptıysanız (a) tuşuna giriniz\n")

    while True:
        try:
            
            response = input('-')

            if response == 'a':
                break

            secilen_pizza = int(response)-1

            secilen_pizza = pizza_türleri[secilen_pizza]
            
            print(f"Pizza: {secilen_pizza}")
            Siparis.addPizza(Pizza(secilen_pizza))
        except:
            print("Bir hata oluştu,Tekrar deneyiniz")
run()

print("your current order total: ", "₺" + str(Siparis.getTotal()))



pizza_sosları_fiyatları = {
                         'Zeytin\n': 5, 
                          'Mantarlar\n': 7, 
                         'Keçi Peyniri\n':9, 
                           'Et\n': 15, 
                         'Soğan\n':10, 
                          'Mısır\n' : 6, 
                        }



class Soslar():
    """ Have customer pick toppings for pizza"""
    
    def __init__(self, numToppings):
        self.numToppings = numToppings

    def set_toppings(self, numToppings):
        self.numToppings = numToppings

    def get_toppings(self):
        return pizza_sosları_fiyatları[self.numToppings]


class SosSiparişi():

    def __init__(self):
        self.topping = []

    def addTopping(self, toppings): 
        self.topping.append(toppings)

    def toppingTotal(self):
        get_topping_total = 0
        for toppings in self.topping:
            get_topping_total += toppings.get_toppings()
        return get_topping_total

# Strat processing the order
topping_order = SosSiparişi()

def runTopping():
    print("\nPizzanızın üzerine hangi sosları koymak istersiniz?(numarasını giriniz)\n\n\
    ________________________________________________\n\
    | 1: Zeytin |  2: Mantarlar  | 3: Keçi Peyniri | \n\
    |   4: Et   |    5: Soğan    |    6: Mısır     | \n\
    |___________|________________|_________________|\n\
    Sos tercihinizi yaptısanız (s) tuşunu giriniz:z \n")

    while True:
        try: 
            response = input('-')
            if response == 's':
                break
            Secilen_soslar = int(response)-1

            Secilen_soslar = pizza_sosları[Secilen_soslar]

            print(f"Sos: {Secilen_soslar}")
            topping_order.addTopping(Soslar(Secilen_soslar))

        except:
            print("Bir hata oluştu,Tekrar deneyiniz")
            
        
runTopping()


sub_çeşit = int(Siparis.getTotal())
sub_soslar =  int(topping_order.toppingTotal())
final_total = sub_çeşit + sub_soslar
finall=str(final_total)
siparis_tutarı= finall + "₺"
print(f" \nÖdemeniz gereken tutar {final_total}₺\n")


kullanıcı_adı=input("Lütfen ad ve soyadınız giriniz :")
while True:
        Tc_no=input("\nLütfen Tc Kimlik numaranızı giriniz : ")
        if len(Tc_no)==0:
            print("TC Kimlik Numarası Boş Olamaz")
        elif Tc_no.isdigit()==False:
            print("Sadece Rakam Giriniz")
        elif len(Tc_no)<11:
            print("TC Kimlik Numarası 11 Haneden Az Olamaz")
        elif len(Tc_no)>11:
            print("TC Kimlik Numarası 11 Haneden Fazla Olamaz")
        elif len(Tc_no)==11:
            break
        

while True:
        Kk_no=input("\nLütfen 16 haneli Kart Numarasını Giriniz : ")
        if len(Kk_no)==0:
            print("Kart No Boş Olamaz")
        elif Kk_no.isdigit()==False:
            print("Sadece Rakam Giriniz")
        elif len(Kk_no)<16:
            print("Kart No 16 Haneden Az Olamaz")
        elif len(Kk_no)>16:
            print("Kart No 16 Haneden Fazla Olamaz")
        elif len(Kk_no)==16:
            break
        

while True:
        K_sifresi=input("\nLütfen 4 Haneli Kart Şifresini Giriniz : ")
        if len(K_sifresi)==0:
            print("Şifre Hatalı")
        elif K_sifresi.isdigit()==False:
            print("Şifre Hatalı")
        elif len(K_sifresi)<4:
            print("Şifre Hatalı")
        elif len(K_sifresi)>4:
            print("Şifre Hatalı")
        elif len(K_sifresi)==4:
            break

a=datetime.datetime.now()
siparis_zamanı=str(a)        

with open("Orders_Database.csv", 'a',encoding="utf-8") as csvfile: 
    csvfile.write(kullanıcı_adı+"---""TC"+Tc_no+"---" + Kk_no+"---"+
                  K_sifresi+"---"+siparis_tutarı+"---"+siparis_zamanı+"\n" )
    
print("\nBizi Tercih Ettiğiniz için Teşekkür Ederiz\n")
print("Afiyet Olsun")