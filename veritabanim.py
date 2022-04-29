import sqlite3
con=sqlite3.connect("banka2.db")
cursor=con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS hastane (hastano INT,hastaad TEXT,hastasoyad TEXT)")
    con.commit()
    
    
        
def veri_ekle():
    cursor.execute("INSERT INTO hastane VALUES (47,'CAN','KAAN')")
    con.commit()
    
  

def veri_sil(a):
    cursor.execute("DELETE FROM hastane where hesapno=?",(a,))
    con.commit()
    con.close()

def veri_guncelle():
    cursor.execute("UPDATE hastane set ad=? where ad=?",('ATACAN','CAN'))
    con.commit()
    con.close()


tablo_olustur()

veri_ekle()

veri_sil()

veri_guncelle()
