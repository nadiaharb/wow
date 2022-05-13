from django.test import TestCase, Client
from django.urls import reverse
from boost.models import *
import json


class TestViews(TestCase):

    def setUp(self):
        self.client=Client()
        self.search_url=reverse('search')
        self.index_url = reverse('index')
        self.register_url=reverse('register')
        self.login_url=reverse('login')
        self.logout_url = reverse('logout')
        self.division_details_url=reverse('division_details', args=['divtest'])
        self.div=Division.objects.create(
            division='divtest',
            description='some text'
        )
        self.services_url=reverse('services', args=['testservice'])
        self.service=Services.objects.create(
            division=self.div,
            service_name='testservice',
            description='some text',
            price=32
        )
        self.cart_url=reverse('cart')
        self.checkout_url = reverse('checkout')
        self.faqs_url = reverse('faqs')
        self.terms_url = reverse('terms')
        self.privacy_url = reverse('privacy')
        self.contact_url = reverse('contact')


    def test_search_view(self):

        response=self.client.get(self.search_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boost/search.html')

    #def test_index_view(self):

#        response=self.client.get(self.index_url)
 #       self.assertEquals(response.status_code, 200)
  #      self.assertTemplateUsed(response, 'boost/home.html')


    def test_div_det(self):

        response=self.client.get(self.division_details_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boost/div_details.html')

    def test_register_view(self):

        response=self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boost/signup.html')

    def test_login_view(self):

        response=self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boost/login.html')


    def test_services_views(self):

        response=self.client.get(self.services_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boost/service_details.html')


    def test_cart_view(self):

        response=self.client.get(self.cart_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boost/cart.html')

    def test_privacy_view(self):

        response=self.client.get(self.privacy_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boost/privacy.html')

    def test_checkout_view(self):

        response=self.client.get(self.checkout_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boost/checkout.html')

    def test_faqs_view(self):

        response=self.client.get(self.faqs_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boost/faq.html')


    def test_terms_view(self):

        response=self.client.get(self.terms_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boost/terms.html')


    def test_contact_view(self):

        response=self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boost/contact.html')