from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from utils import irisprediction

app = Flask(__name__)
api = Api(app)

class Prediction(Resource):
	def get(self):

		parser = reqparse.RequestParser()
		parser.add_argument('slength', type=float, help='slength can not be converted')
		parser.add_argument('swidth', type=float, help='swidth can not be converted')
		parser.add_argument('plenght', type=float, help='plenght can not be converted')
		parser.add_argument('pwidth', type=float, help='pwidth can not be converted')
		args = parser.parse_args()

		prediction = irisprediction.predict([
		  args['slength'],
		  args['swidth'],
		  args['plenght'],
		  args['pwidth']
		])

		# Return the prediction from irisprediction.py
		return {
		  'slength': args['slength'],
		  'swidth': args['swidth'],
		  'plenght': args['plenght'],
		  'pwidth': args['pwidth'],
		  'species': prediction
		}



api.add_resource(Prediction, '/prediction')


# Loop the application
if __name__ == '__main__':
	app.run(debug=False)
