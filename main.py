from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Kết nối MySQL trên AWS
def get_db_connection():
    return pymysql.connect(
        host="your-aws-db-endpoint",
        user="your-db-user",
        password="your-db-password",
        database="your-db-name",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/users', methods=['GET'])
def get_users():

    return jsonify(status = 200)

if __name__ == "__main__":
    app.run(debug=True)
