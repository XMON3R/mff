import random                    #z modulu random použity funkce jako random.choice (Kdo začne?) či random.shuffle (michání karet)

##############################################################################################################################
#KAPITOLA 1 -> URČENÍ POČÁTEČNÍCH DATOVÝCH TYPŮ  
##############################################################################################################################                      

barvy = ["SRDCE", "KULE", "LISTY", "ŽALUDY"]                        #Jednotlivé barvy karet v seznamu                                      
typ = ["7","8","9","10","SPODEK","SVRŠEK","KRÁL","ESO"]             #Jednotlivé typy karet v seznamu

hrac = []               #seznam živého hráče (INPUT)
pc = []                 #seznam karet počítače, který bude random volit 

Liznutelne_Karty = []          #seznam pro všechny karty, kam se na začátku vytvoří balíček jako takový, 
                                #lízne se z něj 8 karet pro hráče a jedna, na kterou se bude hrát

# global PlayBalicek

PlayBalicek = []                #na tento balíček se bude hrát 

#Seznamy jsem vybral z toho důvodu, že se s nimi dobře pracuje a jsou ideální např. pro funkci VytvorBalicek níže.

##############################################################################################################################
#KAPITOLA 2 -> CLASS a FUNKCE
##############################################################################################################################

class karta:                                            #CLASS POUŽÍVÁN NA URČENÍ BARVY A TYPU
    def __init__(self, barva, typ, special,usage):
        self.barva = barva      #reprezentace barvy                                  
        self.typ = typ          #reprezentace typu
        self.special = special  #reprezentace toho, zda je karta speciální (7 či ESO, či ne)
        self.usage = usage      #USAGE je používán pro zjištění, zda je karta "aktivní", či ne u 7ček a ES 
                                    # -> pokud je USAGE 0, již není potřeba stát ani lízat, pokud 1 - efekt platí

#použití Classu jsem zvolil především pro zjednodušené porovnávání karet (viz funkce níže).

##############################################################################################################################

#FUNKCE NA VYTVOŘENÍ BALÍČKU KARET

def VytvorBalicek(self, balicek):
    for i in barvy:      #Každé i ze seznamu "barvy" kombinuji s každou ze 4 barev, tedy s každým j ze seznamu "typ".
        for j in typ:  
            nejaka_karta = (i,j)        #Ukládám jako tuple především kvůli zjednodušení práce.
            
            if j == "7" or j == "ESO":                      #Toto mi zaručí jednodušší kontrolu 7 a ES skrze volání otázky, zda 
                                                            #je USAGE 0 či ne                
                nejaka_karta = karta(barva = i, typ = j, special = "->" + str(j) + "<-", usage = 1)        
            
            else:
                nejaka_karta = karta(barva = i, typ = j, special = "", usage = 0) 
            
            self.append(nejaka_karta)   
    random.shuffle(balicek)                         #příkaz random.shuffle zaručí zamíchání seznamu karet po jeho vytvoření


##############################################################################################################################

#FUNKCE NA ZOBRAZOVÁNÍ KARET PRO UŽIVATELE 
#Vzhledem k tomu, že jsem z karet udělal objekty typu class, tak pro jejich "racionální" zobrazení uživateli nyní potřebuji
#jednoduchou funkci pro zobrazení karet tak, jak je sami vnímáme při hraní Prší v reálném světě.

def DisplayCard(karta):                         #vytiskni danou kartu
    print(karta.barva + " " + karta.typ)        #v printu zkombinuj barvu a typ (např. "SRDCE ESO")
    print()

def DisplayDeck(balicek):                       #vytiskni celý daný balíček (může být i ruka hráče), formát jako DisplayCard
    for x in balicek:                    #Velmi podobný princip jako u DisplayCard, for cyklus zajišťuje tisk celého seznamu.
        print(x.barva + " " + x.typ + " " + x.special)
    print()


#Funkce DisplayPlayer vznikla jako zjednodušení pro uživatele, aby viděl, která karta má jaké číslo. Pro intuitivnost a pro 
#hráče nepolíbené informací, jak funguje indexování v počítači, začínají čísla 1, ne 0 (jako to dělá počítač)**.

def DisplayPlayer(balicek):                       #vytiskni celý daný balíček (může být i ruka hráče), formát jako DisplayCard
    for x in balicek:
        print(balicek.index(x)+1, x.barva + " " + x.typ)        #** to je zaručeno zde, v "balicek.index(x)+´1´"
    print()                                                

