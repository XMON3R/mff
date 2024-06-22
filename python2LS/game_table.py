import time
import sys
import random                    #z modulu random použity funkce jako random.choice (Kdo začne?) či random.shuffle (michání karet)

mezery = "---------------"

##############################################################################################################################
#KAPITOLA 1 -> Prší 
##############################################################################################################################                      

barvy = ["SRDCE", "KULE", "LISTY", "ŽALUDY"]                        #Jednotlivé barvy karet v seznamu                                      
typ = ["7","8","9","10","SPODEK","SVRŠEK","KRÁL","ESO"]             #Jednotlivé typy karet v seznamu

hrac = []               #seznam živého hráče (INPUT)
pc = []                 #seznam karet počítače, který bude random volit 

liznutelne_karty = []          #seznam pro všechny karty, kam se na začátku vytvoří balíček jako takový, 
                                #lízne se z něj 8 karet pro hráče a jedna, na kterou se bude hrát

# global hraci_balicek

hraci_balicek = []                #na tento balíček se bude hrát 

class karta:                                            #CLASS POUŽÍVÁN NA URČENÍ BARVY A TYPU
    def __init__(self, barva, typ, special,usage):
        self.barva = barva                                     
        self.typ = typ          
        self.special = special  #reprezentace toho, zda je karta speciální (7 či ESO, či ne)
        self.usage = usage      #USAGE je používán pro zjištění, zda je karta "aktivní", či ne u 7ček a ES 
                                    # -> pokud je USAGE 0, již není potřeba stát ani lízat, pokud 1 - efekt platí

##############################################################################################################################

#FUNKCE NA VYTVOŘENÍ BALÍČKU KARET
def vytvor_balicek(self, balicek):
    for i in barvy:      #Každé i ze seznamu "barvy" kombinuji s každou ze 4 barev, tedy s každým j ze seznamu "typ".
        for j in typ:  
            nejaka_karta = (i,j)        #Ukládám jako tuple především kvůli zjednodušení práce.
            
            if j == "7" or j == "ESO":                      #Toto mi zaručí jednodušší kontrolu 7 a ES skrze volání otázky, zda 
                                                            #je USAGE 0 či ne                
                nejaka_karta = karta(barva = i, typ = j, special = "->" + str(j) + "<-", usage = 1)        
            
            else:
                nejaka_karta = karta(barva = i, typ = j, special = "", usage = 0) 
            
            self.append(nejaka_karta)   
    random.shuffle(balicek)                         


##############################################################################################################################

#FUNKCE NA ZOBRAZOVÁNÍ KARET PRO UŽIVATELE 
#Vzhledem k tomu, že jsem z karet udělal objekty typu class, tak pro jejich "racionální" zobrazení uživateli nyní potřebuji
#jednoduchou funkci pro zobrazení karet tak, jak je sami vnímáme při hraní Prší v reálném světě.

def ukaz_kartu(karta):                         #vytiskni danou kartu
    print(karta.barva + " " + karta.typ)        #v printu zkombinuj barvu a typ (např. "SRDCE ESO")
    print()

def ukaz_ruku(balicek):                       #vytiskni celý daný balíček (může být i ruka hráče), formát jako ukaz_kartu
    for x in balicek:                    
        print(x.barva + " " + x.typ + " " + x.special)
    print()


#Funkce ukaz_ruku_pro_hrace vznikla jako zjednodušení pro uživatele, aby viděl, která karta má jaké číslo. Pro intuitivnost a pro 
#hráče nepolíbené informací, jak funguje indexování v počítači, začínají čísla 1, ne 0 (jako to dělá počítač)**.

def ukaz_ruku_pro_hrace(balicek):                       #vytiskni celý daný balíček (může být i ruka hráče), formát jako ukaz_kartu
    for x in balicek:
        print(balicek.index(x)+1, x.barva + " " + x.typ)        #** to je zaručeno zde, v "balicek.index(x)+´1´"
    print()                                                

##############################################################################################################################

def start_lizani(balicek, lizaci_balicek):           #balicek reprezentuje ruku daného hráče
    StartPocet = 4                  
    for i in range(StartPocet):
        balicek.append(lizaci_balicek.pop())        #funkci pop používám pro zjednodušení přemisťování karet
                                                        #z Liznutelnych karet dávám do balíčku

#nahodne vyber jednu kartu z balicku, na kterou se zacne hrat
def liznuti_vrchni_karty(hraci_balik, lizaci_balik):                        #Pomocí pop z lizacího balíčku vytáhne jednu kartu
    if lizaci_balik[0].typ == "SVRŠEK":           #Pokud je vytažená vrchní karta, vezmi barvu spodní karty Lízacího balíčku
        lizaci_balik[0].barva = lizaci_balik[-1].barva
    hraci_balik.append(lizaci_balik.pop())                              

def ukaz_vrchni_kartu(balicek):       #UKAŽ vrch_karta, podobné jako u ukaz_kartu, funkce spíše pro přehlednost
    ukaz_kartu(balicek[0])                                            #zobrazí vrchní kartu hracího balíčku 

