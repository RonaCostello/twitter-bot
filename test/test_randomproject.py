import unittest
import tweetbot
from tweetbot import randomproject
from panoptes_client import Project

class TestRandomProjectFunction(unittest.TestCase):

    def setUp(self):
        self.project = randomproject.random_project()

    def test_is_project(self, msg = 'randomproject should return a zooniverse project'):
        self.assertIsInstance( self.project, Project )

    def test_has_title(self, msg ='chosen project must have a title'):
        self.assertTrue( self.project.title )

    def test_has_short_description(self, msg = 'the combined length of the project title and description should be less than 200 characters'):
        self.assertLess( len(self.project.description), 200)

    def test_is_not_redirect(self, msg = 'Project should not be a redirect project'):
        self.assertFalse( self.project.redirect )

    def test_is_not_complete(self, msg = 'Project should have at least 500 unretired subjects'):
        self.assertGreater( self.project.subjects_count - self.project.retired_subjects_count, 500 )

    def test_project_completedness(self, msg = 'Project should have a completeness score of less than 1'):
        self.assertLess( self.project.completeness, 1.0)






if __name__ == '__main__':
    unittest.main()
