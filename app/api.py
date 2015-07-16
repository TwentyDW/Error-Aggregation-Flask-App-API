import redis, jsonpickle
		
server = redis.StrictRedis("localhost")

def get_jsons():
	array_of_jsons = server.hvals("errors")
	json_array_of_jsons = jsonpickle.encode(array_of_jsons)
	return json_array_of_jsons

def get_detailed_json(hash):
	error_instance_json = server.hget("errors", hash)	
	return error_instance_json
		