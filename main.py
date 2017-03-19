# -*- coding: utf-8 -*-
DEFAULT_PORT = 5000
ADDITIVE_FOR_UID = 1000

try:
    from os import getuid

except ImportError:
    def getuid():
        return DEFAULT_PORT - ADDITIVE_FOR_UID

import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main_page.html')
@app.route('/bts.html')
def bts():
    return render_template('bts.html') 
@app.route('/contacts.html')
def contacts():
    return render_template('contacts.html') 
@app.route('/dmitr.html')
def dmitr():
    return render_template('dmitr.html') 
@app.route('/download_page.html')
def download_page():
    return render_template('download_page.html') 
@app.route('/reference.html')
def reference():
    return render_template('reference.html') 
@app.route('/tutorial.html')
def tutorial():
    return render_template('tutorial.html') 
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/index.html', methods=['POST'])
def search():
    key = request.form["key_word"]
    key = key.lower()
    i = 0
    for word in all_words:  
        if key == list(word.keys())[0]:
            result = list(word.values())[0]
        else:
            i += 1        
    if i >= len(all_words):
        result = 'Слово не найдено'    
    return render_template('/index.html', key=key, result=result)
     
def open_dict(path):
    f = open(path,'r',encoding = 'utf-8')
    _dict = f.read().split('<superEntry>')
    f.close()
    return _dict

def fine_dict(_dict):
    all_words = []
    for art in _dict:      
        if art == '':
            _dict.remove(art)
        else:
            art1 = art#.split('\n')
            #tags = []
            #for line in art1:
                #if '<' not in line:
                 #   line = '<p>'+line+'</p>'
                #open_tag = re.findall('^<[0-9A-z\s"=]+>',line)
                #for tag in open_tag:
                 #   line = line.replace(tag,'<hr>'+tag)
                #tags.append(line)
            #art1 = '\n'.join(tags)
            m = re.search('<form type="headword">\n.+',art)
            if m != None:
                word = m.group().lower()
                word = re.sub('[^А-яЁё\-]', '',word)
                all_words.append({word:'<superEntry>\n'+art1})
    return all_words

_dict = open_dict(r'BTS_7.txt')        
all_words = fine_dict(_dict)

if __name__ == '__main__':
    app.run(port=getuid() + ADDITIVE_FOR_UID, debug=True)
          