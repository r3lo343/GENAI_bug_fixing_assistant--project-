
from flask import Flask, render_template, request
from genai_engine import genai_fix

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    explanation = ""
    fixed_code = ""
    if request.method == "POST":
        code = request.form["code"]
        explanation, fixed_code = genai_fix(code)
    return render_template("index.html",
                           explanation=explanation,
                           fixed_code=fixed_code)

if __name__ == "__main__":
    app.run(debug=True)
