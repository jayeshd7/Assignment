from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_users(self):
        self.client.get("/users/2")

    @task(1)
    def post_users(self):
        self.client.post(
            "/user",
            data={
                "user_id": 1,
                "user_name": "jayesh",
                "address": "pune",
                "email": "j.@gmai.com",
            },
        )
