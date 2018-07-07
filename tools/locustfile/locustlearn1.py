from locust import Locust, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def job(self):
        pass

class User(Locust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