##############################################################################################################################

#NALÍZEJ DANÝ POČET KARET DO RUKY HRÁČE
#POUŽITO NA POČÁTKU KAPITOLY "HRA"

def StartLizani(balicek, Lizaci_balicek):           #balicek reprezentuje ruku daného hráče
    StartPocet = 4                  #Tato proměnná nám ulehčí případnou změnu počátečního lízání pro hráče -  jen přepíšu číslo
    for i in range(StartPocet):
        balicek.append(Lizaci_balicek.pop())        #funkci pop používám pro zjednodušení přemisťování karet
                                                        #z Liznutelnych karet dávám do balíčku

#nahodne vyber jednu kartu z balicku, na kterou se zacne hrat
def NaLiznutiTopCard(hraci_balik, lizaci_balik):                        #Pomocí pop z lizacího balíčku vytáhne jednu kartu
    if lizaci_balik[0].typ == "SVRŠEK":           #Pokud je vytažená vrchní karta, vezmi barvu spodní karty Lízacího balíčku
        lizaci_balik[0].barva = lizaci_balik[-1].barva
    hraci_balik.append(lizaci_balik.pop())                              

def DisplayTopCard(balicek):       #UKAŽ TOPCARD, podobné jako u DisplayCard, funkce spíše pro přehlednost
    DisplayCard(balicek[0])                                            #zobrazí vrchní kartu hracího balíčku 

##############################################################################################################################

#FUNKCE NA VYBRÁNÍ KARTY A KONTROLU, ZDA JDE ZAHRÁT 
#VERZE: HRÁČ

def VybraniKarty(SeznamKaret, hraci_balicek, Lizaci_balicek):
        chosen_card = 0         #na počátku 0

    #While loop zaručuje držení hráče do té doby, dokud nenapíše validní číslo karty viditelné v DisplayPlayer, či zvolí lízání
        while True:   
            try:
                #int -> číselný inputu, v případě, že by uživatel zadal znaky (str), tak je zde except ValueError
                chosen_card = int(input("Napište sem číslo vámi zvolené karty. Pokud jste si to rozmyslel a radši byste lízl kartu, napiště 0: ")) - 1

                #chosen_card reprezentuje vybranou kartu, používáno pro CardPlayability níže 
            
            except ValueError:
                print("Nezadávejte prosím znaky.")                      #při špatném hráč-inputu program nespadne
                VybraniKarty(SeznamKaret, hraci_balicek, Lizaci_balicek)

            if chosen_card >= len(hrac):                            #pochopitelné z obsahu printu                                                
                print("Zadejte prosím maximálně tak velké číslo, které odpovídá počtu karet ve Vaší ruce.")
                VybraniKarty(SeznamKaret, hraci_balicek, Lizaci_balicek)

            elif chosen_card < -1:                                                #pochopitlné z obsahu printu
                print("Zadejte prosím minimálně číslo 0 pro líznutí a 1 pro zahrání.")
                VybraniKarty(SeznamKaret, hraci_balicek, Lizaci_balicek)

            elif chosen_card == -1:                       #-1, kvůli chosen_card = int(input)-1 
                print("Zvolil jste lízání.")   
                Lizni(SeznamKaret, Lizaci_balicek)      #Viz Lízni 
                break

            else:
                break
        
        if chosen_card == -1:
            return

        TopCard = PlayBalicek[0]            #TopCard reprezentuje vrchni kartu hracího balíčku

        CardPlayability(TopCard, SeznamKaret, Lizaci_balicek, hraci_balicek, chosen_card)   #viz CardPlayabality 
        return

##############################################################################################################################
#############################################################################################################################

#JAK FUNGUJÍ TAHY HRÁČE A TAHY POČÍTAČE?

