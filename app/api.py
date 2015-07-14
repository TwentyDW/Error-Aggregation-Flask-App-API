import redis, jsonpickle

"""class Error_Without_Details:
	def __init__(self, error_obj_instance):
		self.hash = error_obj_instance.hash
		self.message_string = error_obj_instance.message_string
		self.first_occurrence = error_obj_instance.first_occurrence
		self.last_occurrence = error_obj_instance.last_occurrence
		self.count = error_obj_instance.count"""
		
server = redis.StrictRedis("localhost")

def get_jsons():
	array_of_jsons = server.hvals("errors")
	# commented-out code is for removing details from error_json, but is inefficient
	"""for i in range(0, len(array_of_jsons)): # go through each array element and strip away details 
	error_obj_instance = jsonpickle.decode(array_of_jsons[i])
	without_details_instance = Error_Without_Details(error_obj_instance)
	array_of_jsons[i] = jsonpickle.encode(without_details_instance)"""
	json_array_of_jsons = jsonpickle.encode(array_of_jsons)
	return json_array_of_jsons

def get_detailed_json(hash):
	error_instance_json = server.hget("errors", hash)	
	return error_instance_json
		