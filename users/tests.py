from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile

class UserRegistrationLoginTests(TestCase):
    def setUp(self):
        # Use a test client for all requests
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.home_url = reverse('home')

    # --- Registration GET/POST ------------------------------------------------

    def test_register_get_renders_form(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertIn('form', response.context)

    def test_register_post_valid_creates_user_and_profile_and_logs_in(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'ComplexPass#123',
            'password2': 'ComplexPass#123',
        }
        response = self.client.post(self.register_url, data)
        # Should redirect to home
        self.assertRedirects(response, self.home_url)

        # User & Profile exist
        user = User.objects.filter(username='newuser').first()
        self.assertIsNotNone(user, "User was not created")
        profile = Profile.objects.filter(user=user).first()
        self.assertIsNotNone(profile, "Profile was not created")
        self.assertEqual(profile.email, 'newuser@example.com')

        # Client should now be authenticated
        response = self.client.get(self.home_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_register_post_username_already_exists_shows_error(self):
        # Pre-create a user
        User.objects.create_user(username='dup', password='DummyPass#1')
        data = {
            'username': 'dup',
            'email': 'dup@example.com',
            'password1': 'Another#Pass1',
            'password2': 'Another#Pass1',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)
        # Only check for username error, not password2
        self.assertIn('A user with that username already exists.', form.errors['username'])

    def test_register_post_passwords_do_not_match(self):
        data = {
            'username': 'user2',
            'email': 'u2@example.com',
            'password1': 'ComplexPass#123',
            'password2': 'DifferentPass#456',
        }
        response = self.client.post(self.register_url, data)
        form = response.context['form']
        self.assertTrue(form.errors)
        # Normalize apostrophes for robust comparison
        error_msgs = [msg.replace("’", "'") for msg in form.errors['password2']]
        self.assertIn("The two password fields didn't match.", error_msgs)

    def test_register_post_invalid_email(self):
        data = {
            'username': 'user3',
            'email': 'not-an-email',
            'password1': 'ComplexPass#123',
            'password2': 'ComplexPass#123',
        }
        response = self.client.post(self.register_url, data)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn("Enter a valid email address.", form.errors['email'])

    # --- Login GET/POST -------------------------------------------------------

    def test_login_get_renders_form(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIn('form', response.context)

    def test_login_post_valid_credentials(self):
        User.objects.create_user(username='loginuser', password='LoginPass#1')
        data = {'username': 'loginuser', 'password': 'LoginPass#1'}
        response = self.client.post(self.login_url, data)
        self.assertRedirects(response, self.home_url)

        # After redirect, user should be authenticated
        response = self.client.get(self.home_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_post_invalid_password_shows_error(self):
        User.objects.create_user(username='baduser', password='RightPass#1')
        data = {'username': 'baduser', 'password': 'WrongPass#1'}
        response = self.client.post(self.login_url, data)
        # Stays on login page
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)
        # Non‑field error about invalid credentials
        self.assertIn('Please enter a correct username and password', form.non_field_errors()[0])

    def test_login_post_nonexistent_user_shows_error(self):
        data = {'username': 'noexist', 'password': 'Whatever#1'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('Please enter a correct username and password', form.non_field_errors()[0])

    def test_login_post_blank_fields_shows_required_errors(self):
        data = {'username': '', 'password': ''}
        response = self.client.post(self.login_url, data)
        form = response.context['form']
        # Both fields required
        self.assertIn('This field is required.', form.errors['username'])
        self.assertIn('This field is required.', form.errors['password'])
