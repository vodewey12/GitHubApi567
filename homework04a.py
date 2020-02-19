import requests
import json

count = 0
repoName = ''

#Gets the repos from the user ids
def getRepos(user):
    global repoName
    r = requests.get('https://api.github.com/users/' + user + '/repos')

    if(r.ok):
        repoItem = json.loads(r.text)
        for i in range (0, len(repoItem)):
            print (repoItem[i]['name'])
    
    repo = input("Please Select the repo you want to see the commits for: ")
    repoName = repo
    getCommits(user , repo)


#Get the total commits from the specific repo chosen by the user from the userID
def getCommits(user, repo):
    r = requests.get('https://api.github.com/repos/' + user + '/' + repo + '/commits')
    global count
    if(r.ok):
        "yaya"
        repoItem = json.loads(r.text)
        count = len(repoItem)
    return ("Repo: " + str(repo) + ' Number of commits: ' + str(count))


