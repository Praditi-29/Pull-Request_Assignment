import requests
base_url="https://api.github.com/"
access_tokken="Enter your github access tokken here"

# PULLS : API that allow to list,view,create,edit and merge Pull Requests.
# PULL REQUEST : Pull requests let you tell others about changes you've pushed to a branch in a repository on GitHub.

# 1) List Pull Requests : GET (base_url/repos/{owner}/{repo}/pulls)
# def List_Pull_Request(owner,repo):
#     url=base_url+"repos/" + owner +"/" +repo +"/pulls"
#     print(url)
#     response= requests.get(url,auth=(access_tokken,''))
#     print(response)
#     return response.json()
# print(List_Pull_Request("Praditi-29","PythonApiPractice"))
# RESPONSE : <Response [200]> ("id": 1,"created_at":"2022-11-29T14:14:53Z","updated_at":"2022-11-29T14:14:53Z")

# 2) Create Pull request : POST (base_url/repos/{owner}/{repo}/pulls)   
#  Note: We must have access to create, write and update to particular branch

# def Create_PullRequest(owner,repo):
#     url=base_url+"repos/" + owner +"/" +repo +"/pulls"
#     print(url)
#     todo={ "title": 'Creation',"body": 'Creation is in process'}
#     resp= requests.post(url,auth=(access_tokken,''),json=todo)
#     print(resp)
#     return resp.json()
# print( Create_PullRequest("Praditi-29","PythonApiPractice"))

#RESPONSE : <Response [422]>( 'message': 'Invalid request.\n\n"base",,)

# 3) Get A pull request : GET (base_url/repos/{owner}/{repo}/pulls/{pull_number})

# def Get_PullRequest(owner,repo,pull_number):
#     url=base_url+"repos/" + owner +"/" +repo +"/pulls/"+pull_number
#     print(url)
#     resp= requests.get(url,auth=(access_tokken,''))
#     print(resp)
#     return resp.text
# print(Get_PullRequest("Praditi-29","PythonApiPractice","2"))

#RESPONSE: <Response [200]>( "repo": {"name": "PythonApiPractice","full_name": "Praditi-29/PythonApiPractice",)

# 4) Update Pull Request : Patch (base_url/repos/{owner}/{repo}/pulls/{pull_number})

# def Update_PullRequest(owner,repo,pull_number):
#     url=base_url+"repos/" + owner +"/" +repo +"/pulls/"+pull_number
#     print(url)
#     # todo={"body":"It is my Second Commit","title":"GivenByPraditi","state":'open}
#     todo={"created_at":"2022-10-29T14:14:53Z"}
#     resp= requests.patch(url,auth=(access_tokken,''),json=todo)
#     print(resp)
#     return resp.text
# print(Update_PullRequest("Praditi-29","PythonApiPractice","1"))

# RESPONSE:  <Response [200]>

# 5) List Commits on pull request : Get (base_url/repos/{owner}/{repo}/pulls/{pull_number}/commits)

# def listCommits_PullsRequest(owner,repo,pull_number):  
#     url=base_url+"repos/" + owner +"/" +repo +"/pulls/"+pull_number+"/commits"
#     print(url)
#     resp= requests.get(url,auth=(access_tokken,''))
#     print(resp)
#     return resp.text
# print(listCommits_PullsRequest("Praditi-29","PythonApiPractice","1"))

# Response : <Response [200]>  ("commits":3,"additions":20,"deletions":2,"changed_files":3)

# 6) List Pull Request Files : Get (base_url/repos/{owner}/{repo}/pulls/{pull_number}/files)

# def ListFiles_PullRequest(owner,repo,pull_number):
#     url=base_url+"repos/" + owner +"/" +repo +"/pulls/"+pull_number+"/files"
#     print(url)
#     resp= requests.get(url,auth=(access_tokken,''))
#     print(resp)
#     return resp.json()
# print(ListFiles_PullRequest("Praditi-29","PythonApiPractice","1"))

# RESPONSE :<Response [200]> ("filename": "Praditi.txt","status": "added","additions": 25,"deletions": 5,)

# 7) To check if pull request Has been Merged : GET (base_url/repos/{owner}/{repo}/pulls/{pull_number}/merge )

# def is_merged(owner,repo,pull_number):
#     url=base_url+"repos/" + owner +"/" +repo +"/pulls/"+pull_number+"/merge"
#     print(url)
#     resp= requests.get(url,auth=(access_tokken,''))
#     print(resp)
#     return resp.text
# print(is_merged("Praditi-29","PythonApiPractice","1"))

# RESPONSE :<Response [404]>(if pull request has not been merged)

# 8) Merge Pull request : PUT (/repos/{owner}/{repo}/pulls/{pull_number}/merge)

# def do_merge(owner,repo,pull_number):
#     url=base_url+"repos/" + owner +"/" +repo +"/pulls/"+pull_number+"/merge"
#     print(url)
#     resp= requests.put(url,auth=(access_tokken,''))
#     print(resp)
#     return resp.text
# print(do_merge("Praditi-29","PythonApiPractice","2"))

# RESPONSE:<Response [200]>("merged":true,"message":"Pull Request successfully merged")

# 9)Update Pull Request Branch : PUT(/repos/{owner}/{repo}/pulls/{pull_number}/update-branch)

# def update_PullRequest_branch(owner,repo,pull_number):
#     url=base_url+"repos/" + owner +"/" +repo +"/pulls/"+pull_number+"/update-branch"
#     print(url)
#     todo={"commits":5,"changed_files":100}
#     resp= requests.put(url,auth=(access_tokken,''),json=todo)
#     print(resp)
#     return resp.text
# print(update_PullRequest_branch("Praditi-29","PythonApiPractice","master"))

# RESPONSE:<Response [404]> "message":"Not Found"