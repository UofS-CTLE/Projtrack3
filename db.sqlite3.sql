BEGIN TRANSACTION;
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO `django_session` (session_key,session_data,expire_date) VALUES ('ycvuoi1xy8ed81pxktjpvg4vhfarskwu','MDAyZGNmN2ZjODk3ZjEwNjNiYzVlMjZmOTViYzIwZjhlZGIzYjgzYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzM2YyZjdlYzE5MTZiMmUyZGYxZjQyZjE1NWVmMTQ1NTgxMjk5MWY4In0=','2017-02-02 18:06:24.063203');
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (1,'contenttypes','0001_initial','2017-01-19 18:05:39.523122'),
 (2,'auth','0001_initial','2017-01-19 18:05:39.546371'),
 (3,'admin','0001_initial','2017-01-19 18:05:39.567636'),
 (4,'admin','0002_logentry_remove_auto_add','2017-01-19 18:05:39.587160'),
 (5,'contenttypes','0002_remove_content_type_name','2017-01-19 18:05:39.639998'),
 (6,'auth','0002_alter_permission_name_max_length','2017-01-19 18:05:39.656262'),
 (7,'auth','0003_alter_user_email_max_length','2017-01-19 18:05:39.676174'),
 (8,'auth','0004_alter_user_username_opts','2017-01-19 18:05:39.691657'),
 (9,'auth','0005_alter_user_last_login_null','2017-01-19 18:05:39.710830'),
 (10,'auth','0006_require_contenttypes_0002','2017-01-19 18:05:39.712973'),
 (11,'auth','0007_alter_validators_add_error_messages','2017-01-19 18:05:39.728262'),
 (12,'auth','0008_alter_user_username_max_length','2017-01-19 18:05:39.744621'),
 (13,'projtrack','0001_initial','2017-01-19 18:05:39.791689'),
 (14,'sessions','0001_initial','2017-01-19 18:05:39.800438');
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO `django_content_type` (id,app_label,model) VALUES (1,'projtrack','semester'),
 (2,'projtrack','user'),
 (3,'projtrack','project'),
 (4,'projtrack','department'),
 (5,'projtrack','client'),
 (6,'projtrack','type'),
 (7,'admin','logentry'),
 (8,'auth','permission'),
 (9,'auth','group'),
 (10,'auth','user'),
 (11,'contenttypes','contenttype'),
 (12,'sessions','session');
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "action_time" datetime NOT NULL);
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"));
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" ("id"));
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "username" varchar(150) NOT NULL UNIQUE);
INSERT INTO `auth_user` (id,password,last_login,is_superuser,first_name,last_name,email,is_staff,is_active,date_joined,username) VALUES (1,'pbkdf2_sha256$30000$f7j845T3o9vk$NIFT6AVBbFOwYAFz0o/USc+RUNmpdhH7Wb0CrzRQ0go=','2017-01-19 18:06:24.035066',1,'','','cyclerdannj@gmail.com',1,1,'2017-01-19 18:06:03.428916','daniel');
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (1,1,'add_semester','Can add semester'),
 (2,1,'change_semester','Can change semester'),
 (3,1,'delete_semester','Can delete semester'),
 (4,2,'add_user','Can add user'),
 (5,2,'change_user','Can change user'),
 (6,2,'delete_user','Can delete user'),
 (7,3,'add_project','Can add project'),
 (8,3,'change_project','Can change project'),
 (9,3,'delete_project','Can delete project'),
 (10,4,'add_department','Can add department'),
 (11,4,'change_department','Can change department'),
 (12,4,'delete_department','Can delete department'),
 (13,5,'add_client','Can add client'),
 (14,5,'change_client','Can change client'),
 (15,5,'delete_client','Can delete client'),
 (16,6,'add_type','Can add type'),
 (17,6,'change_type','Can change type'),
 (18,6,'delete_type','Can delete type'),
 (19,7,'add_logentry','Can add log entry'),
 (20,7,'change_logentry','Can change log entry'),
 (21,7,'delete_logentry','Can delete log entry'),
 (22,8,'add_permission','Can add permission'),
 (23,8,'change_permission','Can change permission'),
 (24,8,'delete_permission','Can delete permission'),
 (25,9,'add_group','Can add group'),
 (26,9,'change_group','Can change group'),
 (27,9,'delete_group','Can delete group'),
 (28,10,'add_user','Can add user'),
 (29,10,'change_user','Can change user'),
 (30,10,'delete_user','Can delete user'),
 (31,11,'add_contenttype','Can add content type'),
 (32,11,'change_contenttype','Can change content type'),
 (33,11,'delete_contenttype','Can delete content type'),
 (34,12,'add_session','Can add session'),
 (35,12,'change_session','Can change session'),
 (36,12,'delete_session','Can delete session');
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"));
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE "User" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "username" varchar(100) NOT NULL);
CREATE TABLE "Type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
CREATE TABLE "Semester" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
CREATE TABLE "Project" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "description" varchar(500) NOT NULL, "walk_in" bool NOT NULL, "client_id" integer NOT NULL REFERENCES "Client" ("id"), "semester_id" integer NOT NULL REFERENCES "Semester" ("id"), "type_id" integer NOT NULL REFERENCES "Type" ("id"), "users_id" integer NOT NULL REFERENCES "User" ("id"));
CREATE TABLE "Department" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
CREATE TABLE "Client" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(100) NOT NULL, "last_name" varchar(100) NOT NULL, "email" varchar(100) NOT NULL, "department_id" integer NOT NULL REFERENCES "Department" ("id"));
CREATE INDEX "django_session_de54fa62" ON "django_session" ("expire_date");
CREATE UNIQUE INDEX "django_content_type_app_label_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE INDEX "django_admin_log_e8701ad4" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_417f1b1c" ON "django_admin_log" ("content_type_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_e8701ad4" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_8373b171" ON "auth_user_user_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_e8701ad4" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_0e939a4f" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_permission_content_type_id_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_417f1b1c" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "auth_group_permissions_group_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_8373b171" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_group_permissions_0e939a4f" ON "auth_group_permissions" ("group_id");
CREATE INDEX "Project_df138c17" ON "Project" ("users_id");
CREATE INDEX "Project_94757cae" ON "Project" ("type_id");
CREATE INDEX "Project_5d4db337" ON "Project" ("semester_id");
CREATE INDEX "Project_2bfe9d72" ON "Project" ("client_id");
CREATE INDEX "Client_bf691be4" ON "Client" ("department_id");
COMMIT;
