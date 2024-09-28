import requests

url ="https://api.github.com/repos/kubernetes/kubernetes/pulls"

response=requests.get(url)
if response.status_code == 200:
    details=response.json() ##list of dictionaries
    pr_creators = {}
    for record in range(len(details)):
        current_user=details[record]["user"]["login"]
        if current_user in pr_creators:
            pr_creators[current_user] += 1
        else:
            pr_creators[current_user] = 1
    for i,n in pr_creators.items():
        print(f"{i}:{n}")
else:
    print(f"Error fetching data:{response.status_code}")