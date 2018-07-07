from locust import HttpLocust, TaskSet

def job1(l):
    l.client.get('/')

def job2(l):
    l.client.get('/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=a&rsv_pq=d3e6a1bc0000db99&rsv_t=b2a65Q2Jsj%2FAFujUB%2F6qDEOhO1ylxo5ORDWYiZj%2FHU%2B5AhmDDqDWQQKTlzE&rsv_enter=1&rsv_sug3=1&rsv_sug1=2&rsv_sug2=0&inputT=206&rsv_sug4=207')

class UserBehavior(TaskSet):
    tasks = {job1:1, job2:2}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
