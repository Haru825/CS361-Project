from google_trans_new import google_translator
import sys, getopt
import webbrowser
import os

def batext(tatext,language):
    #print(googletrans.LANGUAGES)

    translator = google_translator()
    takentext= str(tatext)
    lang=str(language)
    #lang = 'es'
    #out = "hi"
    out=translator.translate(takentext, lang)
    #print("Original Text:", out.origin)
    #print("Translated Text:", out.text)
    return out

if __name__ == "__main__":
    pie=batext('hi','es')
    print(pie)



