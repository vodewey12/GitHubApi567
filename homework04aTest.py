import unittest
from homework04a import getCommits
import math

class TestHomework(unittest.TestCase):
    def test_get_repos_commit(self):
        self.assertEqual(getCommits('vodewey12','Classify-Triangle'), 'Repo: Classify-Triangle Number of commits: 4')
        self.assertEqual(getCommits('vodewey12','Leet-Code-Practice'), 'Repo: Leet-Code-Practice Number of commits: 6')
        self.assertEqual(getCommits('vodewey12','Meal-Exchange'), 'Repo: Meal-Exchange Number of commits: 17')
if __name__ == '__main__':
    unittest.main()