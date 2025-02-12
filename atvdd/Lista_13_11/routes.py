from flask import Flask, render_template, request, redirect, url_for, jsonify, Blueprint

lista_13_11_bp = Blueprint('lista_13_11', __name__, template_folder='templates', static_folder='static')

@lista_13_11_bp.route('/ex1a5_lista_13_11')
def ex1a5_lista_13_11():
    return render_template('ex1a5_lista_13_11.html')

@lista_13_11_bp.route('/logged', methods=['POST'])
def logged():
    try:
        user_value = request.form.get('user')
        key_value = request.form.get('key')

        if not user_value or not key_value:
            return jsonify({"error": "Both fields (User and Password) are required."})

        if user_value != "user123" or key_value != "key123":
            return jsonify({"error": "Incorrect username or password."})

        return jsonify({"success": True, "redirect": url_for('lista_13_11.user_info', user=user_value, key=key_value)})
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"})

@lista_13_11_bp.route('/user_info')
def user_info():
    user_value = request.args.get('user')
    key_value = request.args.get('key')

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
        <h1>User info</h1>
        <form>
            <label for="user">User:</label><br>
            <input type="text" id="user" name="user" value="{user_value}" disabled><br><br>
            <label for="key">Password:</label><br>
            <input type="text" id="key" name="key" value="{key_value}" disabled><br><br>
        </form>
        <a href="/lista_13_11/ex1a5_lista_13_11">Back</a>
    </body>
    </html>
    """
    return html_content
