from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def read_root():
    return jsonify({"message": "Hello World"})

@app.route("/items/<int:item_id>", methods=["GET"])
def read_item(item_id):
    q = request.args.get("q")
    return jsonify({"item_id": item_id, "q": q})

@app.route("/items", methods=["POST"])
def create_item():
    data = request.json
    item_name = data.get("name")
    item_price = data.get("price")
    
    if item_name is None or item_price is None:
        return jsonify({"error": "Invalid input"}), 400
    
    twice_price = item_price * 2
    return jsonify({"item_name": item_name, "twice_price": twice_price})

if __name__ == "__main__":
    app.run(debug=True)
