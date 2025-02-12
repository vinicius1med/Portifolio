from flask import Blueprint, render_template, request

lista_06_11_bp = Blueprint('lista_06_11', __name__, template_folder='templates', static_folder='static')

@lista_06_11_bp.route('/ex1_lista_06_11')
def ex1_lista_06_11():
    return render_template('ex1_lista_06_11.html')

@lista_06_11_bp.route('/ex6_lista_06_11')
def ex6_lista_06_11():
    return render_template('ex6_lista_06_11.html')

@lista_06_11_bp.route('/logged', methods=['POST'])
def logged():
    user_value = request.form['user']
    key_value = request.form['key']

    return render_user_form(user_value, key_value)

def render_user_form(user_value, key_value):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User info</title>
    </head>
    <body>
        <h1>User info (Exercices 4 and 5)</h1>
        <form>
            <label for="user">User:</label><br>
            <input type="text" id="user" name="user" value="{user_value}" disabled><br><br>
            <label for="key">Password:</label><br>
            <input type="text" id="key" name="key" value="{key_value}" disabled><br><br>
        </form>
        <a href="/lista_06_11/ex1_lista_06_11">Back</a>
    </body>
    </html>
    """
    return html_content