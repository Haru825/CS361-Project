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

def csvtext(tatext, language):
    translator = google_translator()
    takentext= str(tatext)
    lang=str(language)
    out=translator.translate(tatext, language)
    csv_columns=['Original Text','Language','Translation']
    langdic={
        "Original text":tatext,
        "Language":lang,
        "Translation":out
    }
    
    with open('translate.csv', 'w') as f:
        for key in langdic.keys():
            f.write("%s, %s\n" % (key, langdic[key]))
    

if __name__ == "__main__":
    indict = {}
    with open('file.csv', mode='r') as csvFile:
        reader=csv.reader(csvFile)
        dict_from_csv={rows[0]:rows[1] for rows in reader}
    ntext=dict_from_csv["Original"]
    lang=dict_from_csv["Language"]

    pie=csvtext(ntext.lstrip(" "),lang.lstrip(" "))
    
