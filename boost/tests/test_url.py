from django.test import SimpleTestCase
from django.urls import reverse, resolve
from boost.views import *


class TestUrls(SimpleTestCase):

    def test_index(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)


    def test_register(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signup_view)


    def test_login(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_view)


    def test_logout(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_view)



    def test_index(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search)

    def test_division_details(self):
        url = reverse('division_details', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, division_details)

    def test_services(self):
        url = reverse('services', args=['some-slug-service'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, services)

    def test_cart(self):
        url = reverse('cart')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cart)

    def test_checkout(self):
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)

    def test_updateItem(self):
        url = reverse('updateItem')
        print(resolve(url))
        self.assertEquals(resolve(url).func, updateItem)

    def test_process_order(self):
        url = reverse('process_order')
        print(resolve(url))
        self.assertEquals(resolve(url).func, process_order)

    def test_faqs(self):
        url = reverse('faqs')
        print(resolve(url))
        self.assertEquals(resolve(url).func, faqs)

    def test_terms(self):
        url = reverse('terms')
        print(resolve(url))
        self.assertEquals(resolve(url).func, terms)

    def test_privacy(self):
        url = reverse('privacy')
        print(resolve(url))
        self.assertEquals(resolve(url).func, privacy)

    def test_contact(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact)