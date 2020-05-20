# Simple Sundanese Translator
Simple Sundanese to Bahasa Indonesia translator using Pattern Matching

## Latar Belakang
Pada suatu hari, ada mahasiswa bernama Riyugan yang baru pindah ke Bandung. Pada awalnya dia mengalami kesulitan untuk bersosialisai dengan lingkungan sekitar karena orang-orang di lingkungannya yang baru hanya berbicara dalam bahasa Sunda. Beruntungnya Riyugan punya teman dari kampung halamannya, yaitu Anda, untuk diminta membuat penerjemah sederhana dari Bahasa Sunda ke Bahasa Indonesia begitu pula sebaliknya untuk memudahkan dirinya bersosialisasi dengan lingkungan barunya di Bandung.

## Contoh Kasus Uji
```
Sunda - Indonesia
Sunda : nami abdi Riyugan
Indonesia : nama saya Riyugan
```

```
Sunda - Indonesia
Sunda : abdi teh sanes jalma Bandung
Indonesia : saya bukan orang Bandung
```

```
Sunda - Indonesia
Sunda : anjeun sumping ti mana?
Indonesia : kamu tiba dari mana?
```

```
Indonesia - Sunda
Indonesia : nama saya Riyugan
Sunda : nami abdi teh Riyugan
```

```
Indonesia - Sunda
Indonesia : nama adik kamu siapa?
Sunda : nami rai anjeun teh saha?
```

```
Indonesia - Sunda
Indonesia : saya tidak bisa bahasa Sunda
Sunda : abdi teh henteu tiasa bahasa Sunda
```

## Requirement
1. Virtual environment (optional)
2. Python (3.5 or higher)
3. Flask
```bash
pip install flask
```

## Penggunaan
### Cara Menjalankan di Windows
1. Jalankan command prompt di direktori (src)
2. Run program dengan cara 'python main.py'
3. Copy address yang diberikan dan paste ke browser (Firefox/Chrome)

### Menggunakan translator
1. Pilih jenis translasi yang diinginkan: Indonesia-Sunda atau Sunda-Indonesia
2. Pilih metode pattern matching yang diinginkan: KMP, Boyer-Moore, atau Regex
3. Masukkan kalimat yang ingin diterjemahkan
4. Klik 'Terjemahkan'

## Link
Video demo untuk translator ini dapat dilihat di:
```
https://youtu.be/ktl_E1t2PYY
```