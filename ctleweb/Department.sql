BEGIN TRANSACTION;
CREATE TABLE "Department" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
INSERT INTO `Department` (id,name) VALUES (1,'Accounting'),
 (2,'Annual Given Programs'),
 (3,'Art & History'),
 (4,'Athletics'),
 (5,'Biology'),
 (6,'Business'),
 (7,'Career Services'),
 (8,'Chemistry'),
 (9,'Communication'),
 (10,'Computer Science'),
 (11,'Counseling'),
 (12,'Criminal Justice'),
 (13,'CTLE'),
 (14,'Education'),
 (15,'English'),
 (16,'Exercise Science'),
 (17,'FAC'),
 (18,'Foreign Languages'),
 (19,'HADM'),
 (20,'HAHR'),
 (21,'History'),
 (22,'Human Resources'),
 (23,'ISP'),
 (24,'KSOM'),
 (25,'Library'),
 (26,'Management'),
 (27,'Mathematics'),
 (28,'Multicultural Affairs'),
 (29,'Nursing'),
 (30,'Occupational Therapy'),
 (31,'OIM'),
 (32,'PCPS'),
 (33,'Philosphy'),
 (34,'Physical Therapy'),
 (35,'Physics'),
 (36,'Psychology'),
 (37,'Public Safety'),
 (38,'Recreation'),
 (39,'Student'),
 (40,'Student Affairs'),
 (41,'Theology'),
 (42,'Wellness Center'),
 (43,'World Languages and Cultures');
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
