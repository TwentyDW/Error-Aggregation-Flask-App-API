import unittest
import urllib, redis, jsonpickle

#TODO make config file with url/ports as variables

def open_5_times(url):
	for i in range(0, 5):
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
		open_5_times("http://localhost:5000/error1")
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
		open_5_times("http://localhost:5000/error2")
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
		open_5_times("http://localhost:5000/error3")
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
		open_5_times("http://localhost:5000/error4")
		list_page_content = get_list()
		array = jsonpickle.decode(list_page_content)
		self.assertEqual(len(array), 1) # check there is only one element in array
		error1_obj_json = array[0]
		error1_obj = jsonpickle.decode(error1_obj_json)
		self.assertEqual(error1_obj.message_string, "Test ValueError") # check message string is correct
		self.assertEqual(error1_obj.count, 5) # check error count is correct
		self.assertEqual(error1_obj.context.url, "http://localhost:5000/error4") # check context.url is correct
		self.assertEqual(error1_obj.context.method, "GET") # check context.method is correct				
	
	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity = 2)