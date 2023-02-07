def Sugu(isikukod_list:list)->str:
    """Esimise tahe järgi määrame sugu
    :param list ik_list: Järjend isikukoodi numbridest
    :rtype: str
    """
    if int(isikukod_list[0])%2==0:
        sugu="naine"
    else:
        sugu="mees"
    return sugu

def Sunnikoht(a:int)->str:
    """
    """
    if 1<=a<=10:
         haigla="kuresaare Haigla"
    elif 11<=a<=19:
         haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21<=a<=220:
         haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 271<=a<=310:
         haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371<=a<=420:
         haigla="Narva Haigla"
    elif 421<=a<=470:
         haigla="Pärnu Haigla"
    elif 471<=a<=490:
         haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491<=a<=520:
        haigla="Järvamaa Haigla (Paide)"
    elif 521<=a<=570:
        haigla="Rakvere, Tapa haigla"
    elif 571<=a<=600:
        haigla="Valga Haigla"
    elif 601<=a<=650:
        haigla="Viljandi Haigla"
    elif 651<=a<=700:
        haigla="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    return haigla

def Sunnipaev(isikukod_list:list)->str:
     """määrme spaev
     :parem str ik: Järjend spaev
     :rtype: str
     """
     s1=int(isikukod_list[0])
     y=isikukod_list[1]+isikukod_list[2] #aasta
     m=isikukod_list[3]+isikukod_list[4] #kuu
     d=isikukod_list[5]+isikukod_list[6] #päev
   
     if int(m)<1 or int(m)>13 and int(d)<1 or int(d)>31:
         spaev="Viga"
     else:
         if s1==1 or s1==2:
             yy="18"
         elif s1==3 or s1==4:
             yy="19"
         else:
             yy="20"
         spaev=d+"."+m+"."+yy+y
         return spaev

def naised_mehed(ikoodid:list):
    """
    :rtype list
    """
    naised=[]
    mehed=[]
    for kood in ikoodid:
        isikukod_list=list(kood)
        sugu=Sugu(isikukod_list)
        if sugu=="naine":
            naised.appemd(kood)
        else:
            mehed.append(kood)
    ikoodid.clear()
    ikoodid.extend(naised)
    ikoodid.extend(naised)
    ikoodid.exted(mehed)



