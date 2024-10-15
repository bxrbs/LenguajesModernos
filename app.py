from flask import Flask, render_template, request, redirect, url_for
import pymysql
from dbconfig import getDBConnection


app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    connection = getDBConnection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT ID, album, artista FROM albumes")
        registro = cursor.fetchall()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        registro = []
    finally:
        cursor.close()
        connection.close()

    return render_template('form.html', contacts=registro)

@app.route('/', methods=['POST'])
def submit():
    album = request.form['album']
    artista = request.form['artista']

    connection = getDBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO albumes (album, artista) VALUES (%s,%s)", (album, artista))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=3000, debug=True)