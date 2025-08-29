from flask import Flask, render_template, request
import requests

app = Flask(__name__)

DOG_API_RANDOM = "https://dog.ceo/api/breeds/image/random" # perros random
DOG_API_BY_BREED = "https://dog.ceo/api/breed/{}/images/random" # perros por raza
DOG_API_BREEDS = "https://dog.ceo/api/breeds/list/all" # lista de razas

@app.route("/", methods=["GET", "POST"])
def index():
    breeds = get_breeds()
    image_url = None

    if request.method == "POST":
        breed = request.form.get("breed")
        if breed:
            image_url = requests.get(DOG_API_BY_BREED.format(breed)).json()["message"]
        else:
            image_url = requests.get(DOG_API_RANDOM).json()["message"]

    return render_template("index.html", breeds=breeds, image_url=image_url)

def get_breeds():
    response = requests.get(DOG_API_BREEDS).json()
    return sorted(response["message"].keys())

if __name__ == "__main__":
    app.run(debug=True)