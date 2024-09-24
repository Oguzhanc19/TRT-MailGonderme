import xml.etree.ElementTree as ET
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from requests.api import get
from unittest.mock import patch
from io import StringIO
from unittest.mock import patch, MagicMock
import requests
import shutil
from datetime import date 
today=date.today()


# Gönderen e-posta ve şifresi
gonderen_email = "emailadresiniz@gmail.com"
gonderen_sifre = "gönderenmailşifreniz"

# Alıcı e-posta
alici_email = "alıcıemail@gmail.com"

# E-posta sunucusu bilgileri
smtp_sunucu = "smtp.gmail.com"
smtp_port = 587  # Genellikle 587 veya 465 olarak kullanılır (SSL için)



def eposta_gonder(konu,icerik):
    # E-posta içeriğini oluşturma
    msg = MIMEText(icerik)
    msg["From"] = gonderen_email
    msg["To"] = alici_email
    msg["Subject"] = konu
    
    try:
        # E-posta sunucusuna bağlanma
        smtp_server = smtplib.SMTP(smtp_sunucu, smtp_port)
        smtp_server.starttls()
        smtp_server.login(gonderen_email, gonderen_sifre)

        # E-postayı gönderme
        smtp_server.sendmail(gonderen_email, alici_email, msg.as_string())
        smtp_server.quit()
        
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print("E-posta gönderilirken bir hata oluştu:", e)

dosya="test.xml"
tree=ET.parse(dosya)
root=tree.getroot()

