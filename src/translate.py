import re
import random
from match import *

indonesia = []
sunda = []

# Membaca file kamus Indonesia-Sunda
def readIndoToSunda():
    with open('indonesia.txt') as filename:
        for line in filename:
            splitted = tuple(line.strip().split(' = '))
            indonesia.append(splitted)

# Membaca file kamus Sunda-Indonesia
def readSundaToIndo():
    with open('sunda.txt') as filename:
        for line in filename:
            splitted = tuple(line.strip().split(' = '))
            sunda.append(splitted)

# Memisahkan masukan per kata
def parsingSentence(masukan):
    inputList = re.findall("[\w]+|[.,!?;:]", str(masukan))
    return inputList

# Menghapus stop words
def clearPenekanan(masukan):
    stopWords = ["teh", "mah", "tea", "atuh"]
    for i in masukan[:]:
        if(i in stopWords):
            masukan.remove(i)
    return masukan

def addPenekanan(hasil, result, trans):
    teh = ['itu', 'tuh', 'saya', 'kamu', 'dia', 'mereka', 'kalian', 'kami', 'kita']
    if(result in teh):
        hasil.append('teh')
    elif(result == 'dong'):
        hasil.append('atuh')
    elif(result == 'apa', 'dimana', 'kapan'):
        temp = hasil[0:-1]
        temp.append('teh')
        hasil = temp[0:None]
        hasil.append(trans)
    return hasil

def concateHasil(hasil):
    fin = ""
    for i in range(len(hasil)):
        fin += hasil[i] + ' '
    return fin

# Metode pattern matching
def matchAlgo(choice, masukan, text):
    if(choice == "KMP"):
        idx = kmpMatch(masukan.lower(), text)
    elif(choice == "BM"):
        idx = bmMatch(masukan.lower(), text)
    elif(choice == "Regex"):
        idx = regexMatch(masukan.lower(), text)
    return idx

# Translate Sunda ke Indonesia
def sundaToIndo(choice, masukan):
    readSundaToIndo() # Membaca kamus
    parsed = parsingSentence(masukan) # Parsing kalimat
    result = clearPenekanan(parsed) # Menghapus stop words
    hasil = []
    for i in range(len(result)):
        found = False
        j = 0
        # Iterasi kamus untuk mencari kata yang bersesuaian sampai ditemukan atau kamus sudah selesai diiterasi
        while(not found and j<len(sunda)-1): 
            res = matchAlgo(choice, result[i].lower(), sunda[j][0])
            start = res[0]
            last = res[1]
            if(start == 0 and last == len(sunda[j][0])-1): # Jika ditemukan exact match
                found = True
                hasil.append(sunda[j][1])
            j += 1
        if(not found): # Jika tidak ditemukan, kata tersebut dituliskan apa adanya
            hasil.append(result[i])
    return concateHasil(hasil)

# Translate Indonesia ke Sunda
def indoToSunda(choice, masukan):
    needStopWords = ['saya', 'kamu', 'dia', 'mereka', 'kalian', 'kami', 'kita', 'dong', 'itu', 'tuh', 'apa', 'dimana', 'kapan']
    readIndoToSunda() # Membaca kamus
    result = parsingSentence(masukan) # Parsing kalimat
    hasil = []
    for i in range(len(result)):
        found = False
        penekanan = False
        j = 0
        # Iterasi kamus untuk mencari kata yang bersesuaian sampai ditemukan atau kamus sudah selesai diiterasi
        while(not found and j<len(indonesia)-1):
            res = matchAlgo(choice, result[i].lower(), indonesia[j][0])
            start = res[0]
            last = res[1]
            if(start == 0 and last == len(indonesia[j][0])-1): # Jika ditemukan exact match
                found = True
                hasil.append(indonesia[j][1])
                trans = indonesia[j][1]
            j += 1
        
        if(not penekanan and result[i] in needStopWords): # Jika kata membutuhkan penekanan
            penekanan = True
            hasil = addPenekanan(hasil, result[i], trans)
        elif(not found and not penekanan): # Jika kata tidak ditemukan dan tidak membutuhkan penekanan
            hasil.append(result[i])
    return concateHasil(hasil)