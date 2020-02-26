import unittest
from homework04a import getCommits
import math
from unittest.mock import Mock, patch

class TestHomework(unittest.TestCase):


    def simple_getCommits(user_Name, repo_Name):
        if user_Name == 'vodewey12' and repo_Name == 'Classify-Triangle':
            return "Repo: Classify-Triangle Number of commits: 6"
        if user_Name == 'vodewey12' and repo_Name == 'Leet-Code-Practice':
            return "Repo: Leet-Code-Practice Number of commits: 6"

    @patch("homework04a.getCommits", side_effect=simple_getCommits)
    def test_get_repos_commit(self, getCommits_function):
        commits = ['Repo: Classify-Triangle Number of commits: 6', 'Repo: Leet-Code-Practice Number of commits: 6']
        self.assertEqual(getCommits('vodewey12', 'Classify-Triangle'), commits[0])


        self.assertEqual(getCommits('vodewey12', 'Leet-Code-Practice'), commits[1])
if __name__ == '__main__':
    unittest.main()