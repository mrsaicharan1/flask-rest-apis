from flask import Flask, request
from flask_restful import Resource, Api, reqparse,fields,marshal_with

app = Flask(__name__)
api = Api(app)

# parser = reqparse.RequestParser()
# parser.add_argument('principal_amount',type=float, help='Principal amount must be a number')
# parser.add_argument('period', type=int, help="No. of Years must be an integer")
# parser.add_argument('rate', type=float, help='Rate must be a number')

resource_fields = {
     'simple_interest': fields.Raw,
    'computed_on': fields.DateTime(dt_format='rfc822')
}

class SimpleInterest(Resource):
    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()

        p = float(request.form['principal_amount'])
        n = int(request.form['period'])
        r = float(request.form['rate'])

        si = (p*n*r)/100.0

        return {'simple_interest':si,'computed_on':dt.datetime.now()}

api.add_resource(SimpleInterest, '/simpleinterest/')

if __name__ == '__main__':
    app.run()
