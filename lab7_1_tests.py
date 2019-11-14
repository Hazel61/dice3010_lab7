import unittest
import lab7_1 as target 

class TestLab7(unittest.TestCase):
   
   def setUp(self):
      self.good_url ='https://computingconcepts.herokuapp.com'
      self.bad_url = 'https://www.dylanmedina.com'
      self.unfixible_url = 'www.dylanmedina.horse'
      self.good_data = {'username': 'bobby', 'email': 'bobby@bobby.com'}

   def test_basic_request_bad_url_can_not_be_fixed(self):
      self.assertIsNone(target.basic_request(self.unfixible_url))

   def test_basic_request_bad_url_can_be_fixed(self):
      self.assertEqual(200, target.basic_request(self.bad_url))

   def test_basic_request_good_url(self):
      self.assertEqual(200, target.basic_request(self.good_url))
   
   def test_requests_user_agent_bad_url(self):
      self.assertIsNone(target.request_user_agent(self.unfixible_url, 'DICE'))
   
   def test_requests_user_agent_bad_user_agent(self):
      self.assertIsNone(target.request_user_agent(self.good_url, False))
   
   def test_requests_user_agent(self):
      self.assertEqual("44260953", target.request_user_agent(self.good_url, 'DICE'))
   
   def test_requests_post_bad_url(self):
      self.assertIsNone(target.request_post(self.unfixible_url, self.good_data))
   
   def test_requests_post_bad_data(self):
      self.assertIsNone(target.request_post(self.good_url, None))
   
   def test_requests_post_works(self):
      self.assertEqual("44261853", target.request_post(self.good_url, self.good_data))
   