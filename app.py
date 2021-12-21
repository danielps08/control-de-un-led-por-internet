import pyrebase                                           #importar la libreria pyrebase
from flask import Flask, render_template, request         #importar el objeto flask y librerias necesarias

app = Flask(__name__)                                     #crear una instancia de aplicacion flask                                

config = {                                                #agregar la configuracion de firebase

    "apiKey": "AIzaSyApOH8UDyVn_FAC9swPGH1smcO3Hx0b2-s",
    "authDomain": "lab-remoto-solar.firebaseapp.com",
    "databaseURL": "https://lab-remoto-solar-default-rtdb.firebaseio.com",
    "projectId": "lab-remoto-solar",
    "storageBucket": "lab-remoto-solar.appspot.com",
    "messagingSenderId": "621925670253",
    "appId": "1:621925670253:web:51dd7ea82ecd033dca0e64",
    "measurementId": "G-3MDPK87N5D"

}

firebase = pyrebase.initialize_app(config)                #inicializar la aplicacion flask

db = firebase.database()                                  #conectarse a la base de datos
 
@app.route('/', methods=['GET', 'POST'])                  #crea una ruta url

def index():                                              #funcion de vista
    if request.method == 'POST':                           #verificacion si hay envio de datos
        if request.form['sub'] == 'on':                   #verificacion del nombre del dato enviado
            db.child("estado").update({"led" : True})     #modifica el valor de la variable led a True en la base de datos
        elif request.form['sub'] == 'off':                #verificacion del nombre del dato enviado
            db.child("estado").update({"led" : False})    #modifica el valor de la variable led a False en la base de datos
        return render_template('index.html')              #la funcion devuelve un archivo html
    return render_template('index.html')
   
if __name__ == '__main__':                              

    app.run(debug=True)                                   #iniciar el servidor web
