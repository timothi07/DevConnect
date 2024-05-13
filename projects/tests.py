from django.test import TestCase, Client
from django.urls import reverse
from .models import Project

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.projects_url = reverse('projects')
        self.project1 = Project.objects.create(title='Project 1', description='Description 1')
        self.project2 = Project.objects.create(title='Project 2', description='Description 2')

    def test_projects_GET(self):
        response = self.client.get(self.projects_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/projects.html')

    def test_project_GET(self):
        response = self.client.get(reverse('project', args=[self.project1.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/single-project.html')

    def test_createProject_POST(self):
        response = self.client.post(reverse('create_project'), {
            'title': 'New Project',
            'description': 'New Description'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Project.objects.last().title, 'New Project')

    def test_updateProject_POST(self):
        response = self.client.post(reverse('update_project', args=[self.project1.id]), {
            'title': 'Updated Project',
            'description': 'Updated Description'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Project.objects.get(id=self.project1.id).title, 'Updated Project')

    def test_deleteProject_POST(self):
        response = self.client.post(reverse('delete_project', args=[self.project2.id]))

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Project.objects.filter(id=self.project2.id).exists(), False)
