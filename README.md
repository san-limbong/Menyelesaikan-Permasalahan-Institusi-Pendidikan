# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

Nah, sebagai calon data scientist masa depan Anda diminta untuk membantu Jaya Jaya Institut dalam menyelesaikan permasalahannya. Selain itu, mereka juga meminta Anda untuk membuatkan dashboard agar mereka mudah dalam memahami data dan memonitor performa siswa. 

### Permasalahan Bisnis
1. Institusi memiliki permasalahan dalam mengelola siswa yang cukup banyak tidak menyelesaikan pendidikan alias dropout. 

2. Institusi memerlukan dashboard untuk membantu memonitori berbagai faktor dan latar belakang dari masing - masing siswanya untuk dapat memprediksi apakah siswa tersebut berpotensi dropout sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek
1. Menganalisis kebutuhan (requirements) insitusi yang terdiri atas tahapan
- Business Understanding
- Data Understanding
2. Mengembangkan model, yang terdiri atas tahapan
- Data preparation
- Modeling
- Model Evaluation
- Dashboard 
3. Membangun model yang dapat memprediksi siswa berpotensi untuk dropout atau tidak.

### Persiapan

Sumber data: Sumber data: [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
1. Pengguna telah menginstal Anaconda di komputer yang digunakan
2. Membuka terminal atau command prompt (cmd)
3. Buat Virtual Environment Baru:
```
conda create --name myenv python=3.8
conda activate myenv
```
4. Melakukan Install terhadap requirement:

```
pip install -r requirements.txt
```

5. Menjalankan jupyter notebook
6. Membuka app.py 
7. Menginput data yang ingin diprediksi sesuai dengan label yang tertera pada website.
8. Mengisi semua data yang diperlukan dan tunggu hingga hasil prediksi keluar. 

- Metabase 
```
from sqlalchemy import create_engine

URL = "postgresql://postgres.jjcbnnkvcmoknjjtgpwc:JayaJayaInstitut123@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

engine = create_engine(URL)
trans_df.to_sql('student_data', engine)
```

```
Host : aws-0-ap-southeast-1.pooler.supabase.com
Database name : postgres
port: 6543
user : postgres.jjcbnnkvcmoknjjtgpwc
```

## Business Dashboard
Akses dashboard melalui tautan yang disediakan docker melalui [link](http://localhost:3000/public/dashboard/9058ef49-625a-4351-9d0d-b6128adf65ad)

![san-limbong dashboard](https://github.com/user-attachments/assets/5aa08409-e914-462b-b3e0-645580532fe2)


Analisis dashboard.
1. Salah satu penyebab terjadinya dropout disebabkan oleh biaya kuliah yang tinggi dengan persentase sebanyak 67,8%

2. Mata kuliah juga dapat merupakan salah satu faktor penyebab dropout. Berikut mata kuliah dengan jumlah dropout terbanyak:
- Management
- Nursing
- Journalism and Communication
- Tourism, dan
- Advertising and Management

3. Terdapat korelasi antara jumlah dropout dan waktu datang.
Berdasarkan data yang ditemukan, persentase siswa yang hadir malam hari cenderung lebih rentan dengan dropout.

4. Sebagai data cuplikan, rata - rata nilai dari siswa yang dropout (6-8) cenderung lebih rendah dari nilai rata - rata rekan sesama siswa (12) untuk semua mata kuliah.

5. Pada siswa yang mendapati beasiswa juga ditemukan dropout. Persentase paling banyak ditemukan pada siswa jurusan Animation and Multimedia Design diikuti jurusan Tourism.

6. Nilai masuk 120 - 140 rentan dengan siswa dropout.
7. Pekerjaan orang tua (Ayah - Ibu) atau keduanya memiliki pekerjaan yang sama orang tua, juga berpengaruh terhadap dropoutnya siswa. 
Berikut 4 pekerjaan peringkat tertinggi penghasil siswa dropout:
- Unskilled Workers
- Student
- Administrative staff
- Personal Services, Security and Safety Workers and Sellers 

## Menjalankan Sistem Machine Learning
Cobain sensasi memprediksi siswa dropout atau enggak [disini](https://isstudentdropout.streamlit.app/)

1. Pengguna telah menginstal Anaconda di komputer yang digunakan
2. Membuka terminal atau command prompt (cmd)
3. Buat Virtual Environment Baru:
```
conda create --name myenv python=3.8
conda activate myenv
```
4. Melakukan Install terhadap requirement:

```
pip install -r requirements.txt
```

5. Membuka app.py 
6. Menginput data yang ingin diprediksi sesuai dengan label yang tertera pada website.
7. Mengisi semua data yang diperlukan dan tunggu hingga hasil prediksi keluar. 


## Conclusion
1. Salah satu penyebab terjadinya dropout disebabkan oleh biaya kuliah yang tinggi.
2. Mata kuliah juga dapat merupakan salah satu faktor penyebab dropout.
3. Berdasarkan data yang ditemukan, persentase siswa yang hadir malam hari cenderung lebih rentan dengan dropout.
4. Nilai siswa yang dropout lebih rendah dari pada rata rata siswa umumnya.
5. Siswa berbeasiswa juga memiliki potensi untuk melakukan dropout.
6. Nilai masuk 120 - 140 rentan dengan siswa dropout.
7. Pekerjaan orang tua (Ayah - Ibu) atau keduanya memiliki pekerjaan yang sama orang tua, juga berpengaruh terhadap dropoutnya siswa. 

### Rekomendasi Action Items
1. Melakukan peninjauan terhadap biaya kuliah siswa apakah sudah tepat atau tidak.
2. Evaluasi dan Perbaiki Kondisi pengajaran pada waktu malam hari sehingga menurunkan terjadinya dropout.
3. Melakukan pengecekan terhadap latar belakang siswa, seperti pekerjaan orang tua serta nilai siswa sehingga dapat memantau terjadinya potensi dropout.
4. Siswa yang memiliki beasiswa juga ditemukan dropout, sehingga perlu meninjau kembali kebijakan beasiswa tersebut. 
