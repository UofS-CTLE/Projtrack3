import datetime

import django.test
from django.contrib.auth.models import User as App_User
# noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,
# noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
from projtrack.models import Client, Project, Type, User, Department, Semester

from .report_generator import check_semester, check_client, check_department, check_type


class DepartmentTestCase(django.test.TestCase):
    def setUp(self):
        Department.objects.create(name="A")
        Department.objects.create(name="B")

    def test_departments(self):
        a = Department.objects.get(name="A")
        b = Department.objects.get(name="B")
        self.assertEqual(a.name, "A")
        self.assertEqual(b.name, "B")


class ClientTestCase(django.test.TestCase):
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


class ProjectTestCase(django.test.TestCase):
    def setUp(self):
        u = User()
        u.username = "techconbob"
        u.save()
        Type.objects.create(name="Test")
        Department.objects.create(name="Science")
        Client.objects.create(first_name="Ralph", last_name="Smith",
                              email="rsmith@email.com",
                              department=Department.objects.get(name="Science"))
        p = Project.objects.create(title="Test Project",
                               description="A project to test the application.",
                               type=Type.objects.get(name="Test"),
                               walk_in=False,
                               date=str(datetime.date.today()),
                               semester=Semester.objects.create(name="Spring 2913"),
                               client=Client.objects.get(first_name="Ralph"),
                               completed=False)
        p.save()
        p.users.add(u)

    def test_user(self):
        p = Project.objects.get(title="Test Project")
        self.assertTrue(User.objects.get(username="techconbob") in p.users.all())

    def test_department(self):
        p = Project.objects.get(title="Test Project")
        self.assertEqual(p.client.department.name, "Science")

    def test_description(self):
        p = Project.objects.get(title="Test Project")
        self.assertEqual(p.description, "A project to test the application.")

    def test_type(self):
        p = Project.objects.get(title="Test Project")
        self.assertEqual(p.type.name, "Test")

    def test_client(self):
        p = Project.objects.get(title="Test Project")
        self.assertEqual(p.client.email, "rsmith@email.com")


class TestNavigation(django.test.TestCase):
    def setUp(self):
        App_User.objects.create_user(username="test", email="test@email.com",
                                     password="password123")
        self.client = django.test.Client()
        self.client.login(username="test", password="password123")

    def test_logged_in(self):
        response = self.client.post("/home/", follow=True)
        self.assertContains(response, "Home", status_code=200)


class TestReportGenerator(django.test.TestCase):
    def setUp(self):
        p1 = Project.objects.create(title="Test",
                               description="Test",
                               date=datetime.date.today(),
                               type=Type.objects.create(name="Project"),
                               walk_in=False,
                               client=Client.objects.create(first_name="Bob",
                                                            last_name="Roberts",
                                                            department=Department.objects.create(name="Testing"),
                                                            email='roberts@email.com'),
                               semester=Semester.objects.create(name="Test"),
                               completed=False)
        p1.save()
        p1.users.add(User.objects.create(username="admin"))
        p2 = Project.objects.create(title="Stuff",
                               description="Why",
                               date=datetime.date.today(),
                               type=Type.objects.create(name="Test"),
                               walk_in=False,
                               client=Client.objects.create(first_name="Jerry",
                                                            last_name="Jerries",
                                                            department=Department.objects.create(name="Science"),
                                                            email='jerries@email.com'),
                               semester=Semester.objects.create(name="Test2"),
                               completed=False)
        p2.save()
        p2.users.add(User.objects.create(username="techconbob"))
        p3 = Project.objects.create(title="Help",
                               description="Testing",
                               date=datetime.date.today(),
                               type=Type.objects.create(name="Help"),
                               walk_in=False,
                               client=Client.objects.create(first_name="Larry",
                                                            last_name="Lawrence",
                                                            department=Department.objects.create(name="CTLE"),
                                                            email='jerries@email.com'),
                               semester=Semester.objects.create(name="Later"),
                               completed=False)
        p3.save()
        p3.users.add(User.objects.create(username="harry"))

    def test_check_semester(self):
        sem = Semester.objects.get(name="Test")
        self.assertEqual(check_semester(sem),
                         [Project.objects.get(semester=sem)])

    def test_check_semester_2(self):
        sem = Semester.objects.get(name="Test")
        pro = check_semester(sem)
        self.assertEqual(pro[0].title, "Test")

    def test_semester_get(self):
        sem = Semester.objects.get(name="Test")
        self.assertNotEqual('', str(sem))

    def test_get_user(self):
        use = User.objects.get(username="techconbob")
        self.assertNotEqual('', str(use))

    def test_check_user(self):
        use = User.objects.get(username="techconbob")
        sem = Semester.objects.get(name="Test2")
        self.assertEqual(check_semester(sem),
                         [Project.objects.get(users=use)])

    def test_get_client(self):
        cli = Client.objects.get(email="roberts@email.com")
        self.assertNotEqual('', str(cli))

    def test_check_client(self):
        sem = Client.objects.get(email="roberts@email.com")
        self.assertEqual(check_client(sem),
                         [Project.objects.get(client=sem)])

    def test_get_department(self):
        dept = Department.objects.get(name="Science")
        self.assertNotEqual('', str(dept))

    def test_check_department(self):
        sci = Department.objects.get(name="Science")
        cli = Client.objects.get(department=sci)
        self.assertEqual(check_department(sci),
                         [Project.objects.get(client=cli)])

    def test_get_type(self):
        typ = Type.objects.get(name="Project")
        self.assertNotEqual('', str(typ))

    def test_check_type(self):
        sem = Type.objects.get(name="Project")
        self.assertEqual(check_type(sem),
                         [Project.objects.get(type=sem)])
