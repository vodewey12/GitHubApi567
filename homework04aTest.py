import unittest
from homework04a import getCommits
import math
from unittest.mock import Mock

class TestHomework(unittest.TestCase):
    @mock.patch('homework04a.getCommits')
    def test_get_repos_commit(self):
        gitHub = [{
            'user'
        }]
        

        self.assertEqual(getCommits('vodewey12','Classify-Triangle'), 'Repo: Classify-Triangle Number of commits: 6')
        self.assertEqual(getCommits('vodewey12','Leet-Code-Practice'), 'Repo: Leet-Code-Practice Number of commits: 6')
if __name__ == '__main__':
    unittest.main()