##############################################################################################################################
#VERZE: HRÁČ
def vybrani_karty(seznam_karet, hraci_balicek, lizaci_balicek):
        vybrana_karta = 0         #na počátku 0

    #While loop zaručuje držení hráče do té doby, dokud nenapíše validní číslo karty viditelné v ukaz_ruku_pro_hrace, či zvolí lízání
        while True:   
            try:
                #int -> číselný inputu, v případě, že by uživatel zadal znaky (str), tak je zde except ValueError
                vybrana_karta = int(input("Napište sem číslo vámi zvolené karty. Pokud jste si to rozmyslel a radši byste lízl kartu, napiště 0: ")) - 1

                #vybrana_karta reprezentuje vybranou kartu, používáno pro hratelnost_karty níže 
            
            except ValueError:
                print("Nezadávejte prosím znaky.")                      #při špatném hráč-inputu program nespadne
                vybrani_karty(seznam_karet, hraci_balicek, lizaci_balicek)

            if vybrana_karta >= len(hrac):                            #pochopitelné z obsahu printu                                                
                print("Zadejte prosím maximálně tak velké číslo, které odpovídá počtu karet ve Vaší ruce.")
                vybrani_karty(seznam_karet, hraci_balicek, lizaci_balicek)

            elif vybrana_karta < -1:                                                #pochopitlné z obsahu printu
                print("Zadejte prosím minimálně číslo 0 pro líznutí a 1 pro zahrání.")
                vybrani_karty(seznam_karet, hraci_balicek, lizaci_balicek)

            elif vybrana_karta == -1:                       #-1, kvůli vybrana_karta = int(input)-1 
                print("Zvolil jste lízání.")   
                lizni(seznam_karet, lizaci_balicek)      #Viz Lízni 
                break

            else:
                break
        
        if vybrana_karta == -1:
            return

        vrch_karta = hraci_balicek[0]            #vrch_karta reprezentuje vrchni kartu hracího balíčku

        hratelnost_karty(vrch_karta, seznam_karet, lizaci_balicek, hraci_balicek, vybrana_karta)   #viz CardPlayabality 
        return

##############################################################################################################################
#tahy hráče a počítače

def tah_hrace(lizaci_balicek, hraci_balicek, ruka_hrace):

    print("Vaše karty:")                                        #Na začátku zobrazím hráči karty, které má v ruce.
    ukaz_ruku_pro_hrace(ruka_hrace)

    print("")
    print("Karta, na kterou hrajete:")                          #Následně mu zobrazím kartu, na kterou se hraje.
    ukaz_vrchni_kartu(hraci_balicek)
    vrch_karta = hraci_balicek[0]
                                                                #Poté zkontroluji, zda se jedná o 7 či eso.

    #POKUD SE JEDNÁ O 7:                                                            
    if vrch_karta.typ == "7" and vrch_karta.usage == 1:                  
        input("Na stole leží sedmička, lízněte 2 karty.")       
        a = 0
        hraci_balicek[0].usage = a    #vynulování USAGE (viz class karta), aby tato sedmička neplatila pro dalšího hráče
        for i in range(2):
            lizni(ruka_hrace, lizaci_balicek)               #Lizní dvě karty (viz funkce Lízni)
        return                                     #return, aby se již dále nepokračovalo = hráč přichází správně o tah

    #POKUD SE JEDNÁ O ESO:
    elif vrch_karta.typ == "ESO" and vrch_karta.usage == 1:       #Funguje velmi podobně jako kontrola 7 včetně vynulování USAGE.
        input("Na stole leží eso, nehrajete.")
        a = 0
        hraci_balicek[0].usage = a                 #STOJÍ SE, tedy hráč přichází o tah.
        return

    #POKUD SE NEJEDNALO O 7 A ANI O ESO, "NORMÁLNÍ" TAH:
    else:
        print("Pro zahrání karty napište 'z', pro líznutí 'l'.\n")          #hráč do inputu zadá buď "z", nebo "l"
        volba = ""
        zahrat_kartu = "z"
        liznout_kartu = "l"
        while volba != zahrat_kartu or liznout_kartu:       #Dokud nenapíše jednu z těchto dvou možností, hra ho drží v loopu
            volba = input("Napište prosím svou volbu: ").lower()
        
            if volba == zahrat_kartu:
                vybrani_karty(ruka_hrace, hraci_balicek, liznutelne_karty)    #vysvětlení viz vybrani_karty
                return
        
            elif volba == liznout_kartu:                                   #vysvětlení viz Lízni
                lizni(ruka_hrace, liznutelne_karty)
                return
        
            else:                                            #Pokud hráč nevybral nic správně, tak se loop opakuje.
                print("---------------------------")
                tah_hrace(lizaci_balicek, hraci_balicek, ruka_hrace)         #volání funkce znovu
                return            

##############################################################################################################################           

def tah_pc(Lizani, hrani, ruka_pc):            #velmi podobné jako tah_hrace, jen bez inputů a printů
    
    vrch_karta = hrani[0]

    if vrch_karta.typ == "7" and vrch_karta.usage == 1:    
        print("Na stole leží (aktivní) 7mička, počítač líže 2 karty.")               
        for i in range(2):
            lizni(ruka_pc, Lizani)
        a = 0
        hrani[0].usage = a                                      #VYNULOVÁNÍ, ABY EFEKT JIŽ NEPLATIL 
        return

    elif vrch_karta.typ == "ESO" and vrch_karta.usage == 1:
        print("Na stole leží (aktivní) Eso, počítač stojí.")
        a = 0
        hrani[0].usage = a                                   #VYNULOVÁNÍ, ABY EFEKT JIŽ NEPLATIL 
        return

    else:
        vybrani_kartyPC(ruka_pc, Lizani, hrani)              #viz vybrani_kartyPC


##############################################################################################################################