def TahHrace(Lizaci_balicek, hraci_balicek, ruka_hrace):

    print("Vaše karty:")                                        #Na začátku zobrazím hráči karty, které má v ruce.
    DisplayPlayer(ruka_hrace)

    print("")
    print("Karta, na kterou hrajete:")                          #Následně mu zobrazím kartu, na kterou se hraje.
    DisplayTopCard(hraci_balicek)
    TopCard = hraci_balicek[0]
                                                                #Poté zkontroluji, zda se jedná o 7 či eso.

    #POKUD SE JEDNÁ O 7:                                                            
    if TopCard.typ == "7" and TopCard.usage == 1:                  
        input("Na stole leží sedmička, lízněte 2 karty.")       
        a = 0
        hraci_balicek[0].usage = a    #vynulování USAGE (viz class karta), aby tato sedmička neplatila pro dalšího hráče
        for i in range(2):
            Lizni(ruka_hrace, Lizaci_balicek)               #Lizní dvě karty (viz funkce Lízni)
        return                                     #return, aby se již dále nepokračovalo = hráč přichází správně o tah

    #POKUD SE JEDNÁ O ESO:
    elif TopCard.typ == "ESO" and TopCard.usage == 1:       #Funguje velmi podobně jako kontrola 7 včetně vynulování USAGE.
        input("Na stole leží eso, nehraješ.")
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
            volba = input("Napište prosím svou volbu: ")
        
            if volba == zahrat_kartu:
                VybraniKarty(ruka_hrace, hraci_balicek, Liznutelne_Karty)    #vysvětlení viz VybraniKarty
                return
        
            elif volba == liznout_kartu:                                   #vysvětlení viz Lízni
                Lizni(ruka_hrace, Liznutelne_Karty)
                return
        
            else:                                            #Pokud hráč nevybral nic správně, tak se loop opakuje.
                print("---------------------------")
                TahHrace(Lizaci_balicek, hraci_balicek, ruka_hrace)         #volání funkce znovu
                return            

##############################################################################################################################           

def TahPC(Lizani, hrani, ruka_pc):            #velmi podobné jako TahHrace, jen bez inputů a printů
    
    TopCard = hrani[0]

    if TopCard.typ == "7" and TopCard.usage == 1:    
        print("Na stole leží (aktivní) 7mička, počítač líže 2 karty.")               
        for i in range(2):
            Lizni(ruka_pc, Lizani)
        a = 0
        hrani[0].usage = a                                      #VYNULOVÁNÍ, ABY EFEKT JIŽ NEPLATIL 
        return

    elif TopCard.typ == "ESO" and TopCard.usage == 1:
        print("Na stole leží (aktivní) Eso, počítač stojí.")
        a = 0
        hrani[0].usage = a                                   #VYNULOVÁNÍ, ABY EFEKT JIŽ NEPLATIL 
        return

    else:
        VybraniKartyPC(ruka_pc, Lizani, hrani)              #viz VybraniKartyPC


##############################################################################################################################

def CardPlayability(Karta_playing, SeznamKaret, Lizaci_balicek, Hraci_balicek, chosen_card):
    #1. MOŽNOST
    #karta se shoduje v barvě či v typu

    #kontrola zvolené karty se současnou TopCard, na kterou se hraje
    if Karta_playing.barva == SeznamKaret[chosen_card].barva or Karta_playing.typ == SeznamKaret[chosen_card].typ:      

        if SeznamKaret[chosen_card].typ == "SVRŠEK":                #Kontrola, zda je chosen_card SVRŠEK
            a = ""
            input("Zahrál jste svrška. Zvolte prosím novou barvu.")         #Zvolení nové barvy
            while a not in barvy:                   #Loop dokud uživatel dobře nezadá barvu
                a = input("Vyberte novou barvu: ")
            SeznamKaret[chosen_card].barva = a                          #změna barvy karty

        Hraci_balicek.append(SeznamKaret[chosen_card])      #Zahraje vybranou kartu do PlayBalicku na index 0
        SeznamKaret.remove(SeznamKaret[chosen_card])            #následně tuto kartu odebere z ruky hráče
        Hraci_balicek.reverse()                         #zaručí, že přidá karta bude na indexu 0

        input("Zahrál jste kartu. Na tahu je soupeř (stisknutím tlačítka bude hra pokračovat).")
        print("---------------------")



    #2. MOŽNOST 
    #karta se shoduje v barvě i typu (případ svrška)
    elif Karta_playing.barva == SeznamKaret[chosen_card].barva and Karta_playing.typ == SeznamKaret[chosen_card].typ:  

        if SeznamKaret[chosen_card].typ == "SVRŠEK":
            a = ""
            input("Zahrál jste svrška. Zvolte prosím novou barvu.")
            while a not in barvy:
                a = input("Vyberte novou barvu: ")
            SeznamKaret[chosen_card].barva = a 
    
        else: #klasika
            print("Kartu lze zahrát.")                                  #FUNGUJE stejně, viz výše

        Hraci_balicek.append(SeznamKaret[chosen_card])      #Zahraje vybranou kartu do PlayBalicku na index 0
        SeznamKaret.remove(SeznamKaret[chosen_card])            #následně tuto kartu odebere z ruky hráče
        Hraci_balicek.reverse()
        
       
        input("Zahrál jste kartu. Na tahu je soupeř (stisknutím tlačítka bude hra pokračovat).")
        print("---------------------")
    

    #3. MOŽNOST, NELZE ZAHRÁT TUTO KARTU
    else:       
        if SeznamKaret[chosen_card].typ == "SVRŠEK":  #svršek je výjimka, jde zahrát kdykoliv (případ esa a 7 ošetřen již dříve)
            a = ""
            input("Zahrál jste svrška. Zvolte prosím novou barvu.")
            while a not in barvy:
                a = input("Vyberte novou barvu: ")                              
            SeznamKaret[chosen_card].barva = a 

            Hraci_balicek.append(SeznamKaret[chosen_card])      #Zahraje vybranou kartu do PlayBalicku na index 0
            SeznamKaret.remove(SeznamKaret[chosen_card])            #následně tuto kartu odebere z ruky hráče
            Hraci_balicek.reverse()
    

        else: 
            print("Zvolená karta nelze zahrát.")
            VybraniKarty(SeznamKaret, Hraci_balicek, Lizaci_balicek)    #pokud karta nelze zahrát, uživatel znovu vybírá kartu      #FUNGUJE stejně, viz výše

