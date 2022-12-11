import flask
from flask import Flask, request, render_template
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

Credentials = ServiceAccountCredentials.from_json_keyfile_name(r"claves.json", scope)
cliente = gspread.authorize(Credentials)

sheet = cliente.open("Estacionamientos Database").sheet1
x = sheet.acell("A1").value
x = int(x)
print(x)



app = Flask(__name__)   


@app.route('/')
def inicio():
    while True:
        x = sheet.acell("A1").value
        x = int(x)
        print(x)
            
        if x==1:
            print(0)
        else:
            print(1)    

        return render_template("index.html", x=x)
        time.sleep(2)

  





if __name__ == '__main__':
    app.run(debug=True)