def hratelnost_karty(hrana_karta, seznam_karet, lizaci_balicek, hraci_balicek, vybrana_karta):
    #1. MOŽNOST
    #karta se shoduje v barvě či v typu

    #kontrola zvolené karty se současnou vrch_karta, na kterou se hraje
    if hrana_karta.barva == seznam_karet[vybrana_karta].barva or hrana_karta.typ == seznam_karet[vybrana_karta].typ:      

        if seznam_karet[vybrana_karta].typ == "SVRŠEK":                #Kontrola, zda je vybrana_karta SVRŠEK
            a = ""
            input("Zahrál jste svrška. Zvolte prosím novou barvu.")         #Zvolení nové barvy
            while a not in barvy:                   #Loop dokud uživatel dobře nezadá barvu
                a = input("Vyberte novou barvu: ")
            seznam_karet[vybrana_karta].barva = a                          #změna barvy karty

        hraci_balicek.append(seznam_karet[vybrana_karta])      #Zahraje vybranou kartu do PlayBalicku na index 0
        seznam_karet.remove(seznam_karet[vybrana_karta])            #následně tuto kartu odebere z ruky hráče
        hraci_balicek.reverse()                         #zaručí, že přidá karta bude na indexu 0

        input("Zahrál jste kartu. Na tahu je soupeř (stisknutím tlačítka bude hra pokračovat).")
        print("---------------------")

    #2. MOŽNOST 
    #karta se shoduje v barvě i typu (případ svrška)
    elif hrana_karta.barva == seznam_karet[vybrana_karta].barva and hrana_karta.typ == seznam_karet[vybrana_karta].typ:  

        if seznam_karet[vybrana_karta].typ == "SVRŠEK":
            a = ""
            input("Zahrál jste svrška. Zvolte prosím novou barvu.")
            while a not in barvy:
                a = input("Vyberte novou barvu: ")
            seznam_karet[vybrana_karta].barva = a 
    
        else: #klasika
            print("Kartu lze zahrát.")                                  #FUNGUJE stejně, viz výše

        hraci_balicek.append(seznam_karet[vybrana_karta])      #Zahraje vybranou kartu do PlayBalicku na index 0
        seznam_karet.remove(seznam_karet[vybrana_karta])            #následně tuto kartu odebere z ruky hráče
        hraci_balicek.reverse()
        
       
        input("Zahrál jste kartu. Na tahu je soupeř (stisknutím tlačítka bude hra pokračovat).")
        print("---------------------")
    

    #3. MOŽNOST, NELZE ZAHRÁT TUTO KARTU
    else:       
        if seznam_karet[vybrana_karta].typ == "SVRŠEK":  #svršek je výjimka, jde zahrát kdykoliv (případ esa a 7 ošetřen již dříve)
            a = ""
            input("Zahrál jste svrška. Zvolte prosím novou barvu.")
            while a not in barvy:
                a = input("Vyberte novou barvu: ")                              
            seznam_karet[vybrana_karta].barva = a 

            hraci_balicek.append(seznam_karet[vybrana_karta])      #Zahraje vybranou kartu do PlayBalicku na index 0
            seznam_karet.remove(seznam_karet[vybrana_karta])            #následně tuto kartu odebere z ruky hráče
            hraci_balicek.reverse()
    

        else: 
            print("Zvolená karta nelze zahrát.")
            vybrani_karty(seznam_karet, hraci_balicek, lizaci_balicek)    #pokud karta nelze zahrát, uživatel znovu vybírá kartu      #FUNGUJE stejně, viz výše

############################################################################################################################## 
#VERZE: PC

def vybrani_kartyPC(seznam_karet, lizaci_balik, hraci_balicek):     #skoro stejné jako vybrani_karty u hráče, jen bez inputů 

        def NeniNutneLiznout(seznam_karet, vrch_karta):         #speciální funkce na zhodnocení, zda počítač může něco zahrát
            check = 0
            for karty in seznam_karet:
                if (karty.barva == vrch_karta.barva and karty.typ == vrch_karta.typ) or (karty.barva == vrch_karta.barva or karty.typ == vrch_karta.typ):
                    check = check + 1                  #check pak reprezentuje počet zahratelných karet
            
            #případ, kdy check není 0:
            if check != 0:
                vybrana_karta = random.randint(0,len(pc)-1)               #počítač vybere náhodnou hratelnou kartu
                hratelnost_kartyPC(vrch_karta, seznam_karet, lizaci_balik, hraci_balicek, vybrana_karta)   #viz hratelnost_kartyPC

            #případ, kdy check je 0:
            elif check == 0:
                lizni(pc, liznutelne_karty)                 #Viz Lízni 
                print("Počítač si líznul. Jste na řadě.")


        def hratelnost_kartyPC(hrana_karta, seznam_karet, lizaci_balik, hraci_balik, vybrana_karta):
            #kontrola zvolené karty se současnou vrch_karta, na kterou se hraje 
            if hrana_karta.barva == seznam_karet[vybrana_karta].barva or hrana_karta.typ == seznam_karet[vybrana_karta].typ:     
                
                if seznam_karet[vybrana_karta].typ == "SVRŠEK":
                    a = 0            #Tato podmínka vyhodnocuje optimální výběr barvy při zahrání svrška
                    b = 0
                    c = 0            #proměnné a-d reprezentují hojnost barev v ruce pc
                    d = 0
                    for x in pc:
                        if x.barva == "SRDCE":
                            a = a + 1                       #při každém výskytu dané barvy se daná proměnná zvětší o 1
                        elif x.barva == "KULE":          
                            b = b + 1
                        elif x.barva == "LISTY":
                            c = c + 1
                        elif x.barva == "ŽALUDY":
                            d = d + 1

                    helplist = []           #pomocný list, který je po appendnutí (přidání) všech proměnných prohledán
                    helplist.append(a)
                    helplist.append(b)
                    helplist.append(c)
                    helplist.append(d)

                    max_value = max(helplist)                   #nalezne se maximální hodnota, ze které se následně vyhodnocuje
                    max_index = helplist.index(max_value)
                
                    seznam_karet[vybrana_karta].barva = barvy[max_index]                   #zahrání ideální barvy

                hraci_balik.append(seznam_karet[vybrana_karta])      #Zahraje vybranou kartu do PlayBalicku na index 0
                seznam_karet.remove(seznam_karet[vybrana_karta])            #následně tuto kartu odebere z ruky hráče
                hraci_balik.reverse()

                print("PC zahrál kartu. Jste na řadě.")
                print("---------------------")
       
            elif hrana_karta.barva == seznam_karet[vybrana_karta].barva and hrana_karta.typ == seznam_karet[vybrana_karta].typ:  
                if seznam_karet[vybrana_karta].typ == "SVRŠEK":
                    a = 0 
                    b = 0                       #VIZ STEJNÁ PODMÍNKA VÝŠE
                    c = 0
                    d = 0
                    for x in pc:
                        if x.barva == "SRDCE":
                            a = a + 1
                        elif x.barva == "KULE":
                            b = b + 1
                        elif x.barva == "LISTY":
                            c = c + 1
                        elif x.barva == "ŽALUDY":
                            d = d + 1

                    helplist = []
                    helplist.append(a)
                    helplist.append(b)
                    helplist.append(c)
                    helplist.append(d)

                    max_value = max(helplist)
                    max_index = helplist.index(max_value)
                
                    seznam_karet[vybrana_karta].barva = barvy[max_index]
    
                hraci_balik.append(seznam_karet[vybrana_karta])      #Zahraje vybranou kartu do PlayBalicku na index 0
                seznam_karet.remove(seznam_karet[vybrana_karta])            #následně tuto kartu odebere z ruky hráče
                hraci_balik.reverse()

                print("PC zahrál kartu. Jste na řadě.")
                print("---------------------")
                
            else:   
                if seznam_karet[vybrana_karta].typ == "SVRŠEK":
                    a = 0 
                    b = 0                       #VIZ STEJNÁ PODMÍNKA VÝŠE
                    c = 0
                    d = 0
                    for x in pc:
                        if x.barva == "SRDCE":
                            a = a + 1
                        elif x.barva == "KULE":
                            b = b + 1
                        elif x.barva == "LISTY":
                            c = c + 1
                        elif x.barva == "ŽALUDY":
                            d = d + 1

                    helplist = []
                    helplist.append(a)
                    helplist.append(b)
                    helplist.append(c)
                    helplist.append(d)

                    max_value = max(helplist)
                    max_index = helplist.index(max_value)
                
                    seznam_karet[vybrana_karta].barva = barvy[max_index]
    
                    hraci_balik.append(seznam_karet[vybrana_karta])      #Zahraje vybranou kartu do PlayBalicku na index 0
                    seznam_karet.remove(seznam_karet[vybrana_karta])            #následně tuto kartu odebere z ruky hráče
                    hraci_balik.reverse()

                    print("PC zahrál kartu. Jste na řadě.")
                    print("---------------------")
                
                else:
                    vybrani_kartyPC(seznam_karet, lizaci_balik, hraci_balik)


        vrch_karta = hraci_balicek[0] 

        NeniNutneLiznout(seznam_karet, vrch_karta)      #volání výše definové funkce, kontrola, zda se musí lízat, či ne

