from flask import Flask, request, jsonify

app = Flask(__name__)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@app.route("/api", methods=["POST"])
def calculate():
    try:
        data = request.get_json()
        number = data["number"]
        if not isinstance(data, dict):
            raise Exception("data must be a dictionary")
        if not data:
            raise Exception("data cannot be empty")
        if not number:
            raise Exception("number cannot be empty")
        if not isinstance(number, int):
            raise Exception("number must be an integer")
        operations = data["operations"]
        if not isinstance(operations, list):
            raise Exception("operations must be a list")
        if not operations:
            raise Exception("operations cannot be empty")
        if not all(isinstance(x, str) for x in operations):
            raise Exception("operations must contain only strings")
        if not all(x in ["factorial", "fibonacci"] for x in operations):
            raise Exception("operations must contain only 'factorial' or 'fibonacci'")
        result = {}

        if "factorial" in operations:
            result["factorial"] = factorial(number)

        if "fibonacci" in operations:
            result["fibonacci"] = fibonacci(number)

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run()
