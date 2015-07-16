from flask import Flask, render_template
from werkzeug.wrappers import BaseResponse as Response
from werkzeug.datastructures import Headers
import api

app2 = Flask(__name__)

@app2.route("/") # url for table page
def home():
	return render_template('home.html')
	
@app2.route("/details.html") # url for displaying details
def details():
	return render_template('details.html')

@app2.route("/list")
def list():
	json_array_of_jsons = api.get_jsons()
	h = Headers()
	h.add('Content-Type', 'application/json')
	h.add('Access-Control-Allow-Origin', '*')
	resp = Response(response = json_array_of_jsons, headers = h, status = 200)
	return resp

@app2.route("/list/<string:provided_hash>")
def list_hash(provided_hash):
	detailed_json = api.get_detailed_json(provided_hash)
	h = Headers()
	h.add('Access-Control-Allow-Origin', '*')
	if detailed_json:
		h.add('Content-Type', 'application/json')
		resp = Response(response = detailed_json, headers = h, status = 200	)
	else:
		resp = Response(response = "Error with given hash not found", headers = h, status = 404)
	return resp
		
if __name__ == "__main__":
	app2.run(port=5001, debug=True)