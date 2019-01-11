import sqlite3
connectdb=sqlite3.connect('test.db')
if(connectdb):
    print('Baglanti Başarılı!')
    veritabani=connectdb.cursor()
    kontrol=True
    while(kontrol):
        nick=input("nickname :\n")
        pssw=input("pass :\n")
        if(len(nick)!=0 and len(pssw)!=0):
            oku=veritabani.execute("SELECT count(*) as 'giris' FROM user where nickname='"+nick+"' and pass='"+pssw+"'")
            for i in oku.fetchall():
                giris=i[0]
            if(giris==1):
                print("Giriş başarılı.")
                break
            else:
                print("bilgilerde hata var")

        else:
            print("hata")


else:
    print('Bağlantı Başarısız!')

