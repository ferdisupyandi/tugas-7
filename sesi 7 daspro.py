#!/usr/bin/env python
# coding: utf-8

# In[1]:


# mencetak angka 1 - 10

for i in range (1,11):
    print(i, end=" ")


# In[2]:


# mencetak angka 10 20 30 .... 100

for i in range (1,11):
    print(i *10, end=" ")


# In[3]:


# mencetak angka 10 20 30 .... 100

for i in range (10,101):
    print(i, end=" ")


# In[4]:


# mencetak angka 10 9 8...1

for i in range (1,11):
    print(11-i, end=" ")


# In[5]:


# mencetak angka 10 9 8...1

for i in range (10,0,-1):
    print(i, end=" ")


# In[6]:


# mencetak angka 100 99 98...1

for i in range (100,0,-1):
    print(i, end=" ")


# In[7]:


# mencetak angka 1-2 3-4 5-6...10
sign = 1
for i in range (1,11):
    sign = sign * - 1
    print(sign, end=" ")


# In[8]:


# mencetak angka 1-2 3-4 5-6...10
sign = 1
for i in range (1,11):
    sign = sign * - 1
    print(sign*i, end=" ")


# In[9]:


# mencetak angka 1-2 3-4 5-6...10
sign = -1
for i in range (1,11):
    sign = sign * - 1
    print(sign*i, end=" ")


# In[13]:


# mencari bil faktorial
# input = 3, output = 3 * 2 * 1 = 6
# input = 4, output = 4 * 3 * 2 * 1 = 24

bil = int(input("isikan bilangan : "))

hasil = 1

for i in range(1, bil+1):
    hasil = hasil * i
print(f"{bil}! adalah {hasil}")


# In[15]:


# mencari bil faktorial
# input = 3, output = 3 * 2 * 1 = 6
# input = 4, output = 4 * 3 * 2 * 1 = 24

bil = int(input("isikan bilangan : "))

hasil = 1
label = " "
for i in range(1, bil+1):
    hasil = hasil * i
    label = label + str((bil+1)-i) + " * "
    
print(f"{bil}! adalah {hasil}")
print(f"{label} = {hasil}")


# In[14]:


# mencari bil pangkat

pangkat = int(input("masukan bilangan : "))

hasil = 1
for i in range(1, pangkat+1):
    hasil *= bil
print(f"{bil}! pangkat {pangkat}adalah{hasil}")


# In[16]:


# mengecek bil prima atau bukan
#bil prima adalah bil yang hanya habis dibagi 1 dan bil itu sendiri

kondisi = " "
bil = int(input("masukan bilangan"))
jumlah = 0
for i in  range(1, bil + 1):
    sisa = bil % i
    if sisa == 0:
        jumlah = jumlah + 1
    if jumlah == 2:
        kondisi = "bilangan prima"
    else:
        kondisi = "bilangan prima"
print(f"sisa={jumlah}, maka{kondisi}")


# In[17]:


# break dan continue

for i in range(1,10):
    print(i)
    if i==5:
        break
    
print()
for j in range(1,10):
    if j==5:
        continue
    print(j, end =" ")


# In[18]:


# looping untuk string, menghuitung hurup vokal

kalimat = input("masukan kalimat: " )

vokal_a = 0
vokal_i = 0
vokal_u = 0
vokal_e = 0
vokal_o = 0

for i in kalimat:
    if i=='a':
        vokal_a += 1
    elif i=='i':
        vokal_i += 1
    elif i=='u':
        vokal_u += 1
    elif i=='e':
        vokal_e += 1
    elif i=='0':
        vokal_o += 1
print(f"jumlah hurup i:{vokal_a}")
print(f"jumlah hurup i:{vokal_i}")
print(f"jumlah hurup i:{vokal_u}")
print(f"jumlah hurup i:{vokal_e}")
print(f"jumlah hurup i:{vokal_o}")

total = vokal_a + vokal_i +  vokal_u +  vokal_e +  vokal_o
print(f"jumlah hurup vokal : {total}")


# In[19]:


# kaliamat palindrom atau bukan
# palindron adalah kalimat yang di baca dari kiri ke kanan == kanan ke kiri
# kasur rusak

kalimat = input("masukan kalimat:")
panjang = len(kalimat)

for i in range(0, panjang):
    kika = kalimat[i]
    kaki = kalimat[panjang - i - 1]
    print(kika, kaki)


# In[ ]:


# kaliamat palindrom atau bukan
# palindron adalah kalimat yang di baca dari kiri ke kanan == kanan ke kiri
# kasur rusak
ulang = "Y"
while(ulang=="Y"):

    kalimat = input('masukan kalimat:')
    panjang = len(kalimat)
    keterangan = "palindrom"
    for i in range(0,panjang):
        kika = kalimat [i].lower()
        kaki = kalimat [panjang-i -1].lower()
        print(kika, kaki)
    
        if kika != kaki:
            keterangan = "bukan palindrom"
            break
            
       
    print(f"{keterangan}")
    jawab =" "
    while(jawab != "Y" and jawab != "n"):
     ulang = input("silahkan ulangi program(Y/n)?:")
    ulang = jawab


# In[ ]:





# In[ ]:





# In[ ]:




