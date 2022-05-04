import unittest
from articles import Articles
# Articles = articles.Articles

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles('news_all','desc_all','image_url_all','p_date_all','url_all')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))


if __name__ == '__main__':
    unittest.main()