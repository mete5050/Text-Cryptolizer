import os
import random


normal = '\033[0m'
kirmizi= '\033[31m'
yesil= '\033[32m'
sari= '\033[33m'
lacivert= '\033[34m'
mor= '\033[35m'
mavi= '\033[36m'
pmavi = '\033[96m'#p --> parlak
pyesil = '\033[92m'
psari = '\033[93m'
siyah = '\033[90m'
asiyah= '\033[40m'#a --> arkaplan
akirmizi= '\033[41m'
ayesil= '\033[42m'
asari= '\033[43m'
alacivert= '\033[44m'
amor= '\033[45m'
amavi= '\033[46m'
abeyaz= '\033[47m'
apsiyah= '\033[100m'#a --> arkaplan
apkirmizi= '\033[101m'
apyesil= '\033[102m'
apsari= '\033[103m'
aplacivert= '\033[104m'
apmor= '\033[105m'
apmavi= '\033[106m'
apbeyaz= '\033[107m'

kulad="mete"#buraya kullanıcı adınızı girin veya "mete" yi input("Kullanıcı adınızı giriniz: ") olarak değiştirin
sfrdad=2045077146179#1019300863759 yerine /home/kullanıcı_adınız/sifrele/sifreler/ klasorünün içindeki bir dosyanın adını yazın (bu ad kişiye özeldir)

hrflr=open("/home/"+kulad+"/sifrele/sifreler/"+str(sfrdad),"r")
harfler = str(hrflr.read())
harfler2=harfler.split()
calis=True
os.system("clear")
while (calis):
    rndom = []
    dizilim=[]

    

    print(pmavi+"1-Şifreleme yap")
    print("2-Şifreleme çöz")
    print(kirmizi+"3-Çık \n")

    scm=input(pyesil +"Seçiminiz :"+psari) 

    if (scm== "1"):

        dsyad=input(pmavi+"Şifre dosyasının adını giriniz : "+psari)
        
        os.system("mkdir /home/"+kulad+"/Masaüstü/"+dsyad)
        czm=open("/home/"+kulad+"/Masaüstü/"+dsyad+"/coz.txt",'w')
        klm = input(pmavi+"Harf veya harf gurubunu giriniz :"+psari)
        klml = list(klm)
        
        say=0
        
        while (say < len(klml)):
            x=True
            say3=0
            
            while (say3 < len (klml)):
                if(klml[say3]==" "):
                    klml[say3]=""
                say3+=1
            
            say2=0
            
            while x:
                print(klml[say])
                if(klml[say]==harfler2[say2]):
                    dizilim.append(say2)
                    x = False
                say2+=1

            czm.write(str(dizilim[say])+" ")
            print (str(dizilim[say])+" ")
            say+=1
        os.system("clear")
        print (psari+str(dizilim)+"\n \n \n")
        czm.close()

        
    if (scm== "2"):  
        say4=0
        cozulmus=[]
        dosyaad=input(pmavi+"Şifrelenmiş dosya konumunu giriniz :"+psari)
        print(psari)
        coz=open(dosyaad,"r")
        cozliste=coz.read()
        cozliste2=cozliste.split()
    
        while(say4 < len(cozliste2)):
           cozs=int(cozliste2[say4])
           cozulmus.append(harfler2[cozs])
           say4+=1
        say3=0
            
        while (say3 < len (cozulmus)):
            if(cozulmus[say3]==""):
                cozulmus[say3]=" "
            say3+=1
        os.system("clear")
        print(psari+str(cozulmus)+"\n \n \n")
        
        
    
    if (scm== "3"):  
        calis=False
    
