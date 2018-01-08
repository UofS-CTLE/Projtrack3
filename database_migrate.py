#! /usr/bin/env python

import sqlite3

conn = sqlite3.connect("db.sqlite3")

projects = list()

for row in conn.execute("SELECT id, users_id FROM Project"):
    print(row)
    projects.append(row)

conn.commit()
conn.close()

conn = sqlite3.connect("./ctleweb/db.sqlite3")
for x in projects:
    conn.execute("INSERT INTO Project_users (project_id, user_id) VALUES (?, ?)", (x[0], x[1]))

conn.commit()
conn.close()

conn1 = sqlite3.connect("db.sqlite3")
conn2 = sqlite3.connect("./ctleweb/db.sqlite3")
for row in conn1.execute("SELECT * FROM Client"):
    conn2.execute("INSERT INTO Client VALUES (?,?,?,?,?)", row)

for row in conn1.execute("SELECT * FROM CurrentSemester"):
    conn2.execute("INSERT INTO CurrentSemester VALUES (?,?)", row)

for row in conn1.execute("SELECT * FROM Department"):
    conn2.execute("INSERT INTO Department VALUES (?,?)", row)

for row in conn1.execute("SELECT id, title, description, walk_in, hours, completed, client_id, semester_id, type_id, \
                          date FROM Project"):
    conn2.execute("INSERT INTO Project VALUES (?,?,?,?,?,?,?,?,?,?)", row)

for row in conn1.execute("SELECT * FROM Semester"):
    conn2.execute("INSERT INTO Semester VALUES (?,?)", row)

for row in conn1.execute("SELECT * FROM Type"):
    conn2.execute("INSERT INTO Type VALUES (?,?)", row)

for row in conn1.execute("SELECT * FROM auth_group"):
    conn2.execute("INSERT INTO auth_group VALUES (?,?)", row)

for row in conn1.execute("SELECT * FROM auth_group_permissions"):
    conn2.execute("INSERT INTO auth_group_permissions VALUES (?,?,?)", row)

for row in conn1.execute("SELECT * FROM auth_user"):
    conn2.execute("INSERT INTO auth_user VALUES (?,?,?,?,?,?,?,?,?,?,?)", row)

for row in conn1.execute("SELECT * FROM auth_user_groups"):
    conn2.execute("INSERT INTO auth_user_groups VALUES (?,?,?)", row)

for row in conn1.execute("SELECT * FROM auth_user_user_permissions"):
    conn2.execute("INSERT INTO auth_user_user_permissions VALUES (?,?,?)", row)

for row in conn1.execute("SELECT * FROM django_admin_log"):
    conn2.execute("INSERT INTO django_admin_log VALUES (?,?,?,?,?,?,?,?)", row)

for row in conn1.execute("SELECT * FROM django_session"):
    conn2.execute("INSERT INTO django_session VALUES (?,?,?)", row)

for row in conn1.execute("SELECT * FROM sqlite_sequence"):
    conn2.execute("INSERT INTO sqlite_sequence VALUES (?,?)", row)

conn1.commit()
conn1.close()
conn2.commit()
conn2.close()