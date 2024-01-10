import requests
import bs4

# url = "https://warframe.fandom.com/wiki/Gotva_Prime"
url = "https://warframe.fandom.com/wiki/Catabolyst"
# url = "https://warframe.fandom.com/wiki/Amphis"
saturs = requests.get(url)

if(saturs.status_code == 200):
    lapas_saturs = bs4.BeautifulSoup(saturs.content, 'html.parser')

    atradu = lapas_saturs.find_all('div', attrs = {'data-source' : "Slot"})
    exact = atradu[0].find_all(class_="pi-data-value pi-font")
    slot = exact[0].string

    if(slot != "Melee"):

        atradu = lapas_saturs.find_all(class_="pi-item pi-item-spacing pi-title pi-secondary-background")
        for item in atradu:
            print(item.string) # Gotva Prime
        
        print("Crit Chance: ", end="")
        atradu = lapas_saturs.find_all('div', attrs = {'data-source' : "Attack1CritChance"})
        exact = atradu[0].find_all(class_="pi-data-value pi-font")
        crit = exact[0].string
        print(crit)

        print("Crit Dmg: ", end="")
        atradu = lapas_saturs.find_all('div', attrs = {'data-source' : "Attack1CritMultiplier"})
        exact = atradu[0].find_all(class_="pi-data-value pi-font")
        crit = exact[0].string
        print(crit)

        print("Status Chance: ", end="")
        atradu = lapas_saturs.find_all('div', attrs = {'data-source' : "Attack1StatusChance"})
        exact = atradu[0].find_all(class_="pi-data-value pi-font")
        crit = exact[0].string
        print(crit)

        print("Fire Rate: ", end="")
        atradu = lapas_saturs.find_all('div', attrs = {'data-source' : "Attack1FireRate"})
        exact = atradu[0].find_all(class_="pi-data-value pi-font")
        crit = exact[0].string
        print(crit)

        print("Multishot: ", end="")
        atradu = lapas_saturs.find_all('div', attrs = {'data-source' : "Attack1Multishot"})
        exact = atradu[0].find_all(class_="pi-data-value pi-font")
        crit = exact[0].string
        print(crit)
    else:
        pass

    
    
    # for item in atradu:
    #     exact = item.find_all('div', attrs = {'class' : "pi-data-value pi-font"})
    #     print(exact.string)


    # atradu = lapas_saturs.find_all('div', attrs = {'data-source' : True})
    # atradu = lapas_saturs.find_all(class_="pi-data-value pi-font")
    # print(atradu[0].string)
    # for item in atradu:
    #     print(item)