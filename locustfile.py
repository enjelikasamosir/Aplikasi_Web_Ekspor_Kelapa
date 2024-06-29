from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    @task(1)
    def load_home_page(self):
        self.client.get("/home.php")

    @task(2)
    def load_products_section(self):
        self.client.get("/home.php#products")

    @task(1)
    def load_deal_of_the_day(self):
        self.client.get("/home.php#deal-of-the-day")

    @task(1)
    def load_testimony_section(self):
        self.client.get("/home.php#testimony")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://localhost/Ekspor_Kelapa"  # Sesuaikan dengan host aplikasi Anda
