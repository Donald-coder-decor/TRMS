from flask import Flask, jsonify
from controller import first_page_controller as fc
from flask_cors import  CORS

app = Flask(__name__)
CORS(app)
fc.route(app)

if __name__ == '__main__':
    app.run(debug=True)
