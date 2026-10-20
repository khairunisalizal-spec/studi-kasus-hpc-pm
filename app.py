from flask import Flask, render_template, request, jsonify
import csv
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

app = Flask(__name__)
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "pm25_demo.csv")
FEATURES = ["suhu_c", "kelembapan_pct", "kecepatan_angin_ms", "indeks_lalu_lintas"]

def load_data():
    X, y = [], []
    with open(DATA_PATH, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            X.append([float(row[key]) for key in FEATURES])
            y.append(float(row["pm25_ug_m3"]))
    return X, y

X, y = load_data()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
MODEL_MAE = round(mean_absolute_error(y_test, predictions), 2)
MODEL_R2 = round(r2_score(y_test, predictions), 2)

@app.route("/")
def home():
    return render_template("index.html", mae=MODEL_MAE, r2=MODEL_R2, samples=len(y))

@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        payload = request.get_json(force=True)
        values = [float(payload[key]) for key in FEATURES]
        if not (0 <= values[1] <= 100):
            return jsonify({"error": "Kelembapan harus berada pada rentang 0–100%."}), 400
        if values[2] < 0:
            return jsonify({"error": "Kecepatan angin tidak boleh negatif."}), 400
        if not (0 <= values[3] <= 100):
            return jsonify({"error": "Indeks lalu lintas harus berada pada rentang 0–100."}), 400
        estimate = max(0, float(model.predict([values])[0]))
        if estimate <= 15:
            category = "Relatif rendah"
            advice = "Tetap pantau kualitas udara dan ikuti informasi resmi setempat."
        elif estimate <= 35:
            category = "Perlu diperhatikan"
            advice = "Kurangi aktivitas berat di luar ruangan bila sensitif terhadap polusi."
        else:
            category = "Tinggi pada model demo"
            advice = "Periksa pengukuran resmi sebelum mengambil keputusan kesehatan."
        return jsonify({
            "pm25": round(estimate, 1),
            "category": category,
            "advice": advice,
            "note": "Ini estimasi dari data sintetis untuk pembelajaran, bukan prakiraan resmi."
        })
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Isi semua kolom dengan angka yang valid."}), 400

if __name__ == "__main__":
    app.run(debug=True)
