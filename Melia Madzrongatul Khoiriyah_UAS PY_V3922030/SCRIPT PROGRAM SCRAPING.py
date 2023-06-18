#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests  # Impor modul requests untuk melakukan permintaan HTTP
import csv  # Impor modul csv untuk memanipulasi file CSV

key = input('masukkan keyword :')  # Meminta input kata kunci dari pengguna
#bisa masukkan key nya sepatu

write = csv.writer(open('hasil/{}.csv'.format(key), 'w', newline=''))  # Membuka file CSV baru dengan nama file sesuai dengan kata kunci yang dimasukkan
header = ['Nama', 'Harga', 'Alamat']  # Menentukan header file CSV
write.writerow(header)  # Menulis header ke dalam file CSV

url = 'https://api.bukalapak.com/multistrategy-products'  # URL API untuk mengambil data produk
count = 0  # Inisialisasi variabel untuk menghitung jumlah produk

for page in range(1, 3):  # Melakukan pengulangan untuk mengambil beberapa halaman data
    parameter = {
        'keywords': 'sepatu',  # Kata kunci pencarian produk
        'limit': 50,  # Jumlah produk yang ingin diambil per halaman
        'offset': 50,  # Mengatur posisi awal indeks produk
        'facet': True,
        'page': 2,  # Nomor halaman yang ingin diambil
        'shouldUseSeoMultistrategy': False,
        'isLoggedIn': False,
        'show_search_contexts': True,
        'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjY291bnRzLmp3dC5hY2Nlc3MtdG9rZW4iLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmJ1a2FsYXBhay5jb20vIiwic3ViIjoiMjMxZDRhODY5MDVmMGYyNjJjNWUwM2ZjIiwiYXVkIjpbImh0dHBzOi8vYWNjb3VudHMuYnVrYWxhcGFrLmNvbSIsImh0dHBzOi8vYXBpLmJ1a2FsYXBhay5jb20iLCJodHRwczovL2FwaS5zZXJ2ZXJtaXRyYS5jb20iXSwiZXhwIjoxNjg2ODkyNTAyLCJuYmYiOjE2ODY4ODAwODIsImlhdCI6MTY4Njg4MDA4MiwianRpIjoiYVM2bWRjeC1WUXZld2FYQkt5N1J2ZyIsImNsaWVudF9pZCI6IjIzMWQ0YTg2OTA1ZjBmMjYyYzVlMDNmYyIsInNjb3BlIjoicHVibGljIn0.NZQ6HEJslHmccKpkYAIz-qH-pCZsUVlA4VMtvZru71ouErTB6uQXUdObhLWWvaHZVRIsamkuhWuk4orEpXZbG6R5JgsBeSljGg9kB362idrxNrk_ilPQhqYGSWPVotwpT0aqxR9C01ArfGb3xSlMU92EFw-rWKz2_WbfoQAVI5mGwyT9VWCqzeJr2tIte3JRBbfSNpLrixE4kioFpyiTTz1cZscRZzWLigYMsYBYtu-pbSo-ErkBqUdefeqDMr3KaomkxNGRBmbNZi8NJoQS3UBqxCrkk_NdBJ3t9d45GgvySjKIu23xsVLm-vqycetyc9AUg2D73w1BuSWAfk4_3g'
        # Access token untuk otentikasi
    }  # Menentukan parameter untuk permintaan API

    r = requests.get(url, params=parameter).json()  # Mengirim permintaan GET ke API dan mengambil respons dalam format JSON

    products = r['data']  # Mengambil data produk dari respons

    for p in products:  # Melakukan pengulangan untuk setiap produk
        nama = p['name']  # Mengambil nama produk
        harga = p['price']  # Mengambil harga produk
        alamat = p['store']['address']['city']  # Mengambil alamat toko

        count += 1  # Menambah jumlah produk

        print('No:', count, 'nama:', nama, 'harga:', harga, 'alamat', alamat)  # Menampilkan informasi produk di layar

        write = csv.writer(open('hasil/{}.csv'.format(key), 'a', newline=''))  # Membuka file CSV dalam mode append
        data = [nama, harga, alamat]  # Membuat data produk
        write.writerow(data)  # Menulis data produk ke dalam file CSV


# In[22]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('hasil/sepatu.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Membaca header
    for row in reader:
        data.append(row)

# Menyiapkan data yang diperlukan untuk grafik
x = range(1, len(data) + 1)  # Nilai x (misalnya nomor entri)
harga = [float(row[1]) for row in data]  # Nilai harga

# Grafik Batang (Bar Plot)
plt.figure(figsize=(8, 6))
plt.bar(x, harga, color='green', alpha=0.7)
plt.xlabel('Nomor Entri')
plt.ylabel('Harga')
plt.title('Grafik Batang Harga Sepatu')
plt.grid(True)

# Menyimpan gambar grafik batang dengan latar belakang putih
plt.savefig('grafik_batang_sepatu.png')

# Menampilkan gambar grafik batang
plt.show()


# In[18]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('hasil/sepatu.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Membaca header
    for row in reader:
        data.append(row)

# Menyiapkan data yang diperlukan untuk histogram
harga = [float(row[1]) for row in data]  # Nilai harga

# Histogram
plt.figure(figsize=(8, 6))
plt.hist(harga, bins=10, color='purple', edgecolor='black')
plt.xlabel('Harga')
plt.ylabel('Frekuensi')
plt.title('Histogram Harga Sepatu')
plt.grid(True)

# Menyimpan gambar histogram
plt.savefig('histogram_sepatu.png')

# Menampilkan gambar histogram
plt.show()


# In[6]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('hasil/sepatu.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Membaca header
    for row in reader:
        data.append(row)

# Menghitung jumlah produk berdasarkan alamat
alamat_counts = {}
for row in data:
    alamat = row[2]
    if alamat in alamat_counts:
        alamat_counts[alamat] += 1
    else:
        alamat_counts[alamat] = 1

# Persiapan data untuk pie chart
labels = list(alamat_counts.keys())
counts = list(alamat_counts.values())

# Pie chart
plt.figure(figsize=(8, 6))
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Distribusi Produk Berdasarkan Alamat')
plt.show()


# In[12]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('hasil/sepatu.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Membaca header
    for row in reader:
        data.append(row)

# Menyiapkan data yang diperlukan untuk line chart
x = range(1, len(data) + 1)  # Nilai x (misalnya nomor entri)
harga = [float(row[1]) for row in data]  # Nilai harga

# Line chart
plt.figure(figsize=(8, 6))
plt.plot(x, harga, color='blue', marker='o', linestyle='-', linewidth=2)
plt.xlabel('Nomor Entri')
plt.ylabel('Harga')
plt.title('Diagram Garis Harga Sepatu')
plt.grid(True)

# Menyimpan gambar diagram garis
plt.savefig('diagram_garis_sepatu.png')

# Menampilkan gambar diagram garis
plt.show()


# In[15]:


import csv
import matplotlib.pyplot as plt

# Membaca data dari file CSV
data = []
with open('hasil/sepatu.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Membaca header
    for row in reader:
        data.append(row)

# Menyiapkan data yang diperlukan untuk scatter plot
harga = [float(row[1]) for row in data]  # Harga
alamat = [row[2] for row in data]  # Alamat

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(harga, alamat, color='blue', marker='o')
plt.xlabel('Harga')
plt.ylabel('Alamat')
plt.title('Scatter Plot Harga dan Alamat Sepatu')
plt.grid(True)

# Menyimpan gambar scatter plot
plt.savefig('scatter_plot.png')

# Menampilkan gambar scatter plot
plt.show()


# In[ ]:




