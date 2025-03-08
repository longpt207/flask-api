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
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
