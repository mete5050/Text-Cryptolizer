#bu program ihtimalleri oluşturur ve her çalıştığında ihtimaller farklılık göstereceğinden dolayı farklı bir bilgisayarda şifreyi çözmek istiyorsanız /home/kullanıcı_adınız/sifrele/sifreler/     klasorünü farklı bir cihaza atıp oradan okutmanız gerek 

import random
import os

kulad=input("Kullanıcı adınızı giriniz: ")
os.system("sudo rm -r /home/"+kulad+"/sifrele/sifreler/")
os.system("mkdir /home/"+kulad+"/sifrele/")
os.system("mkdir /home/"+kulad+"/sifrele/sifreler/")
say=0
while (say < 10000):#10000 yerine daha büyük bir sayı girebilirsiniz fakat bu sefer bilgisayarınız zorlanabillir
    harfler=['e','Ö','k','Y','f','g','C','h','V','a','T','D','b','X','ö','F','ç','i','j','l','m','O','n','c','d','o','Ç','p','r','s','t','y','z','x','u','ü','v','K','w','L',':',',','`','@','.','-','=','J','Ü','(','P',')','R','[','U',']','İ','&','W','%','Ş','+','$','I','S','#','A','Q','^','Z','!','>','_','B','é','\ ','£','1','G','2','9','/','*','0','N','7','6','8','H','4','ı','5','M','E','3','','?','"','q']#,''
    
    isim=random.randint(0,82182128218212)
    dosya=open("/home/mete/sifrele/sifreler/"+str(isim),"a")
    str(random.shuffle(harfler))
    x=0
    
    while(x<len(harfler)):
        dosya.write(str(harfler[x])+" ")
        x+=1
        
    say +=1
    b=0
    
    print(say)
    print(harfler)
