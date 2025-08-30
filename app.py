from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Urls de la Api

API_ALEATORIO = "https://dog.ceo/api/breeds/image/random"
API_POR_RAZA = "https://dog.ceo/api/breed/{}/images/random"
API_TODAS_RAZAS = "https://dog.ceo/api/breeds/list/all"

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/razas")
def obtener_razas():
    respuesta = requests.get(API_TODAS_RAZAS).json()
    return jsonify(sorted(respuesta["message"].keys()))

@app.route("/perro")
def obtener_perro():
    raza = request.args.get("raza")
    if raza:
        url = API_POR_RAZA.format(raza)
    else:
        url = API_ALEATORIO

    respuesta = requests.get(url).json()
    return jsonify({"imagen": respuesta["message"]})

if __name__ == "__main__":
    app.run(debug=True)