import requests
import bs4
from MakeExcel import *

url = input("Lūdzu iekopējiet url: ")
# url = "https://warframe.fandom.com/wiki/Baza_Prime"
# url = "https://warframe.fandom.com/wiki/Corinth_Prime"
# url = "https://warframe.fandom.com/wiki/Afuris_Prime"
# url = "https://warframe.fandom.com/wiki/Gotva_Prime"
# url = "https://warframe.fandom.com/wiki/Paris_Prime"
# url = "https://warframe.fandom.com/wiki/Catabolyst"

TheSite = requests.get(url)

if(TheSite.status_code == 200):
    RawSite = bs4.BeautifulSoup(TheSite.content, 'html.parser')

    Souped = RawSite.find_all('div', attrs = {'data-source' : "Slot"})
    Value = Souped[0].find_all(class_="pi-data-value pi-font")
    WeaponSlot = Value[0].string

    Souped = RawSite.find_all('div', attrs = {'data-source' : "Class"})
    Value = Souped[0].find_all(class_="pi-data-value pi-font")
    WeaponType = Value[0].string

    Souped = RawSite.find_all(class_="pi-item pi-item-spacing pi-title pi-secondary-background")
    WeaponName = Souped[0].string

    InfoList = []
    InfoList.append(WeaponName)

    Souped = RawSite.find_all('div', attrs = {'data-source' : "Attack1Multishot"})
    Value = Souped[0].find_all(class_="pi-data-value pi-font")
    MSandDMG = Value[0].string
    MSandDMG = MSandDMG.split(" ")
    Multishot = MSandDMG[0]
    Multishot = float(Multishot)
    Damage = MSandDMG[1][1:]
    Damage = float(Damage)
    InfoList.append(Damage)
    InfoList.append(Multishot)

    Souped = RawSite.find_all('div', attrs = {'data-source' : "Attack1FireRate"})
    Value = Souped[0].find_all(class_="pi-data-value pi-font")
    FireRate = Value[0].string
    FireRate = FireRate.split(" ")
    FireRate = FireRate[0]
    FireRate = float(FireRate)
    InfoList.append(FireRate)

    Souped = RawSite.find_all('div', attrs = {'data-source' : "Attack1CritChance"})
    Value = Souped[0].find_all(class_="pi-data-value pi-font")
    CriticalChance = Value[0].string
    CriticalChance = CriticalChance[:-1]
    CriticalChance = float(CriticalChance) * 0.01
    InfoList.append(CriticalChance)
    
    Souped = RawSite.find_all('div', attrs = {'data-source' : "Attack1CritMultiplier"})
    Value = Souped[0].find_all(class_="pi-data-value pi-font")
    CriticalDamage = Value[0].string
    CriticalDamage = CriticalDamage[:-1]
    CriticalDamage = float(CriticalDamage)
    InfoList.append(CriticalDamage)

    Souped = RawSite.find_all('div', attrs = {'data-source' : "Attack1StatusChance"})
    Value = Souped[0].find_all(class_="pi-data-value pi-font")
    StatusChance = Value[0].string
    StatusChance = StatusChance[:-1]
    StatusChance = float(StatusChance) * 0.01
    InfoList.append(StatusChance)

    if(WeaponSlot == "Primary" and (WeaponType == "Bow" or WeaponType == "Crossbow" or WeaponType == "Exalted Weapon" or WeaponType == "Launcher" or WeaponType == "Rifle" or WeaponType == "Sniper Rifle" or WeaponType == "Speargun" or WeaponName == "Shedu")):
        RifleExcel(InfoList)

    elif(WeaponSlot == "Primary" and (WeaponType == "Shotgun" or WeaponName == "Bubonico")):
        ShotgunExcel(InfoList)

    elif(WeaponSlot == "Secondary"):
        PistolExcel(InfoList)

    else:
        print("Unsupported weapon type or invalid link!")
