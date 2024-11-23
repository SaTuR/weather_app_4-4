from flask import Flask,render_template, request


import requests

app = Flask(__name__)

def get_weather_data(city:str):
    """
    Funcion que espera el nombre de la ciudad por parametro, para luego realizar un get a openweather
    para consultar el clima de la ciudad ingresada
    """
    API_KEY = '6440f9bd7422123f37a1e881b2ad6fa5'
    idioma = 'es'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}'
    r = requests.get(url).json()
    return r

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '',cod = '')

    ciudad= request.form.get('txtCiudad')
    if ciudad:
        data=get_weather_data(ciudad) #lo que trae el api
        cod=data.get('cod')
        if cod != 200:
            return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '' , cod = cod)
        
        humedad=data.get('main').get('humidity')
        presion=data.get('main').get('pressure')
        descripcion=data.get('weather')[0].get('description')
        icon=data.get('weather')[0].get('icon')
        return render_template('index.html', ciudad=ciudad, humedad=humedad,presion=presion, descripcion=descripcion, icon = icon , cod = cod)
    else:
        return render_template('index.html', ciudad='', humedad='',presion='', descripcion='', icon = '',cod = '')


if __name__ == "__main__":
    app.run(debug=True)