##############################################################################################################################
def dojdou_kartyTEST(lizaci_balicek, odhazovaci_balicek):  
    helplist = []                       #pomocný list na uložení vrchní karty, na kterou se bude i nadále hrát
    helplist.insert(0,odhazovaci_balicek[0])    #vložení vrchní karty
    odhazovaci_balicek.remove(odhazovaci_balicek[0])    #odebrání vrchní karty z hracího balíčku (aby nebyl duplikát)

    while len(odhazovaci_balicek) != 0:              #dokud v odhazovacím balíčku není jen jedna karta
        premichana = odhazovaci_balicek.pop()       
        lizaci_balicek.append(premichana)       #vkládej karty z hracího balíčku do lízacího, dokud není hrací prázdný

        random.shuffle(lizaci_balicek)          #zamíchej vytáhlé karty
        

    for karty in liznutelne_karty:        #OŠETŘENÍ, ŽE SE SEDMIČKY A ESO "ZNOVU-AKTIVUJÍ", jinak by byly po 1 použití 
        if karty.special != "":             #bez efektu, a to nechceme
            reset = 1
            karty.usage == reset
        
    odhazovaci_balicek.append(helplist[0])      #Vrať vrchní kartu do hracího balíčku, to zaručí i "ne-znovuaktivaci"
                                                            #V odhazovacím balíčku tak bude 1 karta.

##############################################################################################################################

#LIZÁNÍ

def lizni(balicek_kam, balicek_odkud):                                     
    if balicek_odkud != []:                                #if, aby se mi nemohlo stát, že bude lízat z NIČEHO 
        balicek_kam.append(balicek_odkud.pop())                         #balicek odkud je lízací balíček
                                                                        #balicek kam je ruka hráče či pc
    
    #Ošetření případu, kdy je lízací balíček prázdný, ale nikdo nezahrál kartu
    elif liznutelne_karty == [] and len(hraci_balicek) == 1:   
        print("Není z čeho lízat a ani přemíchat, zahrajte kartu.")
        vybrani_karty(balicek_kam,hraci_balicek,balicek_odkud)
        return
    
    #Nutnost přemíchání balíčku jako v "reálném" Prší
    elif liznutelne_karty == [] and len(hraci_balicek) != 1:     #pokud je lizácí balíček prázdný a je odehráno více než 1 karet
        print("Není z čeho lízat, přemíchávám balíček.")
        dojdou_kartyTEST(balicek_odkud, hraci_balicek)       #Viz dojdou_karty níže 
        lizni(balicek_kam, balicek_odkud)                   #po přemíchání lízni tomu, kdo chtěl


##############################################################################################################################

#V Prší může dojít k situaci, kdy je lízací balíček prázdný a hrací ne. V tu chvíli je nutnost přemíchat karty:

def dojdou_karty(lizaci_balicek, odhazovaci_balicek):          
    if len(lizaci_balicek) == 0:     
        helplist = []                   #ověření prázdnosti lízacího balíčku
        
        helplist.insert(0,odhazovaci_balicek[0])
        odhazovaci_balicek.remove(odhazovaci_balicek[0])

        while len(odhazovaci_balicek) != 0:              #dokud v odhazovacím balíčku není jen jedna karta
            premichana = odhazovaci_balicek.pop()       
            lizaci_balicek.append(premichana)       #vkládej karty z hracího balíčku do lízacího, dokud není hrací prázdný

        random.shuffle(lizaci_balicek)          #zamíchej vytáhlé karty
        

        for karty in liznutelne_karty:        #OŠETŘENÍ, ŽE SE SEDMIČKY A ESO "ZNOVU-AKTIVUJÍ", jinak by byly po 1 použití 
            if karty.special != "":             #bez efektu, a to nechceme
                reset = 1
                karty.usage == reset
        
        odhazovaci_balicek.append(helplist[0])      #Vrať vrchní kartu do hracího balíčku, to zaručí i "ne-znovuaktivaci"
                                                            #V odhazovacím balíčku tak bude 1 karta.

    else:
        return