def process_xml_data():
    try:
        print("""
        1-TRT Cocuk
        2-TRT Turk
        3-TRT 1 HD
        4-TRT Spor2
        5-TRT Avaz
        6-MEB
        7-TRT Belgesel
        8-TRT Kurdi                                                        
        """)
        tercih=int(input("Hangi Kanal : "))

        belirliTarih=today
        tum_trtcocuk_verileri ={}
        tum_trtturk_verileri ={}
        tum_trt1hd_verileri ={}
        tum_spor2_verileri ={}
        tum_meb_verileri ={}
        tum_trtbelgesel_verileri ={}
        tum_trtkurdi_verileri ={}
        tum_trtavaz_verileri={}
        videolar = {"trt1":[], "trtcocuk":[]}

        for id in root.findall("MediaInfo"):
                    
            if tercih==1:
                        ID=id.find("MediaID").text
                        deneme=id.find("Channels").text
                        tarihi=id.find("DateCreation")

                        tarih1=datetime.strptime(belirliTarih,'%Y-%m-%d %H:%M:%S.%f')#belirlenen tarih
                        tarih2=[]
                        tarih2.append(tarihi.text)
                        a=tarih2[0]
                        XmlTarih=datetime.strptime(a,'%Y-%m-%d %H:%M:%S.%f')
                        
                        if deneme=="TRT Cocuk;":
                            if XmlTarih<tarih1:     
                                if deneme in tum_trtcocuk_verileri:
                                        tum_trtcocuk_verileri[deneme].append({"MediaID": ID, "Yayın Tarihi": tarihi.text})
                                            
                                else:
                                        tum_trtcocuk_verileri[deneme] = [{"MediaID": ID, "Yayın Tarihi": tarihi.text}]
                            
            if tercih==2:
                    ID=id.find("MediaID").text
                    deneme=id.find("Channels").text
                    tarihi=id.find("DateCreation")

                    tarih1=datetime.strptime(belirliTarih,'%Y-%m-%d %H:%M:%S.%f')#belirlenen tarih
                    tarih2=[]
                    tarih2.append(tarihi.text)
                    a=tarih2[0]
                    XmlTarih=datetime.strptime(a,'%Y-%m-%d %H:%M:%S.%f')
                        
                    if deneme=="TRT Turk;":
                                if XmlTarih<tarih1:     
                                    if deneme in tum_trtturk_verileri:
                                        tum_trtturk_verileri[deneme].append({"MediaID": ID, "Yayın Tarihi": tarihi.text})
                                            
                                    else:
                                        tum_trtturk_verileri[deneme] = [{"MediaID": ID, "Yayın Tarihi": tarihi.text}]
            if tercih==3:
                    ID=id.find("MediaID").text
                    deneme=id.find("Channels").text
                    tarihi=id.find("DateCreation")

                    tarih1=datetime.strptime(belirliTarih,'%Y-%m-%d %H:%M:%S.%f')#belirlenen tarih
                    tarih2=[]
                    tarih2.append(tarihi.text)
                    a=tarih2[0]
                    XmlTarih=datetime.strptime(a,'%Y-%m-%d %H:%M:%S.%f')
                        
                    if deneme=="TRT 1 HD;":
                                if XmlTarih<tarih1:     
                                    if deneme in tum_trt1hd_verileri:
                                        tum_trt1hd_verileri[deneme].append({"MediaID": ID, "Yayın Tarihi": tarihi.text})
                                            
                                    else:
                                     tum_trt1hd_verileri[deneme] = [{"MediaID": ID, "Yayın Tarihi": tarihi.text}]
            if tercih==4:     
                    ID=id.find("MediaID").text
                    deneme=id.find("Channels").text
                    tarihi=id.find("DateCreation")

                    tarih1=datetime.strptime(belirliTarih,'%Y-%m-%d %H:%M:%S.%f')#belirlenen tarih
                    tarih2=[]
                    tarih2.append(tarihi.text)
                    a=tarih2[0]
                    XmlTarih=datetime.strptime(a,'%Y-%m-%d %H:%M:%S.%f')
                        
                    if deneme=="TRT Spor2;":
                                if XmlTarih<tarih1:
                                    if deneme in tum_spor2_verileri:
                                        tum_spor2_verileri[deneme].append({"MediaID": ID, "Yayın Tarihi": tarihi.text})
                                            
                                    else:
                                        tum_spor2_verileri[deneme] = [{"MediaID": ID, "Yayın Tarihi": tarihi.text}]
                            
            if tercih==5: 
                    ID=id.find("MediaID").text
                    deneme=id.find("Channels").text 
                    tarihi=id.find("DateCreation")

                    tarih1=datetime.strptime(belirliTarih,'%Y-%m-%d %H:%M:%S.%f')#belirlenen tarih
                    tarih2=[]
                    tarih2.append(tarihi.text)
                    a=tarih2[0]
                    XmlTarih=datetime.strptime(a,'%Y-%m-%d %H:%M:%S.%f')
                        
                    if deneme=="TRT Avaz;":
                        if XmlTarih<tarih1:
                                if deneme in tum_trtavaz_verileri:
                                        tum_trtavaz_verileri[deneme].append({"MediaID": ID, "Yayın Tarihi": tarihi.text})
                                            
                                else:
                                        tum_trtavaz_verileri[deneme] = [{"MediaID": ID, "Yayın Tarihi": tarihi.text}]
                                

            if tercih==6:
                    ID=id.find("MediaID").text
                    deneme=id.find("Channels").text
                    tarihi=id.find("DateCreation")
                    
                    tarih1=datetime.strptime(belirliTarih,'%Y-%m-%d %H:%M:%S.%f')#belirlenen tarih
                    tarih2=[]
                    tarih2.append(tarihi.text)
                    a=tarih2[0]
                    XmlTarih=datetime.strptime(a,'%Y-%m-%d %H:%M:%S.%f')
                        
                    if deneme=="MEB;":
                        if XmlTarih<tarih1:
                                if deneme in tum_meb_verileri:
                                        tum_meb_verileri[deneme].append({"MediaID": ID, "Yayın Tarihi": tarihi.text})
                                            
                                else:
                                        tum_meb_verileri[deneme] = [{"MediaID": ID, "Yayın Tarihi": tarihi.text}]
                                

            if tercih==7:
                    ID=id.find("MediaID").text
                    deneme=id.find("Channels").text
                    tarihi=id.find("DateCreation") 
                    
                    tarih1=datetime.strptime(belirliTarih,'%Y-%m-%d %H:%M:%S.%f')#belirlenen tarih
                    tarih2=[]
                    tarih2.append(tarihi.text)
                    a=tarih2[0]
                    XmlTarih=datetime.strptime(a,'%Y-%m-%d %H:%M:%S.%f')
                        
                    if deneme=="TRT Belgesel;":
                        if XmlTarih<tarih1:
                            if deneme in tum_trtbelgesel_verileri:
                                tum_trtbelgesel_verileri[deneme].append({"MediaID": ID, "Yayın Tarihi": tarihi.text})
                                            
                            else:
                                tum_trtbelgesel_verileri[deneme] = [{"MediaID": ID, "Yayın Tarihi": tarihi.text}]

                    
            if tercih==8:
                    ID=id.find("MediaID").text
                    deneme=id.find("Channels").text
                    tarihi=id.find("DateCreation")

                    tarih1=datetime.strptime(belirliTarih,'%Y-%m-%d %H:%M:%S.%f')#belirlenen tarih
                    tarih2=[]
                    tarih2.append(tarihi.text)
                    a=tarih2[0]
                    XmlTarih=datetime.strptime(a,'%Y-%m-%d %H:%M:%S.%f')
                        
                    if deneme=="TRT Kurdi;":
                        if XmlTarih<tarih1:
                            if deneme in tum_trtkurdi_verileri:
                                tum_trtkurdi_verileri[deneme].append({"MediaID": ID, "Yayın Tarihi": tarihi.text})
                                            
                            else:
                                tum_trtkurdi_verileri[deneme] = [{"MediaID": ID, "Yayın Tarihi": tarihi.text}]


        for kanal, veriler in tum_trtcocuk_verileri.items():#veriler tek bir sözlük içinde sadece alt alta durmasın için olan yer
                print("Şu kayıtların süresi belirlenen tarih dışındadır;")
                if tum_trtcocuk_verileri=={}:
                    print(" ")
                else:
                    a=[]    
                    for veri in veriler:
                        print(kanal,veri)
                        a.append(veri)  
                altalta="\n".join(str(veri) for veri in a)    
                icerik="Süresi Dolmuş Kayıtlar ! "
                konu=f"Merhaba,bu bir otomatik mesaj e-posta gönderimidir.Biriminiz adında kayıtlı bulunan bu kayıtların , belirlenen tarih dışında olduğu anlaşılmıştır lütfen siliniz.\n\n{altalta}"          
                eposta_gonder(icerik,konu)      
        

        for kanal, veriler in tum_trtturk_verileri.items():
                print("Şu kayıtların süresi belirlenen tarih dışındadır;")
                if tum_trtturk_verileri=={}:
                    print(" ")
                else:  
                    a=[]  
                    for veri in veriler:
                        print(kanal,veri) 
                        a.append(veri)  
                altalta="\n".join(str(veri) for veri in a)    
                icerik="Süresi Dolmuş Kayıtlar ! "
                konu=f"Merhaba,bu bir otomatik mesaj e-posta gönderimidir.Biriminiz adında kayıtlı bulunan bu kayıtların , belirlenen tarih dışında olduğu anlaşılmıştır lütfen siliniz.\n\n{altalta}"          
                eposta_gonder(icerik,konu)  
        
        for kanal, veriler in tum_trtkurdi_verileri.items():
                print("Şu kayıtların süresi belirlenen tarih dışındadır;")
                if tum_trtkurdi_verileri=={}:
                    print(" ")
                else:   
                    a=[] 
                    for veri in veriler:
                        print(kanal,veri)
                        a.append(veri)  
                altalta="\n".join(str(veri) for veri in a)    
                icerik="Süresi Dolmuş Kayıtlar ! "
                konu=f"Merhaba,bu bir otomatik mesaj e-posta gönderimidir.Biriminiz adında kayıtlı bulunan bu kayıtların , belirlenen tarih dışında olduğu anlaşılmıştır lütfen siliniz.\n\n{altalta}"          
                eposta_gonder(icerik,konu)  
        
                    
        for kanal, veriler in tum_meb_verileri.items():
                print("Şu kayıtların süresi belirlenen tarih dışındadır;")
                if tum_meb_verileri=={}:
                    print(" ")
                else:  
                    a=[]  
                    for veri in veriler:
                        print(kanal,veri) 
                        a.append(veri)  
                altalta="\n".join(str(veri) for veri in a)    
                icerik="Süresi Dolmuş Kayıtlar ! "
                konu=f"Merhaba,bu bir otomatik mesaj e-posta gönderimidir.Biriminiz adında kayıtlı bulunan bu kayıtların , belirlenen tarih dışında olduğu anlaşılmıştır lütfen siliniz.\n\n{altalta}"          
                eposta_gonder(icerik,konu)  
         
        for kanal, veriler in tum_spor2_verileri.items():
                print("Şu kayıtların süresi belirlenen tarih dışındadır;")
                if tum_spor2_verileri=={}:
                    print(" ")
                else:
                    a=[]    
                    for veri in veriler:
                        print(kanal,veri)  
                        a.append(veri)  
                altalta="\n".join(str(veri) for veri in a)    
                icerik="Süresi Dolmuş Kayıtlar ! "
                konu=f"Merhaba,bu bir otomatik mesaj e-posta gönderimidir.Biriminiz adında kayıtlı bulunan bu kayıtların , belirlenen tarih dışında olduğu anlaşılmıştır lütfen siliniz.\n\n{altalta}"          
                eposta_gonder(icerik,konu)  

        for kanal, veriler in tum_trt1hd_verileri.items():
                print("Şu kayıtların süresi belirlenen tarih dışındadır;")   
                if tum_trt1hd_verileri=={}:
                    print(" ")
                else: 
                    a=[]   
                    for veri in veriler:
                        print(kanal,veri)  
                        a.append(veri)  
                altalta="\n".join(str(veri) for veri in a)    
                icerik="Süresi Dolmuş Kayıtlar ! "
                konu=f"Merhaba,bu bir otomatik mesaj e-posta gönderimidir.Biriminiz adında kayıtlı bulunan bu kayıtların , belirlenen tarih dışında olduğu anlaşılmıştır lütfen siliniz.\n\n{altalta}"          
                eposta_gonder(icerik,konu)  

        for kanal, veriler in tum_trtavaz_verileri.items():
                print("Şu kayıtların süresi belirlenen tarih dışındadır;")
                if tum_trtavaz_verileri=={}:
                    print(" ")
                else:
                    a=[]    
                    for veri in veriler:
                        print(kanal,veri) 
                a.append(veri)  
                altalta="\n".join(str(veri) for veri in a)    
                icerik="Süresi Dolmuş Kayıtlar ! "
                konu=f"Merhaba,bu bir otomatik mesaj e-posta gönderimidir.Biriminiz adında kayıtlı bulunan bu kayıtların , belirlenen tarih dışında olduğu anlaşılmıştır lütfen siliniz.\n\n{altalta}"          
                eposta_gonder(icerik,konu)  

        for kanal, veriler in tum_trtbelgesel_verileri.items():
                
                print("Şu kayıtların süresi belirlenen tarih dışındadır;")
                if tum_trtbelgesel_verileri=={}:
                    print(" ")
                else:
                    a=[]    
                    for veri in veriler:
                        print(kanal,veri)
                        a.append(veri)  
                    altalta="\n".join(str(veri) for veri in a)    
                icerik="Süresi Dolmuş Kayıtlar ! "
                konu=f"Merhaba,bu bir otomatik mesaj e-posta gönderimidir.Biriminiz adında kayıtlı bulunan bu kayıtların , belirlenen tarih dışında olduğu anlaşılmıştır lütfen siliniz.\n\n{altalta}"          
                eposta_gonder(icerik,konu)  
                

                                     

    except Exception as e:
            print("Listeden Seç")

