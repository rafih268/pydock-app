from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
  text = None
  if request.method == "POST":
    text = request.form.get("user_input")

  return render_template("index.html", text=text)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)