##############################################################################################################################

#FUNKCE NA VYBRÁNÍ KARTY A KONTROLU, ZDA JDE ZAHRÁT 
#VERZE: PC

def VybraniKartyPC(SeznamKaret, Lizaci_balik, Hraci_balicek):     #skoro stejné jako VybraniKarty u hráče, jen bez inputů 

        def NeniNutneLiznout(SeznamKaret, TopCard):         #speciální funkce na zhodnocení, zda počítač může něco zahrát
            check = 0
            for karty in SeznamKaret:
                if (karty.barva == TopCard.barva and karty.typ == TopCard.typ) or (karty.barva == TopCard.barva or karty.typ == TopCard.typ):
                    check = check + 1                  #check pak reprezentuje počet zahratelných karet
            
            #případ, kdy check není 0:
            if check != 0:
                chosen_card = random.randint(0,len(pc)-1)               #počítač vybere náhodnou hratelnou kartu
                CardPlayabilityPC(TopCard, SeznamKaret, Lizaci_balik, Hraci_balicek, chosen_card)   #viz CardPlayabilityPC

            #případ, kdy check je 0:
            elif check == 0:
                Lizni(pc, Liznutelne_Karty)                 #Viz Lízni 
                print("Počítač si líznul. Jste na řadě.")


        def CardPlayabilityPC(Karta_playing, SeznamKaret, Lizaci_balik, Hraci_balik, chosen_card):
            #kontrola zvolené karty se současnou TopCard, na kterou se hraje 
            if Karta_playing.barva == SeznamKaret[chosen_card].barva or Karta_playing.typ == SeznamKaret[chosen_card].typ:     
                
                if SeznamKaret[chosen_card].typ == "SVRŠEK":
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
                
                    SeznamKaret[chosen_card].barva = barvy[max_index]                   #zahrání ideální barvy

                Hraci_balik.append(SeznamKaret[chosen_card])      #Zahraje vybranou kartu do PlayBalicku na index 0
                SeznamKaret.remove(SeznamKaret[chosen_card])            #následně tuto kartu odebere z ruky hráče
                Hraci_balik.reverse()

                print("PC zahrál kartu. Jste na řadě.")
                print("---------------------")
       
            elif Karta_playing.barva == SeznamKaret[chosen_card].barva and Karta_playing.typ == SeznamKaret[chosen_card].typ:  
                if SeznamKaret[chosen_card].typ == "SVRŠEK":
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
                
                    SeznamKaret[chosen_card].barva = barvy[max_index]
    
                Hraci_balik.append(SeznamKaret[chosen_card])      #Zahraje vybranou kartu do PlayBalicku na index 0
                SeznamKaret.remove(SeznamKaret[chosen_card])            #následně tuto kartu odebere z ruky hráče
                Hraci_balik.reverse()

                print("PC zahrál kartu. Jste na řadě.")
                print("---------------------")
                
            else:   
                if SeznamKaret[chosen_card].typ == "SVRŠEK":
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
                
                    SeznamKaret[chosen_card].barva = barvy[max_index]
    
                    Hraci_balik.append(SeznamKaret[chosen_card])      #Zahraje vybranou kartu do PlayBalicku na index 0
                    SeznamKaret.remove(SeznamKaret[chosen_card])            #následně tuto kartu odebere z ruky hráče
                    Hraci_balik.reverse()

                    print("PC zahrál kartu. Jste na řadě.")
                    print("---------------------")
                
                else:
                    VybraniKartyPC(SeznamKaret, Lizaci_balik, Hraci_balik)


        TopCard = PlayBalicek[0] 

        NeniNutneLiznout(SeznamKaret, TopCard)      #volání výše definové funkce, kontrola, zda se musí lízat, či ne