##############################################################################################################################

#LOOP S HROU

def hra_prvni_hrac(lizaci_balicek, odhazovaci_balicek, ruka_hrace, ruka_pc):
    while True:                 #Tento loop bude fungovat až do doby, než hráč či pc bude mít prázdnou ruku = konec hry
        print()
        print(mezery)
        print()

        input("Tah hráče: ")                    #Začíná hráč
        tah_hrace(lizaci_balicek, odhazovaci_balicek, ruka_hrace)        #viz tah_hrace výše

        print()
        print(mezery)
        print()

        if len(hrac) == 0 or len(pc) == 0:
                break
    
        print("TAH POČÍTAČE: ")
        print("Počet karet pc: " + str(len(pc)))            #pro uživatelský komfort, aby hráč jasně viděl, kolik má soupeř karet
        tah_pc(lizaci_balicek, odhazovaci_balicek, ruka_pc)      #viz tah_pc výše
        print("Počet karet pc po jeho tahu: " + str(len(pc)))
    
        print()
        print(mezery)
        print()
   
        if len(hrac) == 0 or len(pc) == 0:              #pokud má jeden či druhý prázdnou ruku, break loop (skonči s hrou)
                break
        
    #VYHODNOCENÍ VÝSLEDKU HRU
    if len(hrac) == 0:          #hráč má prázdnou ruku
        input("Vyhrál jste.")
    
    elif len(pc) == 0:          #pc má prázdnou ruku
        input("Vyhrál počítač.")


#OBDOBA VÝŠE UVEDENÉ FUNKCE, JEN JE PROHOZENO POŘADÍ, KDO ZAČÍNÁ PRVNÍ
#VYSVĚTLENÍ V "KDO ZAČÍNÁ?"
def hra_prvni_pc(lizaci_balicek, odhazovaci_balicek, ruka_hrace, ruka_pc):
    while True:    
        print()
        print(mezery)
        print()


        print("TAH POČÍTAČE: ")                     #Začíná pc
        print("Počet karet pc: " + str(len(pc)))
        tah_pc(lizaci_balicek, odhazovaci_balicek, ruka_pc)
        print("Počet karet pc po jeho tahu: " + str(len(pc)))

        if len(hrac) == 0 or len(pc) == 0:
                break

        print()
        print(mezery)
        print()
    
        input("Tah hráče: ")
        tah_hrace(lizaci_balicek, odhazovaci_balicek, ruka_hrace)
    
    
        print()
        print(mezery)
        print()
   
        if len(hrac) == 0 or len(pc) == 0:
                break
        
    if len(hrac) == 0:
        input("Vyhrál jste.")
    
    elif len(pc) == 0:
        input("Vyhrál počítač.")

def prsi():
      #1. Přivítání do hry, lehký grafický úvod
    print("/////////////////////////////////////////////////////4/////////")
    print("-------------------------------------------------------------")
    print("Vítejte ve hře Prší pro 1 hráče proti počítači")
    print("-------------------------------------------------------------")
    print("//////////////////////////////////////////////////////////////")

    ##############################################################################################################################

    #2. vytvoř karty, rozdej hráčům
    vytvor_balicek(liznutelne_karty, liznutelne_karty)       #viz vytvor_balicek                      


    #lizni 4 karty pro hrace, lizni 4 karty pro pc, lizni jednu kartu na vrch PlayBalicku

    start_lizani(hrac, liznutelne_karty)           #viz def start_lizani
    start_lizani(pc, liznutelne_karty)

    liznuti_vrchni_karty(hraci_balicek, liznutelne_karty)          #viz def liznuti_vrchni_karty

    ##############################################################################################################################

    #3. Kdo hru začne?  
    moznosti = ["hrac", "pc"]                   #Jednoduché random rozhodnutí, zda začne pc, či hráč
    a = random.choice(moznosti)        


    # 4. HRA
    if a == moznosti[0]:                                #random choice implementován zde
        print("Náhodným výběrem - začíná hráč.")
        hra_prvni_hrac(liznutelne_karty,hraci_balicek,hrac,pc)     
    else:          
        print("Náhodným výběrem - začíná pc.")
        hra_prvni_pc(liznutelne_karty,hraci_balicek,hrac,pc)

##############################################################################################################################
#KAPITOLA 2 -> Black Jack
##############################################################################################################################

# Definice balíčku karet
barvy_bj = ["Srdce", "Káry", "Piky", "Kříže"]
hodnosti = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Spodek", "Královna", "Král", "Eso"]
hodnoty = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Spodek": 10, "Královna": 10, "Král": 10, "Eso": 11}

# Vytvoření balíčku karet
def vytvorit_balicek():
    return [{"barva": barva, "hodnost": hodnost, "hodnota": hodnoty[hodnost]} for barva in barvy_bj for hodnost in hodnosti]

def zamichat_balicek(balicek):
    random.shuffle(balicek)
    return balicek

def rozdat_kartu(balicek):
    return balicek.pop()

def spocitat_hodnotu_ruky(ruka):
    hodnota = sum(karta['hodnota'] for karta in ruka)
    pocet_es = sum(1 for karta in ruka if karta['hodnost'] == "Eso")
    
    while hodnota > 21 and pocet_es:
        hodnota -= 10
        pocet_es -= 1
    
    return hodnota

def zobrazit_ruku(ruka, jmeno):
    print(f"{jmeno} máte v ruce:")
    for karta in ruka:
        time.sleep(0.5)
        print(f"{karta['hodnost']} {karta['barva']}")
        time.sleep(0.5)
    print(f"Celková hodnota: {spocitat_hodnotu_ruky(ruka)}\n")
    print(mezery)

