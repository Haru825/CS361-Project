from google_trans_new import google_translator
import sys, getopt
import webbrowser
import os
import json
import csv

def batext(tatext,language):
    translator = google_translator()
    takentext= str(tatext)
    lang=str(language)
    out=translator.translate(takentext, lang)
    #print("Original Text:", out.origin)
    #print("Translated Text:", out.text)
    
    return out

def jsontext(tatext,language):
    translator = google_translator()
    takentext= str(tatext)
    lang=str(language)
    out=translator.translate(takentext, lang)
    
    langdic={
        "Original text": takentext,
        "Language": lang,
        "New text": out
    }
    return json.dumps(langdic)

def csvtext(tatext):
    translator = google_translator()
    takentext= str(tatext)
    lang="nl"
    out=translator.translate(takentext, lang)
    csv_columns=['Original Text','Language','Translation']
    langdic={
        "Original text": takentext,
        "Language": lang,
        "New text": out
    }
    
    with open('translate.csv', 'w') as f:
        for key in langdic.keys():
            f.write("%s, %s\n" % (key, langdic[key]))

if __name__ == "__main__":
    pie=batext('hi','es')
    print(pie)
    pie=jsontext('hi','es')
    print(pie)
    pie=csvtext('hi')
    print(pie)



