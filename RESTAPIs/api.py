from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloFresco(Resource):
    def get(self):
        return {'message':'Welcome to Fresco play!!!'},201,{'response_header1':'header-message-sai'}

api.add_resource(HelloFresco,'/')

if __name__ == '__main__':
    app.run()
