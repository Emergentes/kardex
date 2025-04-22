from flask import Flask,request,redirect,url_for,render_template
import sqlite3

app = Flask(__name__)

# Conexion a la base de datos
def get_db_connection():
    conn = sqlite3.connect("bd_kardex.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor =  conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS personal(
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            fecha_nac DATE NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()
# Creando la tabla
init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/personal")
def personal():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personal")
    personal = cursor.fetchall()
    return render_template("personal.html",personal = personal)

if __name__ == '__main__':
    app.run(debug=True)