# Warframe Python projekts

## Projekta uzdevums

Warframe ir bezmaksas tiešsaistes trešās personas lomu šāvēja spēle, kuru izstrādāja un publicēja Digital Extremes.[1]

Viena no spēles Warframe īpašībām, kas to atšķir no līdzīga tipa žanra spēlēm, ir milzīgi liela arsenāla izvēle, kura galvenā doma ir, ka katrs var atrast to, kas patīk - gribas triecienšauteni? Ir klasiskās, kosmiskās, "inficēta" tipa un citas. Kādu pistoli? Arī ne mazāk izvēles ir šeit. Gribas kādu "inficēta" tipa granātmetēju, kas šauj lipīgus lādiņus, kas uzsprāgst ar indes mākoni? Spēlē warframe tādu ieroci sauc "Torid". Tātad, katrs spēlētājs varētu sev atrast tieši to, kas tuvāks sirdij. Bet, ja viss ir tik labi, tad par nekādu automatizāciju, kādu atvieglošanu domāt nevajadzētu. Tomēr, esot bezmaksas spēle, tai ir jābūt kaut kāds veids kā ģenerēt spēles ražotājiem iztiku, un šaja spēlē tā ir iekšspēles augstākās klases valūta, kura tiek saukta par platīnu, līdzās parastai valūtai, kuru var iegūt mainoties ar citiem spēlētājiem vai pērkot par naudu. Ja izvēlas bezmaksas veidu platīnas iegūšanai, tas var aizņemt salīdzinoši daudz laika, skatoties cik daudz tās vajag iegūt. Ar platīnas palīdzību var nopirkt gandrīz visu, bet saistībā ar šo projektu, tā lieta kas interesētu ir "pastiprinātāji", kas dubulto, cik kāds ierocis spēj sevī ietilpināt "modus", kas savukārt palielina kādu ieroča īpašību, piemēram, kaitējumu vai šaušanas ātrumu. Vienīgā problēma šajā situācijā ir ieroču efektivitātes disbalanss - ieroči, kas ir iegūstami spēles sākumā būs vienmēr vājāki nekā tie, kas ir iegūstami vēlāk, un, lai saprastu vai ieroci ir vērts izmantot, to vispirms ir jāiegūst, tad "jāpastiprina", tad jāpalielina ieroča līmenis līdz 30, tad "jāformē", kas atgriež ieroča līmeni līdz 0, bet atļauj ietilpināt vairāk "modus", un tad vēlreiz jāpalielina ieroča līmenis līdz 30 un "jāformē", līdz ietilpst visi vēlamie "modi", kas ir salīdzinoši laikietilpīgs process, vēl jo vairāk jauniem spēlētājiem. Šī projekta mērķis ir atvieglot aprēķinus, lai pašam ir vieglāk izvēlēties, vai šī ieroča efektivitāte, kaitējums utt ir pietiekami labs, lai uz to ieguldītu savu laiku un resursus. Svarīgi ir piebilst, tā kā šo projektu taisīju vairāk savu aprēķinu automatizācijai, kur es jau šajā spēlē salīdzinoši daudz saprotu, tas ir mazāk paredzēts jauniem spēlētājiem - tas nedos ieteikumus, vai ir kāds salīdzinoši labāks ierocis līdzīga tipa, tas neieteiks konkrētu stratēģiju atkarībā no ieroča. Man izlasot ieroča aprakstu vai vienkārši redzot vai izlasot, kā tas strādā un ko tas dara, ir pietiekami, lai saprastu, vai no tā ir salīdzinoši jēga. Šis projekts palīdz tieši ar cipariem, jo "pēc sajūtām" noteikt, kas ir efektīvāks ir salīdzinoši nekonsekventi, kā arī, vēlreiz, laikietilpīgi, jo tad katru ieroci vajag maksimizēt, pirms to lietoju, bet ar šo programmu es varu vienkārši ievadīt wikipēdijas saiti uz ieroci un man tiks izveidots, pēc manām domām, skaists excel dokuments, ar kuru tad pēc vēlēšanas varu arī tālāk strādāt.


### Kā projekts strādā

