from flask import Flask, render_template
app = Flask(__name__, template_folder='Templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/foto")
def about():
    return render_template("foto.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/produk")
def produk():
    return render_template("produk.html")

if __name__ == "__main__":
    app.run()