def tah_hrace_bj(balicek, ruka_hrace):
    while True:
        zobrazit_ruku(ruka_hrace, "Hráč")
        volba = input("Chcete si vzít další kartu nebo zůstat? (v/z): ").lower()
        print(mezery)
        if volba == 'v':
            ruka_hrace.append(rozdat_kartu(balicek))
            if spocitat_hodnotu_ruky(ruka_hrace) > 21:
                break
        elif volba == 'z':
            break
        else:
            print("Neplatná volba. Prosím vyberte 'v' nebo 'z'.")
    return ruka_hrace

def tah_pocitaceBJ(balicek, ruka_pocitace):
    while spocitat_hodnotu_ruky(ruka_pocitace) < 17:
        ruka_pocitace.append(rozdat_kartu(balicek))
    return ruka_pocitace

def blackjack():
    zustatek = 100

    print("//////////////////////////////////////////////////////////////")
    print("-------------------------------------------------------------")
    print("Vítejte ve hře Blackjack proti počítači jako dealerovi!")
    print("-------------------------------------------------------------")
    print("//////////////////////////////////////////////////////////////")

    while zustatek > 0:
        print(f"Váš aktuální zůstatek: {zustatek} dolarů")
        print(mezery)

        # Sázka
        while True:
            sazka = int(input(f"Kolik chcete vsadit? (1-{zustatek}): "))
            if 1 <= sazka <= zustatek:
                break
            print(f"Neplatná sázka. Můžete vsadit od 1 do {zustatek} dolarů.")
        
        balicek = vytvorit_balicek()
        balicek = zamichat_balicek(balicek.copy())
        ruka_hrace = [rozdat_kartu(balicek), rozdat_kartu(balicek)]
        ruka_pocitace = [rozdat_kartu(balicek), rozdat_kartu(balicek)]
        
        print(mezery)
        print("Vítejte ve hře Blackjack!\n")
        print(mezery)

        # Tah hráče
        ruka_hrace = tah_hrace_bj(balicek, ruka_hrace)
        if spocitat_hodnotu_ruky(ruka_hrace) > 21:
            zobrazit_ruku(ruka_hrace, "Hráč")
            print("Hráč převršil 21! Počítač vyhrává.")
            print(mezery)
            zustatek -= sazka
        else:
            # Tah počítače
            ruka_pocitace = tah_pocitaceBJ(balicek, ruka_pocitace)
            zobrazit_ruku(ruka_pocitace, "Počítač")
            
            hodnota_hrace = spocitat_hodnotu_ruky(ruka_hrace)
            hodnota_pocitace = spocitat_hodnotu_ruky(ruka_pocitace)
            
            if hodnota_pocitace > 21 or hodnota_hrace > hodnota_pocitace:
                print("Hráč vyhrává!")
                print(mezery)
                zustatek += sazka
            elif hodnota_hrace < hodnota_pocitace:
                print("Počítač vyhrává!")
                print(mezery)
                zustatek -= sazka
            else:
                print("Remíza!")

        if zustatek == 0:
            print("Nemáte žádné peníze, hra končí.")
            break
        
        # Možnost odejít ze hry
        while True:
            pokracovat = input("Chcete pokračovat ve hře? (a/n): ").lower()
            if pokracovat in ['a', 'n']:
                break
            print("Neplatná volba. Prosím vyberte 'a' pro ano nebo 'n' pro ne.")
        
        if pokracovat == 'n':
            print(mezery)
            print(f"Odcházíte ze hry se zůstatkem {zustatek} dolarů. Díky za hru!")
            break

##############################################################################################################################
#KAPITOLA 3 -> Generál (hra s kostkami)
##############################################################################################################################

def hrat_hru():
    print("//////////////////////////////////////////////////////////////")
    print("-------------------------------------------------------------")
    print("Vítejte ve hře Generál!")
    print("-------------------------------------------------------------")
    print("//////////////////////////////////////////////////////////////")

    print("Pravidla: hráči hází kostkou a snaží se dosáhnout 666")
    print(mezery)

    hrac_1 = [-1, -1, -1]  # -1 znamená, že pozice je volná
    hrac_2 = [-1, -1, -1]  # -1 znamená, že pozice je volná

    #range 3 zaručí správnou délku hry
    for i in range(3):
        print(f"\n=== Kolo {i + 1} ===")

        #tah hráče 1
        print(f"Hráč 1: {' '.join([str(pozice) if pozice != -1 else 'X' for pozice in reversed(hrac_1)])}")
        input("Hráč 1, stiskněte Enter pro hod kostkou...")

        vysledek_hrac_1 = hod_kostkou()
        print(f"Hráč 1 hodil: {vysledek_hrac_1}")

        hrac_1 = vyber_pozici("Hráč 1", hrac_1, vysledek_hrac_1)
        print(f"Hráč 1: {' '.join([str(pozice) if pozice != -1 else 'X' for pozice in reversed(hrac_1)])}")
        print(mezery)

        #tah hráče 2
        print(f"Hráč 2: {' '.join([str(pozice) if pozice != -1 else 'X' for pozice in reversed(hrac_2)])}")
        input("Hráč 2, stiskněte Enter pro hod kostkou...")
        
        vysledek_hrac_2 = hod_kostkou()
        print(f"Hráč 2 hodil: {vysledek_hrac_2}")
        
        hrac_2 = vyber_pozici("Hráč 2", hrac_2, vysledek_hrac_2)
        print(f"Hráč 2: {' '.join([str(pozice) if pozice != -1 else 'X' for pozice in reversed(hrac_2)])}")
        print(mezery)

    rozhodnout_viteze(hrac_1, hrac_2)
    sys.exit() 

def hod_kostkou():
    return random.randint(1, 6)