Palaižot "WarframeWeaponAutoExcel.py", tas prasīs ievadīt saiti uz kādu ieroci. Ieroču sarakstu var atrast "https://warframe.fandom.com/wiki/Weapons#List" un šis projekts strādā ieročiem no kategorijas "Primary" un "Secondary", kas var likties salīdzinoši maz, ņemot vērā visu pārējo kategoriju eksistenci, bet ieroči pārējās kategorijās ir vai nu saistīti ar ļoti specifiskām misijām, kas ikdienas gaitā netiek sastaptas vai starp tiem ir tikai daži, kas ir vērti uzlabošanai, lai tie būtu tādā līmenī kā primārias vai sekundārais ierocis, kas nozīmē, ka tur neko skaitīt nevajag, jo jau eksistē "labākie" no pārējām kategorijām.

Tad, izvēloties kādu no ieročiem, piemēram, "Primary" katergorijā, "Rifle" zemkategorijā, "Auto" tipa ceturtais ir "Baza Prime". Noklikšķinot uz to, lietotājs tiek aizsūtīts uz "https://warframe.fandom.com/wiki/Baza_Prime", kur šo saiti tad arī tālāk ir jāiekopē ievadē cmd.

Tad, programma nolasīs tai nepieciešamo informāciju no saites un, balstoties uz to, izveidos excel dokumentu ar jau gatavām "uzbūvēm" atkarība no ieroča tipa, kur šeit arī tad šī projekta lielākā automatizācijas daļa arī parādās. Spēlē Warframe vai nu nav vai ir uz rokām saskaitāmi gadījumi, kad kādi nosaukumi sakrīt savā starpā. Piemēram, "Rifle" tipa ieročiem kaitējuma palielināsanai var izmantot "modu", kuru sauc "Serration", kas šī "moda" desmitajā līmenī palielina ieroča kaitējumu par +165%. Bet "Shotgun" tipa ieročiem tāda tipa "modu" sauc "Point Blank", kas palielina kaitējumu par +90%. "Pistol" tipa ieročiem to sauc par "Hornet Strike", kas palielina par +220%. Tātad, to ir tik daudz un dažādi, ka, ja pēkšņi gribās apskatīt kādu konkrētu ieroci, tad vajag apskatīties to tipu, uzzināt kādus "modus" tas lieto, uzzināt to nosaukums un tikai tad var jau veikt aprēķinus. Šī programma to izdara mana vietā - uzzinot ieroča tipu, tā ģenerē excel failu, kurš jau tiek aizpildīts ar saderīgiem "modiem", kā arī kreisajā excel pusē, es pievienoju "špikeri" ar "modiem", kas tika lietoti, vai kas varētu interesēt. Dažiem no "modiem" ir arī īpašības, kas excel failā netiek parādītas, kā "Hunter Munitions", jo tas nav vienkāršs kaitējuma pastiprinātājs vai tamlīdzīgi, bet visi spēlētāji, kas ir ieguldījuši vismaz vidēju laiku spēlē ir pazīstami ar šo "modu" un tā funkcionalitāti, tāpēc tā detalizētu aprakstu es nepievienoju, jo, vēlreiz, šis ir vairāk domāts manu aprēķinu automatizācijai, nevis jauniem spēlētājeim.

Visbeidzot, pēc excel dokumenta izvedošanas, to var atvērt, "paspēlēties" ar to, samainot kādu "modu" jau pieejamās "būvēs" vai aizpildot tukšās "būves", kas atrodas pa labi. Tās arī ir atstātas tukšas ar iemeslu, ka vēlēšos "būvēs" pievienot "Riven" tipa "modus", kas ir pēc nejaušības ģenerēti "modi" konkrēta tipa ierocim, un, pat ja divu viena ieroča "Riven modu" bonusi sakrīt, tie nebūs vienādi skaitliski.


## Izmantotās bibliotēkas

requests - saites informācijas nolasīšanai
bs4 - saites informācijas apstrādei
os - faila esamības pārbaudei
openpyxl - excel faila radīšanai un apstrādei


## Programmatūras izmantošanas metodes

Lai automatizētu aprēķinus ieročiem spēlē Warframe, izmantojot ieroča wiki saiti


### Izmantotā literatūra:
1. https://en.wikipedia.org/wiki/Warframe