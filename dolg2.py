import math
import random

#1
alakzat = input("Kör vagy négyzet? (írj 'kör' vagy 'négyzet'): ")

if alakzat == "kör":

    sugar = float(input("Add meg a sugarat(cm): "))
    terulet1 = math.pi * sugar * sugar
    print("A kör területe:", terulet1, "cm2")
    
elif alakzat == "négyzet":

    oldal = float(input("Add meg az oldalhosszúságot(cm): "))
    terulet2 = oldal * oldal
    print("A négyzet területe: ",terulet2,"cm2")
    
else:
    print("Hibás választás! Kérjük, írj 'kör' vagy 'négyzet'.")


#2
helyes_nev = "admin"
helyes_jelszo = "1234"

nev = input("Felhasználónév: ")
jelszo = input("Jelszó: ")

nev_hibas = (nev != helyes_nev)
jelszo_hibas = (jelszo != helyes_jelszo)

if not nev_hibas and not jelszo_hibas:
    print("Sikeres bejelentkezés.")
elif nev_hibas and not jelszo_hibas:
    print("Ismeretlen felhasználó.")
elif not nev_hibas and jelszo_hibas:
    print("Hibás jelszó.")
else:
    print("Helytelen adatok.")



#3
osszeg = float(input("Add meg a vásárlás összegét (Ft): "))

if osszeg < 10000:
    kedvezmeny = 0
elif osszeg <= 20000:
    kedvezmeny = 0.05
else:
    kedvezmeny = 0.10

fizetendo = osszeg * (1 - kedvezmeny)

print("A fizetendő végösszeg: ", fizetendo, "Ft")


#4
osszeg = random.randint(1, 6) + random.randint(1, 6)
print("Összeg:", osszeg)

if osszeg > 9:
    print("Nagy dobás!")
elif osszeg >= 6:
    print("Közepes dobás.")
else:
    print("Kicsi dobás.")
