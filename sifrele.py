import os
import random
import sys

normal = '\033[0m'
kirmizi= '\033[31m'
pmavi = '\033[96m'#p --> parlak
pyesil = '\033[92m'
psari = '\033[93m'


kulad="mete"#buraya kullanıcı adınızı girin veya "mete" yi input("Kullanıcı adınızı giriniz: ") olarak değiştirin
sfrdad=327397359814#327397359814 yerine /home/kullanıcı_adınız/sifrele/sifreler/ klasorünün içindeki bir dosyanın adını yazın (bu ad kişiye özeldir)

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
        print(klml)
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
                
                
                if(klml[say]==harfler2[say2]):
                    dizilim.append(say2)
                    
                    x = False
                say2+=1
            print(dizilim)
            print(str(say)+"  "+str(say2))
            czm.write(str(dizilim[say])+" ")
            #print (str(dizilim[say])+" ")
            say+=1
        czm.write(str(sfrdad))
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
        print(cozliste2)
        sfrdad=cozliste2[len(cozliste2)-1]
        cozliste2.pop()
        print(sfrdad)
        hrflr=open("/home/"+kulad+"/sifrele/sifreler/"+str(sfrdad),"r")
        harfler = str(hrflr.read())
        harfler2=harfler.split()  
        
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
        x1=0
        while(x1<len(cozulmus)):
            sys.stdout.write(sari+str(cozulmus[x1]))
            x1+=1
        
        
    
    if (scm== "3"):  
        calis=False
    
    print("\n \n")
