from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		user = request.form["name"]
		return redirect(url_for("user", usr=user))

	return render_template("login.html")

@app.route("/<usr>")
def user(usr):
	return f"<p>{usr}</p>"

@app.route("/admin/Payment_Order")
def Payment_Order():
	return render_template("Payment_Order.html")

if __name__ == "__main__":
	app.run(debug=True)