##############################################################################################################################
def CoKdyzDojdouKartTEST(Lizaci_balicek, Odhazovaci_balicek):  
    helplist = []                       #pomocný list na uložení vrchní karty, na kterou se bude i nadále hrát
    helplist.insert(0,Odhazovaci_balicek[0])    #vložení vrchní karty
    Odhazovaci_balicek.remove(Odhazovaci_balicek[0])    #odebrání vrchní karty z hracího balíčku (aby nebyl duplikát)

    while len(Odhazovaci_balicek) != 0:              #dokud v odhazovacím balíčku není jen jedna karta
        premichana = Odhazovaci_balicek.pop()       
        Lizaci_balicek.append(premichana)       #vkládej karty z hracího balíčku do lízacího, dokud není hrací prázdný

        random.shuffle(Lizaci_balicek)          #zamíchej vytáhlé karty
        

    for karty in Liznutelne_Karty:        #OŠETŘENÍ, ŽE SE SEDMIČKY A ESO "ZNOVU-AKTIVUJÍ", jinak by byly po 1 použití 
        if karty.special != "":             #bez efektu, a to nechceme
            reset = 1
            karty.usage == reset
        
    Odhazovaci_balicek.append(helplist[0])      #Vrať vrchní kartu do hracího balíčku, to zaručí i "ne-znovuaktivaci"
                                                            #V odhazovacím balíčku tak bude 1 karta.

##############################################################################################################################

#LIZÁNÍ

def Lizni(balicek_kam, balicek_odkud):                                     
    if balicek_odkud != []:                                #if, aby se mi nemohlo stát, že bude lízat z NIČEHO 
        balicek_kam.append(balicek_odkud.pop())                         #balicek odkud je lízací balíček
                                                                        #balicek kam je ruka hráče či pc
    
    #Ošetření případu, kdy je lízací balíček prázdný, ale nikdo nezahrál kartu
    elif Liznutelne_Karty == [] and len(PlayBalicek) == 1:   
        print("Není z čeho lízat a ani přemíchat, zahraj kartu.")
        VybraniKarty(balicek_kam,PlayBalicek,balicek_odkud)
        return
    
    #Nutnost přemíchání balíčku jako v "reálném" Prší
    elif Liznutelne_Karty == [] and len(PlayBalicek) != 1:     #pokud je lizácí balíček prázdný a je odehráno více než 1 karet
        print("Není z čeho lízat, přemíchávám balíček.")
        CoKdyzDojdouKartTEST(balicek_odkud, PlayBalicek)       #Viz CoKdyzDojdouKarty níže 
        Lizni(balicek_kam, balicek_odkud)                   #po přemíchání lízni tomu, kdo chtěl


##############################################################################################################################

#V Prší může dojít k situaci, kdy je lízací balíček prázdný a hrací ne. V tu chvíli je nutnost přemíchat karty:

