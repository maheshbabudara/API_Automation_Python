import requests


class APIclient:
    base_url = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.header = {
            'Content-Type': 'application/json'
        }

    def get(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url=url, headers=self.header)
        return response

    def post(self,endpoint,data):
        url=f"{self.base_url}/{endpoint}"
        response=requests.post(url=url,headers=self.header,json=data)
        return response


    def put(self,endpoint,data):
        url=f"{self.base_url}/{endpoint}"
        response=requests.put(url=url,headers=self.header,json=data)
        return response

    def delete(self,endpoint):
        url=f"{self.base_url}/{endpoint}"
        response=requests.delete(url=url,headers=self.header)
        return response


