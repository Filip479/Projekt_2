"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Filip
email: 479@seznam.cz
discord: Filip479#8140
"""


import random

def generuj_cislo() -> list:
    """
    Vybere 4 náhodné číslice,
    které jsou různé a nezačínají nulou.
    Tyto tajné číslice bude hráč hádat.

    Příklad:
    9074
    """
    tajne_cislo = random.sample(range(0, 10), 4)
    while tajne_cislo[0] == 0:
        random.shuffle(tajne_cislo)
    return tajne_cislo


def porovnej_seznamy(tajne_c_porovnej, hracuv_vstup) -> tuple[int, int]:
    """
    Porovná seznam vygenerovaných čísel a seznam čísel, které zadal hráč.
    Pokud najde shodu na stejné pozici, přičte do skóre  'Bulls' + 1.
    Pokud najde shodu na jiné pozici, přičte do skóre  'Cows' + 1.
    """
    bulls = 0
    cows = 0
    for cislo in range(len(hracuv_vstup)):
        if hracuv_vstup[cislo] == tajne_c_porovnej[cislo]:
            bulls += 1
        elif hracuv_vstup[cislo] in tajne_c_porovnej:
            cows += 1
    return bulls, cows


def hra() -> None:
    """
    Přiřadí proměnné náhodně vygenerované číslo.
    Nechá hráče zadat svůj tip a vytvoří z něj seznam.
    Porovná seznam vygenerovaných a seznam čísel hráče.
    Vytiskne skóre po každém pokusu hráče.
    Když je skóre Bulls rovno 4, hráč vyhrál a hra končí.
    """
    tajne_c_hra = generuj_cislo()
    # print(tajne_c_hra)
    while True:
        tip_hrace = input("\nZadej svůj tip: ")
        if len(tip_hrace) != 4 or not tip_hrace.isdigit():
            print("Zadej právě 4 číslice")
            continue
        tip_list = [int(item) for item in tip_hrace]
        skore_bulls, skore_cows = porovnej_seznamy(tajne_c_hra, tip_list)
        if skore_bulls == 4:
            break
        print(f"{skore_bulls} bull" + ("s" if skore_bulls != 1 else ""),
            f"{skore_cows} cow" + ("s" if skore_cows != 1 else ""))
    print("Výborně ! Vyhrál jsi ! Uhodl jsi tajné číslo !")


def pravidla():
    """
    Uvítá hráče a zobrazí mu pravidla hry.
    """
    print(
    """
    -------------------------------
    Vítejte ve hře 'Bulls and Cows'
    -------------------------------
    """
    )
    print(
    """
    Pravidla hry:
    1. Program vygeneruje náhodné 4 místné číslo,
    2. Vaším úkolem je uhádnout toto číslo,
    3. Číslice musí být unikátní a nesmí začínat 0,
    4. 'Bulls' znamená, že uhádnutá číslice je na správné pozici,
    5. 'Cows' znamená, že uhádnutá číslice není na správné pozici.
    6. Číslo u 'Bulls' nebo 'Cows' značí počet uhádnutých číslic.

    Hodně štěstí !
    """) 


def main():
    pravidla()
    hra()
main()
