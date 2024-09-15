from flask import Flask, request, render_template
from googlesearch import search
import json

app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/search', methods=['POST'])
def search_google():
   klicova_slova = request.form["keywords"]
   vysledky_vyhledavani = []
   
   if klicova_slova == "":
      return render_template("nowords.html")

   else:
      for vysledek in search(klicova_slova):
         vysledky_vyhledavani.append(vysledek)

      with open("vysledky_vyhledavani.json", mode = "w", encoding = "utf-8") as file:
         json.dump(vysledky_vyhledavani, file)

   return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)
