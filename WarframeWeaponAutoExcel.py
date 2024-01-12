import requests
import bs4
from MakeExcel import *

# url = "https://warframe.fandom.com/wiki/Baza_Prime"
# url = "https://warframe.fandom.com/wiki/Corinth_Prime"
# url = "https://warframe.fandom.com/wiki/Afuris_Prime"
url = "https://warframe.fandom.com/wiki/Nikana_Prime"
# url = "https://warframe.fandom.com/wiki/Gotva_Prime"
# url = "https://warframe.fandom.com/wiki/Paris_Prime"
# url = "https://warframe.fandom.com/wiki/Catabolyst"
# url = "https://warframe.fandom.com/wiki/Amphis"
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

    if(WeaponSlot == "Primary" and (WeaponType == "Bow" or WeaponType == "Crossbow" or WeaponType == "Exalted Weapon" or WeaponType == "Launcher" or WeaponType == "Rifle" or WeaponType == "Sniper Rifle" or WeaponType == "Speargun" or WeaponName == "Shedu")):
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
    
        RifleExcel(InfoList)

    elif(WeaponSlot == "Primary" and WeaponType == "Shotgun"):
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
    
        ShotgunExcel(InfoList)

    elif(WeaponSlot == "Secondary"):
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
    
        PistolExcel(InfoList)

    elif(WeaponSlot == "Melee"):
        Souped = RawSite.find_all(class_="pi-item pi-item-spacing pi-title pi-secondary-background")
        WeaponName = Souped[0].string

        Souped = RawSite.find_all('div', attrs = {'data-source' : "Attack1AttackSpeed"})
        Value = Souped[0].find_all(class_="pi-data-value pi-font")
        AttackSpeed = Value[0].string
        AttackSpeed = AttackSpeed.split(" ")[0]
        AttackSpeed = AttackSpeed[:-1]
        AttackSpeed = float(AttackSpeed)

        Souped = RawSite.find_all('div', attrs = {'data-source' : "Attack1CritChance"})
        Value = Souped[0].find_all(class_="pi-data-value pi-font")
        CriticalChance = Value[0].string
        CriticalChance = CriticalChance[:-1]
        CriticalChance = float(CriticalChance)
        
        Souped = RawSite.find_all('div', attrs = {'data-source' : "Attack1CritMultiplier"})
        Value = Souped[0].find_all(class_="pi-data-value pi-font")
        CriticalDamage = Value[0].string
        CriticalDamage = CriticalDamage[:-1]
        CriticalDamage = float(CriticalDamage)

        Souped = RawSite.find_all('div', attrs = {'data-source' : "Attack1StatusChance"})
        Value = Souped[0].find_all(class_="pi-data-value pi-font")
        StatusChance = Value[0].string
        StatusChance = StatusChance[:-1]
        StatusChance = float(StatusChance)

        Souped = RawSite.find_all('div', attrs = {'data-source' : "Attack1Total"})
        Value = Souped[0].find_all(class_="pi-data-value pi-font")
        Damage = str(Value[0])
        Damage = Damage[Damage.find("pi-data-value pi-font")+23:Damage.find("pi-data-value pi-font")+32]
        Damage = Damage.split(" ")
        Damage = Damage[0]
        Damage = float(Damage)
        
        Souped = RawSite.find_all('div', attrs = {'data-source' : "MeleeRange"})
        Value = Souped[0].find_all(class_="pi-data-value pi-font")
        MeleeRange = Value[0].string
        MeleeRange = MeleeRange.split(" ")
        MeleeRange = MeleeRange[0]
        MeleeRange = float(MeleeRange)


        print("Weapon name:", WeaponName)
        print("Damage:", Damage)
        print("Range:", MeleeRange)
        print("Attack Speed:", AttackSpeed)
        print("Critical Chance:", CriticalChance)
        print("Critical Damage:", CriticalDamage)
        print("Status Chance:", StatusChance)

    else:
        print("Unsupported weapon type or invalid link!")
