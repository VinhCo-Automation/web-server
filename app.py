from flask import Flask, render_template, request, jsonify
import mysql.connector
from db_config import db_config

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route("/")
def index():
    return render_template("sensor.html", data=get_data("sensor"))

@app.route("/sensor")
def sensor():
    return render_template("sensor.html", data=get_data("sensor"))

@app.route("/alarm")
def alarm():
    return render_template("alarm.html", data=get_data("alarm"))

@app.route("/run")
def run():
    return render_template("run.html", data=get_data("run"))

def get_data(table):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    db.close()
    return rows

@app.route("/add/<table>", methods=["POST"])
def add_row(table):
    data = request.get_json()
    db = get_db_connection()
    cursor = db.cursor()
    if table == "sensor":
        cursor.execute("INSERT INTO sensor (ID_Device, Date, Time, Temp, Hum) VALUES (%s, %s, %s, %s, %s)",
                       (data["ID_Device"], data["Date"], data["Time"], data["Temp"], data["Hum"]))
    elif table == "alarm" or table == "run":
        cursor.execute(f"INSERT INTO {table} (ID_Device, Date, Time, Var) VALUES (%s, %s, %s, %s)",
                       (data["ID_Device"], data["Date"], data["Time"], data["Var"]))
    db.commit()
    db.close()
    return jsonify({"success": True})

@app.route("/delete/<table>")
def delete_row(table):
    id_device = request.args.get("ID_Device")
    date = request.args.get("Date")
    time = request.args.get("Time")
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE ID_Device=%s AND Date=%s AND Time=%s", (id_device, date, time))
    db.commit()
    db.close()
    return jsonify({"success": True})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

