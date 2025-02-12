from flask import Flask, render_template, redirect, url_for
from atvdd.Lista_30_10.routes import lista_30_10_bp
from atvdd.Lista_06_11.routes import lista_06_11_bp
from atvdd.Lista_13_11.routes import lista_13_11_bp

app = Flask(__name__)

app.register_blueprint(lista_30_10_bp, url_prefix='/lista_30_10')
app.register_blueprint(lista_06_11_bp, url_prefix='/lista_06_11')
app.register_blueprint(lista_13_11_bp, url_prefix='/lista_13_11')

@app.route("/")  
def home():
    return render_template("home.html")

@app.route("/class_04_exercices")  
def class04():
    return redirect(url_for('lista_30_10.home_lista_30_10'))

@app.route("/class_05_exercices")
def class05():
    return redirect(url_for('lista_06_11.ex1_lista_06_11'))

@app.route("/class_06_exercices")
def class06():
    return redirect(url_for('lista_13_11.ex1a5_lista_13_11'))

if __name__ == "__main__":
    app.run(debug=True)