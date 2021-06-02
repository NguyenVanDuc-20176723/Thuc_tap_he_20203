import requests


def find_dict(title="", completed=False):
    re_list = []
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    data = response.json()
    for item in data:
        if title in item["title"] and item["completed"] == completed:
            re_list.append(item)
    return re_list


ttl = "autem"
complete = False
result = find_dict(ttl, complete)
print(result)
