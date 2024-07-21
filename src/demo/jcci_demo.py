import json


def load_and_parse_json(file_path):
    # Load JSON data from a file
    with open(file_path, 'r') as file:
        input_json = json.load(file)

    # Extract node names
    nodes = input_json['nodes']
    links = [_ for _ in input_json['links']]
    categories = [_ for _ in input_json['categories']]
    impacted_api_list = input_json['impacted_api_list']

    return nodes, links, categories, impacted_api_list


# File path
file_path = 'D:\PycharmProjects\jcci\src\demo\master..feature#order202407.cci'

# Call the function and retrieve data
nodes, links, categories, impacted_api_list = load_and_parse_json(file_path)

# print("Nodes:", type(nodes), nodes)
# print("File Paths:", links)
# print("Node Types:", categories)
# print("Impacted APIs:", type(impacted_api_list), impacted_api_list)

targets = set([link["target"] for link in links])
print(targets)

api_paths = [node.get("api_path").split("]")[1] for node in nodes if
             node.get("api_path") and node["id"] in targets and "Controller" in node["name"]]
print(api_paths)

import requests


# 基础 URL
base_url = "http://test.com/search"

# 定义要发送的 cookies
cookies = {
    'name1': 'value1',
    'name2': 'value2'
}

# 遍历 api_paths 并发送 GET 请求
for api_path in api_paths:
    # 构造完整的 URL
    # 注意：这里假设 api_path 是一个简单的字符串，可能需要根据实际情况进行解析和编码
    full_url = f"{base_url}?api_path={api_path}"

    # 发送 GET 请求
    response = requests.get(full_url, cookies=cookies)

    # 打印响应内容
    print(f"Response for {api_path}: {response.text}")

# 如果需要处理响应数据或其他逻辑，可以在这里添加相应的代码

