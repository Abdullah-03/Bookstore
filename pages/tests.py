from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import AboutPageView


class HomePageTests(SimpleTestCase):
    def setUp(self) -> None:
        self.response = self.client.get(reverse('home'))

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "ligma balls")


class AboutPageTests(SimpleTestCase):
    def setUp(self) -> None:
        self.response = self.client.get(reverse('about'))

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'I should not be here!')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
