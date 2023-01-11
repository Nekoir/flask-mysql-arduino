from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask (__name__)

# Connect to the database

cnx = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='S@kur@514',
    database='arduino'
)

@app.route('/data')
def data():
    cursor = cnx.cursor()
    query = "SELECT timestamp, moisture FROM sensorsdata"
    cursor.execute(query)
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({
            'timestamp': row[0],
            'moisture': row[1],
        })
    # Return the data as a JSON object
    return jsonify(data)

@app.route('/')
def index():
    # Retrieve data from the database
    with cnx.cursor() as cursor:
        sql = "SELECT * FROM sensorsdata"
        cursor.execute(sql)
        result = cursor.fetchall()

    # Render the template and pass the data to the template
    return render_template('dashboard.html', data=result, name="Hustling Dinos")

@app.route('/home')
def home():
    return render_template('home.hmtl')

if __name__ == '__main__':
    app.run()