def CoKdyzDojdouKarty(Lizaci_balicek, Odhazovaci_balicek):          
    if len(Lizaci_balicek) == 0:     
        helplist = []                   #ověření prázdnosti lízacího balíčku
        
        helplist.insert(0,Odhazovaci_balicek[0])
        Odhazovaci_balicek.remove(Odhazovaci_balicek[0])

        while len(Odhazovaci_balicek) != 0:              #dokud v odhazovacím balíčku není jen jedna karta
            premichana = Odhazovaci_balicek.pop()       
            Lizaci_balicek.append(premichana)       #vkládej karty z hracího balíčku do lízacího, dokud není hrací prázdný

        random.shuffle(Lizaci_balicek)          #zamíchej vytáhlé karty
        

        for karty in Liznutelne_Karty:        #OŠETŘENÍ, ŽE SE SEDMIČKY A ESO "ZNOVU-AKTIVUJÍ", jinak by byly po 1 použití 
            if karty.special != "":             #bez efektu, a to nechceme
                reset = 1
                karty.usage == reset
        
        Odhazovaci_balicek.append(helplist[0])      #Vrať vrchní kartu do hracího balíčku, to zaručí i "ne-znovuaktivaci"
                                                            #V odhazovacím balíčku tak bude 1 karta.

    else:
        return

##############################################################################################################################

#LOOP S HROU

def Hra_FirstPlayer(lizaci_balicek, odhazovaci_balicek, ruka_hrace, ruka_pc):
    while True:                 #Tento loop bude fungovat až do doby, než hráč či pc bude mít prázdnou ruku = konec hry
        print()
        print("---------------")
        print()

        input("Tah hráče: ")                    #Začíná hráč
        TahHrace(lizaci_balicek, odhazovaci_balicek, ruka_hrace)        #viz TahHrace výše

        print()
        print("---------------")
        print()

        if len(hrac) == 0 or len(pc) == 0:
                break
    
        print("TAH POČÍTAČE: ")
        print("Počet karet pc: " + str(len(pc)))            #pro uživatelský komfort, aby hráč jasně viděl, kolik má soupeř karet
        TahPC(lizaci_balicek, odhazovaci_balicek, ruka_pc)      #viz TahPC výše
        print("Počet karet pc po jeho tahu: " + str(len(pc)))
    
        print()
        print("---------------")
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
def Hra_FirstPC(lizaci_balicek, odhazovaci_balicek, ruka_hrace, ruka_pc):
    while True:    
        print()
        print("---------------")
        print()


        print("TAH POČÍTAČE: ")                     #Začíná pc
        print("Počet karet pc: " + str(len(pc)))
        TahPC(lizaci_balicek, odhazovaci_balicek, ruka_pc)
        print("Počet karet pc po jeho tahu: " + str(len(pc)))

        if len(hrac) == 0 or len(pc) == 0:
                break

        print()
        print("---------------")
        print()
    
        input("Tah hráče: ")
        TahHrace(lizaci_balicek, odhazovaci_balicek, ruka_hrace)
    
    
        print()
        print("---------------")
        print()
   
        if len(hrac) == 0 or len(pc) == 0:
                break
        
    if len(hrac) == 0:
        input("Vyhrál jste.")
    
    elif len(pc) == 0:
        input("Vyhrál počítač.")


##############################################################################################################################
#KAPITOLA 3 -> HRA
##############################################################################################################################


#1. Přivítání do hry, lehký grafický úvod
print("//////////////////////////////////////////////////////////////")
print("-------------------------------------------------------------")
print("Vítejte ve hře Prší pro 1 hráče proti počítači\n")
print("-------------------------------------------------------------")
print("//////////////////////////////////////////////////////////////")

##############################################################################################################################

#2. vytvoř karty, rozdej hráčům
VytvorBalicek(Liznutelne_Karty, Liznutelne_Karty)       #viz VytvorBalicek                      


#Lizni 4 karty pro hrace, lizni 4 karty pro pc, lizni jednu kartu na vrch PlayBalicku

StartLizani(hrac, Liznutelne_Karty)           #viz def StartLizani
StartLizani(pc, Liznutelne_Karty)

NaLiznutiTopCard(PlayBalicek, Liznutelne_Karty)          #viz def NaliznutiTopCard

##############################################################################################################################

#3. Kdo hru začne?  
moznosti = ["hrac", "pc"]                   #Jednoduché random rozhodnutí, zda začne pc, či hráč
a = random.choice(moznosti)        


# 4. HRA
if a == moznosti[0]:                                #random choice implementován zde
    print("Náhodným výběrem - začíná hráč.")
    Hra_FirstPlayer(Liznutelne_Karty,PlayBalicek,hrac,pc)     
else:          
    print("Náhodným výběrem - začíná pc.")
    Hra_FirstPC(Liznutelne_Karty,PlayBalicek,hrac,pc)

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################