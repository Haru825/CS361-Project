from myTranslate import*
from flask import Flask, request, render_template

app = Flask(__name__)

global texttran
global tvalue

@app.route('/')
def home():
   return render_template('project.html')

@app.route('/',methods=['POST'])
def save_text():
   #texttran = request.form.get('origText')
   #tvalue=request.form.get('value')
   texttran = "Hi"
   tvalue = "es"
   nt = batext(texttran,tvalue)
   return nt   


if __name__ == '__main__':
   app.run(debug=on)