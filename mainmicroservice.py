from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from currency import countryCurrency

app = Flask(__name__)
api = Api(app)
CORS(app)


class CountryCurrency(Resource):
    def get(self, code):
        """
        Takes in a country 2 digit code and returns the currency that country uses.
        """
        output = countryCurrency(code)
        return {
            'input': code,
            'output': output
        }


api.add_resource(CountryCurrency, '/<code>')

if __name__ == '__main__':
    app.run(debug=True)
