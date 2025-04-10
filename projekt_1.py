# moje údaje: 
# """
# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Zuzana Fabiánová
# email: zuzanka72@seznam.cz
# """



uzivatele = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

user = input("Zadejte své uživatelské jméno: ")
password = input("Zadejte své heslo: ")
print("-" * 40)

if uzivatele.get(user) != password:
    print("Neplatné přihlašovací údaje nebo nejste registrován. Program se nyní ukončí.")
    exit()

print(f"Vítejte v aplikaci, {user}!\nMáme {len(TEXTS)} texty k analýze.")
print("-" * 40)

print("Zadejte, prosím, číslo textu, který chcete analyzovat --> 1, 2, nebo 3:")
vyber = input("Vaše vybrané číslo textu je: ")

if not vyber.isdigit() or not 1 <= int(vyber) <= len(TEXTS):
    print("Vybrali jste neplatné číslo textu. Program se nyní ukončí.")
    exit()

vybrany_text = TEXTS[int(vyber) - 1]
slova = vybrany_text.split()

pouze_slova = [slovo.strip(".,") for slovo in slova]

pocet_Slov = len(pouze_slova)
velke_pismeno_zacatek = [s for s in pouze_slova if s.istitle()]
velka_slova = [s for s in pouze_slova if s.isupper()]
mala_slova = [s for s in pouze_slova if s.islower()]
pocet_cislic = [s for s in pouze_slova if s.isdigit()]
suma_cislic = sum(int(num) for num in pocet_cislic)

print("-" * 40)
print(f"Počet slov ve vybraném textu je: {pocet_Slov}")
print(f"počet slov začínajících velkým písmenem ve vybraném textu je: {len(velke_pismeno_zacatek)}")
print(f"Počet slov psaných velkými písmeny ve vybraném textu je: {len(velka_slova)}")
print(f"Počet slov psaných malými písmeny ve vybraném textu je: {len(mala_slova)}")
print(f"Počet čísel ve vybraném textu je: {len(pocet_cislic)}")
print(f"Suma všech čísel ve vybraném textu je: {suma_cislic}")
print("-" * 40)

print("DÉLKA | GRAF | POČET")
print("-" * 40)
pocet_vyskytu = {}

for slovo in pouze_slova:
    delka = len(slovo)
    pocet_vyskytu[delka] = pocet_vyskytu.get(delka, 0) + 1

for delka in sorted(pocet_vyskytu):
    pocet = pocet_vyskytu[delka]
    print(f"{delka:>5} | {'*' * pocet:<20} | {pocet}")

print(f"To je vše z analýzy textu, {user}. Měj hezký den!")
    