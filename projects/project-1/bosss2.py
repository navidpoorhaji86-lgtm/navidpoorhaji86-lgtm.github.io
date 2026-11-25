print('----khoah galdin ----')
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime('%a'))
while True:
    noetuple=int(input('1.barname 1. telefon ---'))
    print(noetuple)
    if noetuple==1:
                sef={'ghifi':'ghi 1 ghi2 ghi 3','non':'non1 non2','ab':'ab1 ab2 ab3 ','esc':'esc1 esc2 esc3'}
                print(sef)
                if sef==1:
                     ghi=int(input('1.ghi 2.ghi 3.ghi '))
                for ghi in range(4):
                    if ghi==1:
                        print('gheymat 45000')  
                    elif ghi==2:
                        print('gheymat 48000')
                    elif ghi==3:
                        print('gheymat 55000')
                    elif sef==2:
                         non=int(input('non ----1.noni sade 2.noni ba peste '))
                for non in range(3): 
                    if non==1:
                        print('gheymat 55000')
                    elif non==2:
                        print('gheymat 60000')
                    elif sef==3:
                         ab=int(input('ab -----1.ab porteghal 2.ab havij bas 3.ab talebi'))
                for ab in range(4):
                    if ab==1:
                        print('gheymat 45000')
                    elif ab==2:
                        print('gheymat 55000')
                    elif ab==3:
                        print('ghetymat 46000')
                    elif sef==4:
                         esc=int(input('esc-----1.1esc 2.2esc 3.esc'))
                for esc in range(4):
                    if esc==1:
                        print('gheyamt 20000')
                    elif esc==2:
                        print('gheymat 40000')
                    elif esc==3:
                        print('gheymat 60000')
                avr=int(input('avrdan ----1.peyk 2.hozori'))
                if avr==1:
                     esm=input('esme ranande ----')
                     time=input('key miyay -----  ')
                     time2=input('key -----')
                     adr=input('adr bede ----')    
                     shomare=int(input('shomare fak -----'))
                     ghy=int(input('ghy bede ---'))
                     print(f'aghay:{esm} saat tahvil:{time}  saat residan:{time2}  adr:{adr}  shomare fak:{shomare}  ghemat kol:{ghy}')
                elif avr==2:
                     print('20 daghige dik tashrif biyavarid')
    else:
            es=input('esme bede ------')
            shomar=int(input('sho bede -----'))
            sef=input('sef bede ----')
            gh=int(input('ghey bede -----'))
            sh=int(input('fak bede -----'))
            no=int(input('biyarim ------1.peyk 2.hozori'))
            if  no==1:
                ra=input('esm ranande ------')
                adrs=input('adrs bede -----')
                print(f'aghaye:{es}  shomare:{shomar}  sefaresh:{sef}  gheymat kol:{gh}  shomare faktor:{sh}  zaman residan:{ra}  adr:{adrs}')
            elif no==2:
                print('20 min digev tashrif biyarid ')
            print('khodafez')
            r=int(input('exit -----'))
            import datetime
            x=datetime.datetime.now()
            print(x.year)
            print(x.strftime('%a'))
            if r==10:
             break
