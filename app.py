from flask import Flask, request, jsonify, render_template # Ajout de render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- CETTE PARTIE EST NOUVELLE ---
@app.route('/')
def home():
    # Flask va chercher ce fichier dans le dossier /templates
    return render_template('index.html')
# ---------------------------------

@app.route('/calculer', methods=['POST'])
def calculer():
    donnees = request.json
    nombre = donnees.get('nombre')
    
    # Sécurité si le nombre est vide
    if nombre is None:
        return jsonify({"resultat": 0})
        
    resultat = nombre * nombre
    return jsonify({"resultat": resultat})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)