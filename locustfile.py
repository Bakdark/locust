import random
from locust import HttpUser, task, between, TaskSet

class SimpleAuthWebUser(HttpUser):
    wait_time = between(5, 9)
    
    def on_start(self):
       response = self.client.request(method="GET", url = "/", auth=("cloud", "cloud"))
       self.token = response.request.headers['Authorization']
       print(self.token)

    @task
    def index_page(self):
        self.client.get("/", headers={"Authorization": self.token })

    @task
    def cms_page(self):
        self.client.get("", headers={"Authorization": self.token })
