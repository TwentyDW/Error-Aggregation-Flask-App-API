from flask import Flask, render_template
from werkzeug.wrappers import BaseResponse as Response
from werkzeug.datastructures import Headers
import api

"""class Error_Without_Details:
	def __init__(self, error_obj_instance):
		self.hash = error_obj_instance.hash
		self.message_string = error_obj_instance.message_string
		self.first_occurrence = error_obj_instance.first_occurrence
		self.last_occurrence = error_obj_instance.last_occurrence
		self.count = error_obj_instance.count"""

app2 = Flask(__name__)

@app2.route("/")
def home():
	return render_template('home.html')

@app2.route("/list")
def list():
	json_array_of_jsons = api.get_jsons()
	h = Headers()
	h.add('Content-Type', 'application/json')
	resp = Response(response = json_array_of_jsons, headers = h, status = 200)
	return resp

@app2.route("/list/<string:provided_hash>")
def list_hash(provided_hash):
	detailed_json = api.get_detailed_json(provided_hash)
	if detailed_json:
		h = Headers()
		h.add('Content-Type', 'application/json')
		resp = Response(response = detailed_json, headers = h, status = 200	)
	else:
		resp = Response(response = "Error with given hash not found", status = 404)
	return resp
		
if __name__ == "__main__":
	app2.run(port=5001, debug=True)