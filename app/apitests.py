import unittest
import urllib, redis, jsonpickle

#TODO make config file with url/ports as variables

def open_n_times(url, n):
	for i in range(0, n):
		urllib.urlopen(url)

def get_list():
	response = urllib.urlopen("http://localhost:5001/list")
	content = response.read()
	return content

class TestErrors(unittest.TestCase):
	def setUp(self): # clears redis database before each test runs
		server = redis.StrictRedis("localhost")
		server.flushall()
	
	def test_setUp(self): # test that setUp cleared redis database
		list_page_content = get_list()
		array = jsonpickle.decode(list_page_content)
		self.assertEqual(len(array), 0)
	
	def test_5_Error1(self): # change to capital T to skip test
		open_n_times("http://localhost:5000/error1", 5)
		list_page_content = get_list()
		array = jsonpickle.decode(list_page_content)
		self.assertEqual(len(array), 1) # check there is only one element in array
		error1_obj_json = array[0]
		error1_obj = jsonpickle.decode(error1_obj_json)
		self.assertEqual(error1_obj.message_string, "integer division or modulo by zero") # check message string is correct
		self.assertEqual(error1_obj.count, 5) # check error count is correct
		self.assertEqual(error1_obj.context.url, "http://localhost:5000/error1") # check context.url is correct
		self.assertEqual(error1_obj.context.method, "GET") # check context.method is correct
		
	def test_5_Error2(self): # change to capital T to skip test
		open_n_times("http://localhost:5000/error2", 5)
		list_page_content = get_list()
		array = jsonpickle.decode(list_page_content)
		self.assertEqual(len(array), 1) # check there is only one element in array
		error1_obj_json = array[0]
		error1_obj = jsonpickle.decode(error1_obj_json)
		self.assertEqual(error1_obj.message_string, "global name 'spam' is not defined") # check message string is correct
		self.assertEqual(error1_obj.count, 5) # check error count is correct
		self.assertEqual(error1_obj.context.url, "http://localhost:5000/error2") # check context.url is correct
		self.assertEqual(error1_obj.context.method, "GET") # check context.method is correct

	def test_5_Error3(self): # change to capital T to skip test
		open_n_times("http://localhost:5000/error3", 5)
		list_page_content = get_list()
		array = jsonpickle.decode(list_page_content)
		self.assertEqual(len(array), 1) # check there is only one element in array
		error1_obj_json = array[0]
		error1_obj = jsonpickle.decode(error1_obj_json)
		self.assertEqual(error1_obj.message_string, "cannot concatenate 'str' and 'int' objects") # check message string is correct
		self.assertEqual(error1_obj.count, 5) # check error count is correct
		self.assertEqual(error1_obj.context.url, "http://localhost:5000/error3") # check context.url is correct
		self.assertEqual(error1_obj.context.method, "GET") # check context.method is correct

	def test_5_Error4(self): # change to capital T to skip test
		open_n_times("http://localhost:5000/error4", 5)
		list_page_content = get_list()
		array = jsonpickle.decode(list_page_content)
		self.assertEqual(len(array), 1) # check there is only one element in array
		error1_obj_json = array[0]
		error1_obj = jsonpickle.decode(error1_obj_json)
		self.assertEqual(error1_obj.message_string, "Test ValueError") # check message string is correct
		self.assertEqual(error1_obj.count, 5) # check error count is correct
		self.assertEqual(error1_obj.context.url, "http://localhost:5000/error4") # check context.url is correct
		self.assertEqual(error1_obj.context.method, "GET") # check context.method is correct				
	
	def test_2_AllErrors(self): 
		open_n_times("http://localhost:5000/error1", 2)
		open_n_times("http://localhost:5000/error2", 2)
		open_n_times("http://localhost:5000/error3", 2)
		open_n_times("http://localhost:5000/error4", 2)
		list_page_content = get_list()
		array = jsonpickle.decode(list_page_content)
		self.assertEqual(len(array), 4) # check there are four elements in array
		error_obj0 = jsonpickle.decode(array[0])
		error_obj1 = jsonpickle.decode(array[1])
		error_obj2 = jsonpickle.decode(array[2])
		error_obj3 = jsonpickle.decode(array[3])
		if error_obj0.count == error_obj1.count == error_obj2.count == error_obj3.count == 2: # check count for each error is correct
			correct_count = True
		self.assertEqual(correct_count, True)
		if error_obj0.context.method == error_obj1.context.method == error_obj2.context.method == error_obj3.context.method == "GET": # check context.method for each error is correct
			correct_method = True
		self.assertEqual(correct_method, True) 
		
	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity = 2)