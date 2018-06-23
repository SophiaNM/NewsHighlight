import unittest
from app.models import Article
# from models import article
# Article = article.Article

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News Source Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("BBC News","Theranos founder hit with criminal charges","Elizabeth Holmes is charged with fraud over claims made for blood tests her company developed.", "http://www.bbc.co.uk/news/business-44501631","https://ichef.bbci.co.uk/news/1024/branded_news/8AC7/production/_102072553_holmes.jpg","2018-06-15T22:25:40Z")

    def test_instance(self):
        '''
        test case to test if object instance is created
        '''
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        '''
        Test case to test if object is initialized properly
        '''
        self.assertEqual(self.new_article.author,"BBC News")
        self.assertEqual(self.new_article.title,"Theranos founder hit with criminal charges")
        self.assertEqual(self.new_article.description,"Elizabeth Holmes is charged with fraud over claims made for blood tests her company developed.")
        self.assertEqual(self.new_article.url,"http://www.bbc.co.uk/news/business-44501631")
        self.assertEqual(self.new_article.urlToImage,"https://ichef.bbci.co.uk/news/1024/branded_news/8AC7/production/_102072553_holmes.jpg")
        self.assertEqual(self.new_article.publishedAt,"2018-06-15T22:25:40Z")
