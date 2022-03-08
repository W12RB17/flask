from os import environ
from flask_mysqldb import MySQL
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

app.config['MYSQL_HOST'] = environ.get('AWS_SN')
app.config['MYSQL_USER'] = environ.get('AWS_UN')
app.config['MYSQL_PASSWORD'] = environ.get('AWS_PASSWORD')
app.config['MYSQL_DB'] = environ.get('AWS_DBNAME')

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/main_menu")
def main_menu():
    return render_template("main_menu.html")


@app.route("/create_user")
def create_user():
    return render_template("create_user.html")
    

@app.route("/change_password")
def change_password():
    return render_template("change_password.html")


@app.route("/delete_user")
def delete_user():
    return render_template("delete_user.html")


@app.route("/list_users")
def list_users():
    return render_template("list_users.html")

   
@app.route("/login", methods = ["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    login_query = cursor.fetchall()
    if login_query:
        #return redirect(url_for("management"))
        return render_template("main_menu.html")
    cursor.close()


@app.route("/create", methods = ['POST'])
def create():
    new_username = request.form['new_username']
    new_password = request.form['new_password']
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES(%s, %s)', (new_username, new_password))
    mysql.connection.commit()
    cursor.close()
    return render_template("create_user.html")


@app.route("/delete", methods = ['POST'])
def delete_use():
    delete_username = request.form['delete_username']
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM users WHERE username=%s', [delete_username])
    mysql.connection.commit()
    cursor.close()
    return render_template("delete_user.html")


@app.route("/change", methods = ['POST'])
def change_passwor():
    cp_username = request.form['cp_username']
    cp_password = request.form['cp_password']
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE users SET password = %s WHERE username = %s', (cp_password, cp_username))
    mysql.connection.commit()
    cursor.close()
    return render_template("change_password.html")

@app.route("/list_user", methods=['POST'])
def list_user():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users')
    query = cursor.fetchall()
    if query:
        return render_template("list_users.html", users=query)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)