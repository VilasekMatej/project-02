'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81  # Normální pozemské tíhové zrychlení v m/s^2
MOON_GRAVITY = 1.625  # Měsíční gravitace v m/s^2
SPEED_OF_LIGHT = 299792458  # Rychlost světla ve vakuu v m/s
SPEED_OF_SOUND = 343  # Rychlost zvuku při teplotě 20 °C v suchém vzduchu v m/s

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
def weight_on_earth(mass):
    """
    Vypočítá váhu objektu na Zemi na základě jeho hmotnosti.
    """
    weight = mass * EARTH_GRAVITY
    return weight

def weight_on_moon(mass):
    """
    Vypočítá váhu objektu na Měsíci na základě jeho hmotnosti.
    """
    weight = mass * MOON_GRAVITY
    return weight

def speed_of_light(distance):
    """
    Vypočítá čas potřebný k překonání určité vzdálenosti rychlostí světla ve vakuu.

    :param distance: Vzdálenost (v metrech).
    :return: Čas cestování světlem (v sekundách).
    """
    time = distance / SPEED_OF_LIGHT
    return time

def speed_of_sound(distance):
    """
    Vypočítá čas potřebný k překonání určité vzdálenosti rychlostí zvuku při teplotě 20 °C v suchém vzduchu.

    :param distance: Vzdálenost (v metrech).
    :return: Čas cestování zvukem (v sekundách).
    """
    time_s = distance / SPEED_OF_SOUND
    return time_s