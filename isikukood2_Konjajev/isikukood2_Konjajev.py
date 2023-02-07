from math import *
from oma1 import *
isikukod=[]
arvud=[]
isikukoodid=[]

while True:
    isikukod=input("Kirjutage tei isikukood: ") #str´
    if isikukod=="1": break
    if isikukod.isalpha():
        print("Viga")
    n=len(isikukod)
    if len(isikukod)!=11:
        print("Liiga palju või liiga vähe sümboleid või lubamatud väärtused. Proovige veel kord:")
        arvud.append(isikukod)
    if isikukod.isalpha():
        print("Viga")
    else:
        print("Isikukoodi kontroll")
        isikukod_list=list(isikukod)
        s1=int(isikukod_list[0]) #"1"->1
        print("Esimene number on" ,isikukod_list[0] )
        if s1 not in [1,2,3,4,5,6]:
            print("Esimene sümbol ei ole õige!")
            arvud.append(isikukod)
        else:
            print("Esimene sümbol on õige")
            spaev=Sunnipaev(isikukod_list)
            if spaev=="Viga":
                arvud.append(isikukod)
            else:
                #
                print(f"Sünnipäev on {spaev}")
                print(f"Viimane number: {isikukod_list[-1]}")
                kontrollnr=0
                a1=int(isikukod[0])*1
                b1=int(isikukod[1])*2
                b2=int(isikukod[2])*3
                b3=int(isikukod[3])*4
                b4=int(isikukod[4])*5
                b5=int(isikukod[5])*6
                b6=int(isikukod[6])*7
                b7=int(isikukod[7])*8
                b8=int(isikukod[8])*9
                b9=int(isikukod[9])*1

                s11=b1+a1+b2+b3+b4+b5+b6+b7+b8+b9
                print(s11)
                s=s11//11
                print(s)
                p=s*11
                p1=s11-p
                if p1==int(isikukod[10]):
                    print(p1)
                else:
                    a1=int(isikukod[0])*3
                    b1=int(isikukod[1])*4
                    b2=int(isikukod[2])*5
                    b3=int(isikukod[3])*6
                    b4=int(isikukod[4])*7
                    b5=int(isikukod[5])*8
                    b6=int(isikukod[6])*9
                    b7=int(isikukod[7])*1
                    b8=int(isikukod[8])*2
                    b9=int(isikukod[9])*3
                    s11=b1+a1+b2+b3+b4+b5+b6+b7+b8+b9
                    print(s11)
                    s=s11//11
                    print(s)
                    p=s*11
                    p1=s11-p
                    print(p1)

                hhh=int(isikukod_list[8]+isikukod_list[9]+isikukod_list[10])
                #
                haigla=Sunnikoht(hhh)
                #
                sugu=Sugu(isikukod_list)
                print("Kontlroll pola")
                print(f"See on {sugu}, sünnipäev{spaev}. Ta on sündinud {haigla}")
                isikukoodid.append(isikukod)
print(isikukoodid) #
isikukoodid=naised_mehed(isikukoodid) #sort
print(isikukoodid)
arvud=list(map(int,arvud))
arvud.sort()
print(arvud)
