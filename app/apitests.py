import unittest
import redis

class TestEachError100(unittest.TestCase):
	def setUp(self):
		server = redis.StrictRedis("localhost")


	
	def tearDown(self):
		
if __name__ == '__main__':
	unittest.main()