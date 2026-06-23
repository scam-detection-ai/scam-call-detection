from flask import Flask, request
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return """
    <h2>Scam Call Detection</h2>
    <form action="/predict" method="post">
        Call Duration: <input name="duration"><br><br>
        Frequency: <input name="frequency"><br><br>
        Complaints: <input name="complaints"><br><br>
        <input type="submit" value="Check">
    </form>
    """

@app.route("/predict", methods=["POST"])
def predict():
    duration = int(request.form["duration"])
    frequency = int(request.form["frequency"])
    complaints = int(request.form["complaints"])

    result = model.predict([[duration, frequency, complaints]])

    if result[0] == 1:
        return "⚠️ Scam Call Detected"
    else:
        return "✅ Safe Call"

app.run(debug=True)