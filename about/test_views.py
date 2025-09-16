from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()

    # GET
    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['collab_form'], CollaborateForm)
        
    # POST
    def test_successful_collab_submission(self):
        """Test for submitting a collaboration request"""
        collab_data = {
            'name': 'Testuser',
            'email': 'test@test.de',
            'message': 'This is a test message.'
        }
        response = self.client.post(reverse(
            'about'), collab_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.', # message
            response.content
        )