import requests
from datetime import datetime
from pixela import pixela_token, user_name

headers = {
    "X-USER-TOKEN": pixela_token
}

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"

def create_user():
    user_params = {
        "token": pixela_token,
        "username": user_name,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)

def create_new_graph(graph_id, graph_name, unit, primitive_type, color):

    graph_config = {
        "id": graph_id,
        "name": graph_name,
        "unit": unit,
        "type": primitive_type,
        "color": color
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

def log_work(hours_worked, graph_id, date):
    pixel_endpoint = f"{graph_endpoint}/{graph_id}"

    pixel_config = {
        "date": date,
        "quantity": hours_worked
    }

    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
    print(response.text)

def update_work_log(hours_worked, graph_id, date):
    new_data = {
        "quantity": hours_worked
    }
    update_endpoint = f"{graph_endpoint}/{graph_id}/{date}"
    response = requests.put(url=update_endpoint, json=new_data, headers=headers)
    print(response.text)

def delete_work_log(graph_id, date):
    delete_endpoint = f"{graph_endpoint}/{graph_id}/{date}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)

timestamp = datetime.now()
log_work("10", "coding", timestamp.strftime("%Y%m%d"))
#update_work_log("2", "coding", timestamp.strftime("%Y%m%d"))
#delete_work_log("coding", timestamp.strftime("%Y%m%d"))



