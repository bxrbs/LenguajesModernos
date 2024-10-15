from flask import Flask, render_template, request, redirect, url_for
from app import app
from dbconfig import getDBConnection
import pymysql


@app.route('/')
def index():
    connection = getDBConnection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * FROM usuario")
        contacts = cursor.fetchall()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        contacts = []
    finally:
        cursor.close()
        connection.close()

    return render_template('form.html', contacts=contacts)

@app.route('/', methods=['POST'])
def submit():
    album = request.form['album']
    artista = request.form['artista']

    connection = getDBConnection()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO usuario (album, artista) VALUES (%s,%s)", (album, artista))
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('index'))    


if __name__ == "__main__":
    app.run(debug=True)