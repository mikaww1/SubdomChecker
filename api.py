from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from main import check_subdomain, normalize

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()

    if not data or not data.get("subdomain"):
        return jsonify({"error": "No subdomain provided"}), 400

    subdomain = normalize(data["subdomain"].strip())
    if not subdomain:
        return jsonify({"error": "Invalid subdomain"}), 400

    try:
        result = check_subdomain(subdomain)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)