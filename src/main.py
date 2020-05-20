from flask import Flask, render_template, request
import re
from match import *
from translate import *
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/output', methods=['GET','POST'])
def choice():
    if(request.method == 'POST'):
        jenis = request.form.get('jenis')
        metode = request.form.get('metode')
        sentence = request.form['sentence']
        return result(jenis, metode, sentence)

def result(jenis, metode, sentence):
    if(jenis == "ITS"):
        hasil = indoToSunda(metode, sentence)
    elif(jenis == "STI"):
        hasil = sundaToIndo(metode, sentence)
    return render_template('show.html', met = metode, input = sentence, hsl = hasil)

if __name__ == '__main__':
    app.run()