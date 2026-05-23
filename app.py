from flask import Flask, render_template, request

app = Flask(__name__)

def predict_sales(ads):
    return ads * 10

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":
        ads = float(request.form["ads"])
        prediction = predict_sales(ads)

    return render_template(
        "home.html",
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)