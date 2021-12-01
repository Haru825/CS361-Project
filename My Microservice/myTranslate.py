#Created By: Susan Liu
#Class: CS361 Fall 2021
#Team: TEAM (Terrific Engineers Amateurs Mostly)
#Date: 10/5/2021

#libaries used to translate and change form of text
from google_trans_new import google_translator
import sys, getopt
import webbrowser
import os
import json
import csv


def normtext(tatext,language):
    translator = google_translator()
    takentext= str(tatext)
    lang=str(language)
    out=translator.translate(takentext, lang)


    
    return out

#change translation into json
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

#turn text into csv file
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
    
    #turn text into new csv file
    with open('translate.csv', 'w') as f:
        for key in langdic.keys():
            f.write("%s, %s\n" % (key, langdic[key]))
    

if __name__ == "__main__":
    indict = {}

    #open csv file in same folder as python and seperate 
    with open('file.csv', mode='r') as csvFile:
        reader=csv.reader(csvFile)
        dict_from_csv={rows[0]:rows[1] for rows in reader}
    ntext=dict_from_csv["Original"]
    lang=dict_from_csv["Language"]

    #make the translated text 
    pie=csvtext(ntext.lstrip(" "),lang.lstrip(" "))
    