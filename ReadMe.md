## Proje Tanıtımı 
o TRT kurumun da ki belli bir tarihten eski dosyaların bulunması ve ilgililerin bilgilendirimlesi.
o Kurumda bulunan XML verilerini işleyerek ilgili kurumlara mail ile bilgilendirme sağlanacaktır

## Kullanılan Kütüphaneler
o import xml.etree.ElementTree as ET
o from datetime import datetime
o import smtplib
o from email.mime.text import MIMEText
o from datetime import datetime, timedelta, date
o from dataclasses import dataclass
o from typing import List
o import os


# Kütüphane Açıklamaları ve Kurulumları

1. import xml.etree.ElementTree as ET
- XML verileri işlemek ve oluşturmak için kullanılan bir modüldür.
- as ET ise bir nevi kısaltmadır.Kodun daha sade durmasını sağlar
# Örnek Kod
    root = ET.Element("data")



2. from datetime import datetim
-  Tarih ve saat bilgilerini işlemek için kullanılan bir sınıftır. Bu modül, tarihleri oluşturmak, manipüle etmek, farklı tarihler arasındaki farkları hesaplamak ve tarih/saat verilerini biçimlendirmek için kullanılır.
# Örnek Kod
    today=date.today()  --> Güncel Tarihi Gösterir



3. import smtplib
- "smtp" kısaltması, "Simple Mail Transfer Protocol" anlamına gelir ve e-postaların iletilmesi ve alınması için kullanılan bir iletişim protokolünü ifade eder
- E-posta sunucularına bağlanmanıza, e-posta göndermenize ve e-postaları almanıza yardımcı olan işlevleri sağlar.
# Örnek Kod
    import smtplib

    ##Bu kod bloğunda bağlanacağımız sunucu ve portu seçilir (tls için 587 genelde)

    smtp_server = "smtp.example.com"
    port = 587  # SMTP sunucunuzun port numarası

    ##Bu kod bloğunda e-mail göndericek e posta ve alacak e posta bilgileri alınır.İçerik de dahil bu kısıma

    sender_email = "your_email@example.com"                 
    receiver_email = "recipient@example.com"
    password = "your_password"  # E-posta hesabınızın şifresi

    subject = "Test E-postası"
    message = "Bu bir test e-postasıdır."


    ## Sunucuya bağlanılan kısım bu kısım

    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)

    ## E posta gönderme kısımı

    email_text = f"Subject: {subject}\n\n{message}"
    server.sendmail(sender_email, receiver_email, email_text)

    ##Sunucudan çıkma kısımı

    server.quit()

3. from email.mime.text import MIMEText
- Bu sınıf, e-posta içeriğini temsil etmek için kullanılan bir MIME(Multipurpose Internet Mail Extensions) türüdür.
# Örnek Kod 
    msg = MIMEText(icerik)

4. from datetime import datetime, timedelta, date
-  datetime :  bir tarihi ve saat bilgisini temsil etmek veya iki tarih arasındaki farkı hesaplamak için kullanılabilir.

- timedelta : Bu sınıf, iki tarih veya saat arasındaki farkı temsil etmek için kullanılır

- date : Bu sınıf, yıl, ay ve gün gibi tarihi temsil eder. Ancak saat, dakika ve saniye bilgilerini içermez. Yani, sadece tarih bölümünü temsil eder.

# Örnek Kod
    from datetime import datetime, timedelta, date

    ** Bugünün tarihini alma
    bugun = date.today()

    ** Şu anki tarihi ve saati alma
    simdiki_tarih_saat = datetime.now()

    ** Belirli bir tarih oluşturma
    belirli_tarih = date(2023, 8, 1)

    ** Belirli bir zaman aralığı oluşturma
    zaman_araligi = timedelta(days=7)

    ** Bir tarih arasındaki farkı hesaplama
    fark = belirli_tarih - bugun

    ** Bir tarihe belirli bir zaman aralığı eklemek
    gelecek_tarih = bugun + zaman_araligi



5.  from dataclasses import dataclass

- Bir dataclass, verileri saklamak ve temsil etmek için kullanılan sınıfları daha az kod yazarak tanımlamanıza olanak tanır

# Örnek Kod
        from dataclasses import dataclass

        @dataclass
        class Person:
            name: str
            age: int
            profession: str

        # Dataclass kullanımı
        person1 = Person("Alice", 30, "Engineer")
        person2 = Person("Bob", 25, "Designer")

        print(person1)  # Bu, otomatik olarak oluşturulan __repr__ metodu sayesinde daha güzel bir çıktı verecektir.
        print(person2)


6. from typing import List
- typing modülü :  tür anotasyonları yaparak kodunuzu daha okunabilir ve anlaşılır hale getirmenize yardımcı olur.

- List sınıfı : belirli bir türde verileri içeren bir liste nesnesini temsil etmek için kullanılır

# Örnek Kod
        from typing import List

        ** List[int] , bu fonksiyona sadece tamsayılar içeren bir liste verilebileceği anlamına gelir
        def double_elements(numbers: List[int]) -> List[int]:
            """Listedeki tüm sayıları iki katına çıkararak yeni bir liste döndürür."""
            doubled = [num * 2 for num in numbers]
            return doubled

        my_list = [1, 2, 3, 4, 5]
        doubled_list = double_elements(my_list)

        print(doubled_list)  # [2, 4, 6, 8, 10]


7. import os
- Bu modül, işletim sistemi ile etkileşimde bulunmanıza ve sistem düzeyinde işlemler gerçekleştirmenize olanak tanır.   
 # Kullanım Alanları Örnek
 1. Dizin ve Dosya İşlemleri
 2. Dosya Silme
 3. Sistem Çevre(environment) Değişkenleri   --> kodumuzda kullandığımız

# Örnek Kod
        import os

        **PATH çevre değişkenini alma
        path_env = os.environ.get("PATH")
- Bu şekilde başka bir cihazda PATH değeri biz ne verdiysek o olarak işlem görür.


