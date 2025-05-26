import pytest
from django.contrib.auth.models import User


def test_home_endpoint_returns_welcome_lage(client):
    response = client.get(path="/")
    assert response.status_code == 200
    assert 'Welcome to SmartNotes!' in str(response.content)

def test_signup_endpoint_returns_form_for_unauthenticated_user(client):
    response = client.get(path="/signup")
    assert response.status_code == 200
    assert 'home/register.html' in str(response.template_name)

@pytest.mark.django_db  # Allowing database access
def test_signup_endpoint_redirects_authenticated_user(client):
    '''
        When a user is authenticated and tries to access the signup page they are
        redirected to the list of their notes.
    '''
    user = User.objects.create_user('Clara', 'clara@example.com', 'password')
    client.login(username = user.username, password='password')
    response = client.get(path="/signup", follow=True)

    assert 200 == response.status_code
    assert 'notes/notes_list.html' in str(response.template_name)








    