import unittest
import smartystreets_python_sdk as smarty
from test.mocks import *


class XForwardedForTest (unittest.TestCase):
    def testNativeSetOnQuery(self):
        smartyrequest = smarty.Request()
        smartyrequest.url_prefix = "http://192.168.1.243:3128"
        smartyrequest.payload = "Test Payload"
        sender = smarty.RequestsSender(10000,None,"0.0.0.0")
        request = smarty.RequestsSender.build_request(sender,smartyrequest)
        response = sender.send(request)
        
        self.assertEqual("0.0.0.0",request.headers['X-Forwarded-For'])
        


    def testNativeNotSet(self):
        smartyrequest = smarty.Request()
        smartyrequest.url_prefix = "http://192.168.1.243:3128"
        smartyrequest.payload = "Test Payload"
        sender = smarty.RequestsSender()
        request = smarty.RequestsSender.build_request(sender,smartyrequest)
        sender.send(request)
        self.assertFalse('X-Forwarded-For' in request.headers)
        