def vyber_pozici(hrac, skore, vysledek):
    while True:
        pozice_input = input(f"{hrac}, na který řád (j/d/s pro jednotky, desítky, stovky) chcete umístit číslo? ").strip().lower()
        if pozice_input in ['j', 'd', 's', 'jednotky', 'desítky', 'stovky']:
            #pravidla pro přepisování hraných kostek hráče
            if pozice_input == 'j' or pozice_input == 'jednotky':
                if skore[0] == -1:
                    skore[0] = vysledek
                else:
                    print("Tato pozice je již obsazená. Vyberte prosím jinou.")
                    continue
            elif pozice_input == 'd' or pozice_input == 'desítky':
                if skore[1] == -1:
                    skore[1] = vysledek
                else:
                    print("Tato pozice je již obsazená. Vyberte prosím jinou.")
                    continue
            elif pozice_input == 's' or pozice_input == 'stovky':
                if skore[2] == -1:
                    skore[2] = vysledek
                else:
                    print("Tato pozice je již obsazená. Vyberte prosím jinou.")
                    continue
            break
        else:
            print("Neplatný vstup. Zadejte j, d, s nebo plné jméno (jednotky, desítky, stovky).")

    return skore

def rozhodnout_viteze(hrac_1, hrac_2):
    skore_hrac_1 = int(''.join(map(str, reversed(hrac_1))))
    skore_hrac_2 = int(''.join(map(str, reversed(hrac_2))))

    print("\n=== Konec hry ===")
    #speciální případy pro rovnou 666
    if skore_hrac_1 == 666 and skore_hrac_2 != 666:
        print("Hráč 1 se stal generálem a vyhrál hru s číslem 666!")
    elif skore_hrac_2 == 666 and skore_hrac_1 != 666:
        print("Hráč 2 se stal generálem a vyhrál hru s číslem 666!")
    else:
        print(f"Hráč 1 skóre: {skore_hrac_1}")
        print(f"Hráč 2 skóre: {skore_hrac_2}")
        print()
        if skore_hrac_1 > skore_hrac_2:
            print("Hráč 1 vyhrává!")
        elif skore_hrac_2 > skore_hrac_1:
            print("Hráč 2 vyhrává!")
        else:
            print("Remíza!")

##############################################################################################################################
#KAPITOLA 4 -> Kámen, nůžky, papír
##############################################################################################################################

#vyhodnocování výsledků
def ziskej_vysledek(volba_hrace, volba_pocitace):
    if volba_hrace == volba_pocitace:
        return "Remíza!"
    elif (volba_hrace == "Kámen" and volba_pocitace == "Nůžky") or \
         (volba_hrace == "Nůžky" and volba_pocitace == "Papír") or \
         (volba_hrace == "Papír" and volba_pocitace == "Kámen"):
        return "Vyhrál jste!"
    else:
        return "Prohrál jste!"

#zjednodušení formátu inputu pro uživatele
def normalizuj_volbu(volba):
    volba = volba.capitalize()
    if volba == 'K' or volba == 'Kámen':
        return 'Kámen'
    elif volba == 'N' or volba == 'Nůžky':
        return 'Nůžky'
    elif volba == 'P' or volba == 'Papír':
        return 'Papír'
    else:
        return None

#herní funkce
def kamen_nuzky_papir():
    volby = ["Kámen", "Nůžky", "Papír"]
    skore_hrac_1 = 0
    skore_hrac_2 = 0

    print("//////////////////////////////////////////////////////////////")
    print("-------------------------------------------------------------")
    print("Vítejte ve hře Kámen, nůžky, papír proti počítači!")
    print("-------------------------------------------------------------")
    print("//////////////////////////////////////////////////////////////")
    
    while True:
        try:
            #nastavitelné množství kol k výhře
            vyherni_body = int(input("Zadejte počet bodů potřebných k výhře: "))
            print(mezery)
            if vyherni_body <= 0:
                raise ValueError
            break
        except ValueError:
            print("Zadejte platné číslo větší než 0.") 
    
    while skore_hrac_1 < vyherni_body and skore_hrac_2 < vyherni_body:
        print(f"Skóre: Hráč - {skore_hrac_1}, Počítač - {skore_hrac_2}")
        print(mezery)
        volba_hrace = input("Zadejte svou volbu (Kámen/K, Nůžky/N, Papír/P nebo Konec): ").capitalize()
        print(mezery)
        
        if volba_hrace == "Konec":
            break
        
        volba_hrace = normalizuj_volbu(volba_hrace)
        
        #projde dál jen když hráč vybere validní možnost
        if volba_hrace not in volby:
            print("Neplatná volba, zkuste to znovu.")
            continue
        
        volba_pocitace = random.choice(volby)
        
        #sleep vytvoří lepší čitelnost pro hráče
        time.sleep(0.5)
        print(f"Počítač zvolil: {volba_pocitace}")
        print(mezery)
        time.sleep(0.5)
        
        vysledek = ziskej_vysledek(volba_hrace, volba_pocitace)
        time.sleep(0.3)
        print(vysledek)
        print(mezery)
        
        #update skóre hráče/pc
        if vysledek == "Vyhrál jste!":
            skore_hrac_1 += 1
        elif vysledek == "Prohrál jste!":
            skore_hrac_2 += 1

    print(f"Závěrečné skóre: Hráč - {skore_hrac_1}, Počítač - {skore_hrac_2}")
    if skore_hrac_1 == vyherni_body:
        print("KONEC HRY")
        print(mezery)
        print("Jste ultimátním vítězem!")
    elif skore_hrac_2 == vyherni_body:
        print("KONEC HRY")
        print(mezery)
        print("Byl jste poražen počítačem!")

    sys.exit()

##############################################################################################################################
#KAPITOLA 5 -> Testování odhadu!
##############################################################################################################################

