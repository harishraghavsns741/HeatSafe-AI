import os
from flask import Flask, render_template, request
from heat_risk import assess_heat_risk

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-only-change-me")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            temperature = float(request.form.get("temperature", ""))
            humidity = float(request.form.get("humidity", ""))
            if not (-10 <= temperature <= 60):
                raise ValueError("Temperature must be between -10°C and 60°C.")
            if not (0 <= humidity <= 100):
                raise ValueError("Relative humidity must be between 0% and 100%.")
            language = request.form.get("language", "en")
            result = assess_heat_risk(temperature, humidity, language)
            result["temperature"] = temperature
            result["humidity"] = humidity
        except (TypeError, ValueError) as exc:
            error = str(exc) or "Enter valid numeric values."
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=os.getenv("FLASK_DEBUG") == "1")
