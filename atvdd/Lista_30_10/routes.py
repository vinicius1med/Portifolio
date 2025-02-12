from flask import Flask, render_template, Blueprint

lista_30_10_bp = Blueprint('lista_30_10', __name__, template_folder='templates', static_folder='static')

@lista_30_10_bp.route("/home_lista_30_10")  
def home_lista_30_10():
    return render_template("home_lista_30_10.html")

@lista_30_10_bp.route("/ex1_lista_30_10")  
def ex1_lista_30_10():
    return render_template("ex1_lista_30_10.html")

@lista_30_10_bp.route("/ex2_lista_30_10")  
def ex2_lista_30_10():
    return render_template("ex2_lista_30_10.html")

@lista_30_10_bp.route('/ex3_lista_30_10')
def ex3_lista_30_10():
    data = [
        {"id": i, "name": f"Name {i}", "surname": f"Surname {i}", "email": f"email{i}@domain.com"}
        for i in range(1, 998)
    ]
    return render_template('ex3_lista_30_10.html', data=data)

@lista_30_10_bp.route("/curriculum_vinicius")  
def curriculum_vinicius():
    return render_template("vinicius.html")

@lista_30_10_bp.route("/curriculum_caio")  
def curriculum_caio():
    return render_template("caio.html")

@lista_30_10_bp.route("/curriculum_isabelle")  
def curriculum_isabelle():
    return render_template("isabelle.html")

@lista_30_10_bp.route("/curriculum_franciele")  
def curriculum_franciele():
    return render_template("franciele.html")

@lista_30_10_bp.route("/curriculum_nathan")  
def curriculum_nathan():
    return render_template("nathan.html")

@lista_30_10_bp.route("/contact_lista_30_10")  
def contact_lista_30_10():
    return render_template("contact_lista_30_10.html")

if __name__ == "__main__":
    app.run(debug=True)
    


