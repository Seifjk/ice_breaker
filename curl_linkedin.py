import requests

api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
api_key = "4Sa7ws9huIgKyv_ciQ4WSQ"
header_dic = {"Authorization": "Bearer " + api_key}
params = {
    "url": "https://www.linkedin.com/in/seifeddineshili/",
}
response = requests.get(api_endpoint, params=params, headers=header_dic)
response.json()
