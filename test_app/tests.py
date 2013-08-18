from django.test import TestCase
from django.contrib.auth.models import User
from .models import UnchangeableModel, UnchangeableModelDependency


class TestAppTests(TestCase):
    def setUp(self):
        User.objects.create_superuser("user", "user@example.com", "password")
        t = UnchangeableModelDependency.objects.create()
        UnchangeableModel.objects.create(dependency=t)
        self.dependency_id = t.id
        self.client.login(username="user", password="password")

    def tearDown(self):
        self.client.logout()

    def test_no_change_url_delete_selected(self):
        """
        delete_selected action should not result in error 500 if no change view is provided by the admin.

        regression test for #20640
        """
        r = self.client.post("/admin/test_app/unchangeablemodeldependency/", {
            "action": "delete_selected",
            "index": 0,
            "_selected_action": self.dependency_id,
        })
        self.assertEquals(r.status_code, 200)

    def test_no_change_url_changelist_page(self):
        """
        changelist view should not result in error 500 if no change view is provided by the admin.

        regression test for #20934
        """
        r = self.client.get("/admin/test_app/unchangeablemodel/")
        self.assertEquals(r.status_code, 200)