def klikni_na_casovac():
    print("//////////////////////////////////////////////////////////////")
    print("-------------------------------------------------------------")
    print("Vítejte u krátkého testu odhadu na dobu!")
    print("-------------------------------------------------------------")
    print("//////////////////////////////////////////////////////////////")

    #nastav cílový čas, přepíše se všude, kde je potřeba
    cilovy_cas = 5.5

    #inicializace na -1, 0 by znamenala rovnou perfektní výsledek, což nechceme
    hracovo_nej_skore = -1

    while True:
        print(mezery)
        print("Klikněte na tlačítko co nejpřesněji blízko " + str(cilovy_cas) + " sekund!")
        input("Stiskněte Enter pro spuštění časovače...")
        print(mezery)
        
        start_cas = time.time()
        input("Stiskněte Enter znovu po 5,5 sekundách...")
        print(mezery)
        end_cas = time.time()
        
        uplynuly_cas = end_cas - start_cas
        herni_cas = cilovy_cas - uplynuly_cas

        #ošetření záporných čísel, rozdíl do mínusu i do plusu budu brát jako "netrefení" se o stejnou míru
        if herni_cas < 0:
            herni_cas = herni_cas * -1
        
        print(f"Cílový čas: {cilovy_cas:.2f} sekund")
        print(f"Váš čas: {uplynuly_cas:.2f} sekund (rozdíl o {herni_cas:.2f} oproti {cilovy_cas:.2f})")
        print(mezery)

        #sleep zde vylepší čitelnost pro uživatele
        time.sleep(0.5)

        #hodnocení výsledku uživatele
        if herni_cas <= 0.2:
            print("Úžasné!")
        elif herni_cas < 0.25:
            print("Velmi dobře!")
        elif herni_cas < 0.5:
            print("To již celkem ujde!")
        elif herni_cas < 1:
            print("Blížíte se slušnému výsledku!")
        elif herni_cas == 0:
            print("To snad není ani možné, gratulujeme!")
        else:
            print("To bylo hodně mimo, zkuste to znovu...")

        time.sleep(0.5)

        #práce s prvním kolem
        if hracovo_nej_skore != -1:
            print(mezery)
        else:
            hracovo_nej_skore = herni_cas
            print("Vaše první hra, získáváte highscore přesnosti k cílovému času!")

        #podmínka přepisu highscore na lepší
        if herni_cas < hracovo_nej_skore:
            print("Překonal(a) jste své původní skóre z " + str(hracovo_nej_skore) + " na " + str(herni_cas) + "!")
            hracovo_nej_skore = herni_cas
        elif herni_cas == hracovo_nej_skore:
            continue
        else:
            print("Bohužel jste své předchozí nejlepší skóre nepřekonali.")
        
        #volba hrát znovu či skončit
        volba = input("Chcete hrát znovu? (ano/ne): ").strip().lower()
        if volba != "ano":
                print("Odcházíte ze hry s výsledkem přesnosti " + str(hracovo_nej_skore) + " vůči cílovému času " + str(cilovy_cas) + " sekund!")
                break
        
    sys.exit()


##############################################################################################################################
#KAPITOLA 6 -> HOD MINCÍ
##############################################################################################################################

def hodit_mince():
    # Funkce pro hod mincí - orel je 0, panna je 1
    return random.choice(["orel", "panna"])

def vybrat_stranu():
    while True:
        vyber = input("Vyberte si (o)rel nebo (p)anna: ").strip().lower()
        if vyber in ['o', 'p', 'orel', 'panna']:
            return 'orel' if vyber in ['o', 'orel'] else 'panna'
        else:
            print("Neplatný vstup. Zadejte 'o' pro orel nebo 'p' pro panna.")

def panna_nebo_orel():

    print("//////////////////////////////////////////////////////////////")
    print("-------------------------------------------------------------")
    print("PANNA NEBO OREL?")
    print("-------------------------------------------------------------")
    print("//////////////////////////////////////////////////////////////")
    print(mezery)

    vyber_hrace = vybrat_stranu()
    vyber_pocitace = 'panna' if vyber_hrace == 'orel' else 'orel'
    
    print(f"Vybral jste si: {vyber_hrace}")
    print()
    print(f"Počítač si vybral: {vyber_pocitace}")
    
    print("\nHázím mincí...")
    time.sleep(random.uniform(0.9, 1.9))  # Pauza mezi 0,5 a 1,2 sekundami

    vysledek = hodit_mince()
    print((vysledek).upper())
    print()
    time.sleep(0.5)
    
    if vysledek == vyber_hrace:
        print("Hráč vyhrál!")
    else:
        print("Počítač vyhrál!")
    
    sys.exit()

##############################################################################################################################
#KAPITOLA POSLEDNÍ -> VOLBA HRY
##############################################################################################################################

#volba her
def hraj_prsi():
    prsi()

def hraj_blackjack():
    blackjack()

def hraj_generala():
    hrat_hru()

def hraj_k_n_p():
    kamen_nuzky_papir()

def p_n_o():
    panna_nebo_orel()

volba_hry = ""
while volba_hry not in ["0", "1", "2", "3", "4", "5"]:
    print("/////////////////////////////////////////////////////4/////////")
    print("-------------------------------------------------------------")
    print(" ! KNIHOVNA MNOHA RŮZNORODÝCH HER VÁS VÍTÁ ! ")
    print("-------------------------------------------------------------")
    print("//////////////////////////////////////////////////////////////")

    print("Zadejte číslo nebo název hry:")
    print("1 = Prší | 2 = Black Jack (BJ) | 3 = Generál | 4 = Kámen, nůžky, papír | 5 = Reflex | 6 = Mince | 0 = konec")
    
    volba_hry = input()

    #využití novější funkcionality match case
    match volba_hry:
        case "1" | "Prší" | "Karty":
            hraj_prsi()
        case "2" | "BJ" | "Black Jack":
            hraj_blackjack()
        case "3" | "Generál" | "666":
            hraj_generala()
        case "4" | "knp":
            hraj_k_n_p()
        case "5" | "reflex":
            klikni_na_casovac()
        case "6" | "Mince":
            p_n_o()
        case "0" | "q" | "konec":
            print("Ukončuji hru...")
        case _:
            print("Zadejte jednu z možností prosím.")
            print()

##############################################################################################################################
