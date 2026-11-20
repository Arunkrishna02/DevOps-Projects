import os
import pymysql
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    return pymysql.connect(
        host=os.environ.get("DB_HOST", "calculator-db"),
        port=int(os.environ.get("DB_PORT", 3306)),
        user=os.environ.get("DB_USER", "calculator_user"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME", "calculator"),
        cursorclass=pymysql.cursors.DictCursor
    )


def save_calculation(operation, num1, num2, result):
    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            sql = """
                INSERT INTO calculations
                (operation, num1, num2, result)
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                sql,
                (operation, num1, num2, result)
            )

        connection.commit()

    finally:
        connection.close()


@app.route("/")
def home():
    return """
    <h1>Docker Calculator with MariaDB</h1>
    <p>Flask application connected to MariaDB.</p>
    <ul>
        <li>/add?a=10&b=5</li>
        <li>/subtract?a=10&b=5</li>
        <li>/multiply?a=10&b=5</li>
        <li>/health</li>
        <li>/history</li>
    </ul>
    """


@app.route("/add")
def add():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    result = a + b

    save_calculation("addition", a, b, result)

    return jsonify({
        "operation": "addition",
        "a": a,
        "b": b,
        "result": result
    })


@app.route("/subtract")
def subtract():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    result = a - b

    save_calculation("subtraction", a, b, result)

    return jsonify({
        "operation": "subtraction",
        "a": a,
        "b": b,
        "result": result
    })


@app.route("/multiply")
def multiply():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    result = a * b

    save_calculation("multiplication", a, b, result)

    return jsonify({
        "operation": "multiplication",
        "a": a,
        "b": b,
        "result": result
    })


@app.route("/history")
def history():
    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM calculations ORDER BY id DESC"
            )

            records = cursor.fetchall()

        return jsonify(records)

    finally:
        connection.close()


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
