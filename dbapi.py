from flask import *
def get_DB_records(table:str):
    import mysql.connector
    import json

    # Connect to MySQL database
    mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
    )

    mycursor = mydb.cursor()

    sql = f"SELECT * FROM {table}"
    mycursor.execute(sql)

    rows = mycursor.fetchall()
    results = []
    columns = [column[0] for column in mycursor.description]
    for row in rows:
        result = {}
        for i in range(len(columns)):
            result[columns[i]] = row[i]
        results.append(result)

    # Convert the list of dictionaries to a JSON string
    json_results = json.dumps(results,default=str)
    return json_results
app = Flask(__name__)


@app.route('/<table>')
def data(table):
    return jsonify(get_DB_records(table))

app.run()