"""""
class TestYourCode(unittest.TestCase):

    def setUp(self):
        self.gonderen_email = "yedekemailil2@gmail.com"
        self.gonderen_sifre = "zqvxuiuypjtmenkn"
        self.alici_email = "oguzhan196060@gmail.com"
        self.konu = "süresi geçmiş yayın"
        self.icerik = "Merhaba, bu bir otomatik e-posta gönderimidir."
        result = TRTxml.eposta_gonder(gonderen_email, gonderen_sifre, alici_email, konu, icerik)
        self.assertIsNone(result)

#kodun otomatikleştirildiği kısım
def run_unit_test(input_data):#input_data  yukarda ki process_xml_data yı çağırır
    #patch unittest.mock ürünü test işlemini otomatikleştirir
    with patch('builtins.input', side_effect=input_data), patch('sys.stdout', new_callable=io.StringIO) as fake_output:
        #input_data ve sys.stdout u geçici değerler ile değiştiriyoruz
        process_xml_data("test.xml", 1, "2024-01-01 23:59:59.590")
    return fake_output.getvalue()

class TestXMLProcessing(unittest.TestCase):

    def test_process_xml_data_for_TRT_Cocuk(self):
        user_input = ["1\n"]#Eğer 1 i yani TRTCOCUK seçersek diye
        output = run_unit_test(user_input)#Girilen değer ile yukarda ki fonksiyonu çağırır
    

    def test_process_xml_data_for_TRT_Turk(self):
        user_input = ["2\n"]
        output = run_unit_test(user_input)
   

    def test_process_xml_data_for_TRT_1_HD(self):
        user_input = ["3\n"]
        output = run_unit_test(user_input)
        

    #Sadece 3 tanesini test ettik bu arttırılabilir


if __name__=="__main__":
      unittest.main()
"""""


def get_xml_data(url):
    """
    get_xml_data bir url kullanarak xml datası çeker
    :param url: ABCD
    :return: EFG
    """
    try:
        response = requests.get(url, stream=True)
        #Stream=true  ifadesi yanıtın(get) içeriğinin hemen değil yavaş yavaş inmesini sağlar
        #büyük dosyaları işlerken bellek verimliliğini sağlar
        if response.status_code == 200:
            with open("TRT.xml", "wb") as file:
                #wb  dosyayı binary modda açacağımızı belirttik.Veriyi doğrudan baytlar halinde yazmamızı sağlar
                
                response.raw.decode_content = True
                #true diyerek decode_contnet e onay veriyoruz yani içerik decode eder
                #response.raw  yanıtın içeriğini temsil eder 
                    
                shutil.copyfileobj(response.raw, file)

            print("XML dosyası başarıyla indirildi ve kaydedildi.")
        else:
            print("XML dosyası indirilemedi. İstek durumu:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("İstek hatası:", e)

# XML verisini çekmek için örnek bir URL
xml_url = "ÇEKİLECEK VERİ URL"


if __name__=="__main__":
     process_xml_data()
     """
     get_xml_data(xml_url) Docstring
     """
     

