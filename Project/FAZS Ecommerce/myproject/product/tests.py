from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from product.models import Category, Product


class PageSmokeTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user("tester", password="pass12345")
        self.category = Category.objects.create(name="Drinks")
        self.product = Product.objects.create(
            name="Test Cola", price=100, stock=5, category=self.category
        )

    def test_public_pages(self):
        urls = [
            reverse("home"),
            reverse("search") + "?q=cola",
            reverse("category-products", args=[self.category.slug]),
            reverse("product-detail", args=[self.product.slug]),
            reverse("login"),
            reverse("register"),
        ]
        for url in urls:
            self.assertEqual(self.client.get(url).status_code, 200, url)

    def test_logged_in_pages(self):
        self.client.login(username="tester", password="pass12345")
        for name in ["cart", "my-orders"]:
            self.assertEqual(self.client.get(reverse(name)).status_code, 200, name)

    def test_missing_page_gives_404(self):
        self.assertEqual(self.client.get("/does-not-exist/").status_code, 404)