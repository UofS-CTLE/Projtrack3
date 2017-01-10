from django.test import TestCase
from projtrack.models import Client, Project, Type, User, Department

class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(first_name="Ralph",
                last_name="Smith", 
                email="rsmith@email.com", 
                department=Department.objects.create(name="Literature"))
        Client.objects.create(first_name="Jill",
                last_name="Jackson",
                email="jjackson@email.com",
                department=Department.objects.create(name="Science"))
        c = Client()
        c.first_name = "Jeff"
        c.last_name = "Guy"
        c.email = "jguy@email.com"
        c.department = Department.objects.create(name="Math")
        c.save()

    def test_check_objects_email(self):
        ralph = Client.objects.get(first_name="Ralph")
        jill = Client.objects.get(first_name="Jill")
        jeff = Client.objects.get(first_name="Jeff")
        self.assertEqual(ralph.email, "rsmith@email.com")
        self.assertEqual(jill.email, "jjackson@email.com")
        self.assertEqual(jeff.email, "jguy@email.com")

    def test_check_objects_last_name(self):
        ralph = Client.objects.get(first_name="Ralph")
        jill = Client.objects.get(first_name="Jill")
        jeff = Client.objects.get(first_name="Jeff")
        self.assertEqual(ralph.last_name, "Smith")
        self.assertEqual(jill.last_name, "Jackson")
        self.assertEqual(jeff.last_name, "Guy")

class ProjectTestCase(TestCase):
    def setUp(self):
        u = User()
        u.username = "techconbob"
        u.save()
        Type.objects.create(name="Test")
        Department.objects.create(name="Science")
        Client.objects.create(first_name="Ralph", last_name="Smith",
                              email="rsmith@email.com", 
                              department=Department.objects.get(name="Science"))
        Project.objects.create(title="Test Project",
                               description="A project to test the application.",
                               type=Type.objects.get(name="Test"),
                               walk_in=False,
                               client=Client.objects.get(first_name="Ralph"),
                               users=User.objects.get(username="techconbob"))

    def test_user(self):
        p = Project.objects.get(title="Test Project")
        self.assertEqual(p.users.username, "techconbob")

    def test_department(self):
        pass

    def test_description(self):
        pass

    def test_type(self):
        pass

    def test_client(self):
        pass
