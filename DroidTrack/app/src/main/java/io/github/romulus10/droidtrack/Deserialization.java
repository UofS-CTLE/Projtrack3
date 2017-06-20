package io.github.romulus10.droidtrack;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Sean Batzel on 6/17/2017.
 */

class Deserialization {

    static List<Project> projects;
    static List<Client> clients;
    static List<Department> departments;
    static List<Type> types;
    static List<Semester> semesters;

    static String user;
    static String pass;

    Deserialization() {
        projects = new ArrayList<>();
        clients = new ArrayList<>();
        departments = new ArrayList<>();
        types = new ArrayList<>();
        semesters = new ArrayList<>();
    }

    static void parseOutJSON(String json, String type) throws JSONException {
        JSONObject jsonObject = new JSONObject(json);
        JSONArray jsonArray = jsonObject.getJSONArray("results");
        switch (type) {
            case "Projects":
                for (int i = 0; i < jsonArray.length(); i++) {
                    projects.add(parseProject(jsonArray.getJSONObject(i)));
                }
                break;
            case "Clients":
                for (int i = 0; i < jsonArray.length(); i++) {
                    clients.add(parseClient(jsonArray.getJSONObject(i)));
                }
                break;
            case "Departments":
                for (int i = 0; i < jsonArray.length(); i++) {
                    departments.add(parseDepartment(jsonArray.getJSONObject(i)));
                }
                break;
            case "Types":
                for (int i = 0; i < jsonArray.length(); i++) {
                    types.add(parseType(jsonArray.getJSONObject(i)));
                }
                break;
            case "Semesters":
                for (int i = 0; i < jsonArray.length(); i++) {
                    semesters.add(parseSemester(jsonArray.getJSONObject(i)));
                }
                break;
        }
    }

    private static Project parseProject(JSONObject jsonObject) throws JSONException {
        Project project = new Project();
        project.id = jsonObject.getInt("id");
        project.title = jsonObject.getString("title");
        project.description = jsonObject.getString("description");
        project.date = jsonObject.getString("date");
        project.type = parseType(jsonObject);
        project.walk_in = jsonObject.getBoolean("walk_in");
        project.client = parseClient(jsonObject);
        project.semester = parseSemester(jsonObject);
        project.hours = jsonObject.getInt("hours");
        project.completed = jsonObject.getBoolean("completed");
        project.completed = jsonObject.getBoolean("deleted");
        return project;
    }

    private static Client parseClient(JSONObject jsonObject) throws JSONException {
        Client client = new Client();
        client.id = jsonObject.getInt("id");
        client.first_name = jsonObject.getString("first_name");
        client.last_name = jsonObject.getString("last_name");
        client.email = jsonObject.getString("email");
        client.department = parseDepartment(jsonObject);
        return client;
    }

    private static Department parseDepartment(JSONObject jsonObject) throws JSONException {
        Department department = new Department();
        department.id = jsonObject.getInt("id");
        department.name = jsonObject.getString("name");
        return department;
    }

    private static Type parseType(JSONObject jsonObject) throws JSONException {
        Type type = new Type();
        type.id = jsonObject.getInt("id");
        type.name = jsonObject.getString("name");
        return type;
    }

    private static Semester parseSemester(JSONObject jsonObject) throws JSONException {
        Semester semester = new Semester();
        semester.id = jsonObject.getInt("id");
        semester.name = jsonObject.getString("name");
        return semester;
    }
}