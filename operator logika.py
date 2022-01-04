#belajar operator logika

gaji_pokok = int(input("gaji pokok bulanan kamu Rp:"))

if gaji_pokok >= 2000000 and gaji_pokok <= 4000000:
    pajak = gaji_pokok*2/100
    gaji_bersih = gaji_pokok-pajak
elif gaji_pokok >= 4000000 and gaji_pokok <= 5000000:
    pajak = gaji_pokok*3/100
    gaji_bersih = gaji_pokok-pajak
elif gaji_pokok >= 5000000:
    pajak = gaji_pokok*5/100
    gaji_bersih = gaji_pokok-pajak
gaji_selama_setahun = gaji_bersih*12
print("gaji kamu selama setahun Rp:",gaji_selama_setahun)






