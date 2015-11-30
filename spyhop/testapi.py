#!/usr/bin/python

from mock import MagicMock
import mock
import unittest
from api import Api


docker_api = Api()

docker_api_mock =  Api()

def ps():
    all_containers = docker_api.get_all_containers()
    return all_containers


class MyClient:
    def __init__(self):
        self.data =  {"a":1, "b":2} 
    def containers(self):
        print "enter mock client"
        return self.data
    def start(self):
        self.data["b"] = 2
    def stop(self):
        #self.data.remove("b")
        pass

data = {"a":1, "b":2}
def my_containers(a):
    print "enter my containers"
    return data

def my_start(o, id):
    data["b"] = 2

def my_stop(o, id):
    del data["b"]



class MyTest(unittest.TestCase):

    @mock.patch('docker.Client.containers', my_containers)
    @mock.patch('docker.Client.start', my_start)
    @mock.patch('docker.Client.stop', my_stop)
    def test_api(self):
	self.assertEqual(len(docker_api.get_all_containers()),2)
	docker_api.get_container_stop("8264ee6c8424")	
	self.assertEqual(len(docker_api.get_all_containers()),1)
	docker_api.get_container_start("8264ee6c8424")
	self.assertEqual(len(docker_api.get_all_containers()),2)

    def atest_instance(self):
        self.assertIsInstance(docker_api, Api)

    def atest_raise(self):
    	with self.assertRaises(BufferError):
            docker_api.get_container_stop("8264ee6c8425")

if __name__ == '__main__':
    unittest.main()
