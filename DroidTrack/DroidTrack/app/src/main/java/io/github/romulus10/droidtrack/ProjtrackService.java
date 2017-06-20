package io.github.romulus10.droidtrack;

import android.os.AsyncTask;
import android.util.Base64;
import android.util.Log;

import org.json.JSONException;

import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Authenticator;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.PasswordAuthentication;
import java.net.URL;
import java.util.Arrays;

/**
 * Created by Sean Batzel on 6/17/2017.
 */

class ProjtrackService extends AsyncTask {

    private String json;
    public boolean logged_in;

    ProjtrackService() {

    }

    @Override
    protected Object doInBackground(Object[] params) {
        try {
            this.getProjects();
            this.getSemester();
            this.getType();
            this.getClients();
            this.getDepartments();
        } catch (JSONException e) {
            Log.d("JSONException", e.getMessage());
        }
        return new Object();
    }

    private void setUp(String url_add) {
        URL url = null;
        try {
            String SERVER = "http://192.168.1.25:8080/api/";
            url = new URL(SERVER + url_add);
        } catch (MalformedURLException e) {
            Log.d("MalformedURLException", e.getMessage());
        }
        try {
            assert url != null;
            HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
            httpURLConnection.setRequestProperty("Authorization",
                    "basic" + Arrays.toString(Base64.
                            encode((Deserialization.user + ":" + Deserialization.pass)
                                    .getBytes(),
                            Base64.NO_WRAP)));
            InputStream in = new BufferedInputStream(httpURLConnection.getInputStream());
            readStream(in);
            this.logged_in = true;
        } catch (IOException e) {
            this.logged_in = false;
            Log.d("IOException", e.getMessage());
        }
    }

    private void readStream(InputStream in) {
        try {
            java.util.Scanner s = new java.util.Scanner(in).useDelimiter("\\A");
            json = s.hasNext() ? s.next() : "";
            in.close();
            Log.d("JSON Result", json);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    void getProjects() throws JSONException {
        setUp("projects/");
        Deserialization.parseOutJSON(json, "Projects");
    }

    void getClients() throws JSONException {
        setUp("clients/");
        Deserialization.parseOutJSON(json, "Clients");
    }

    void getDepartments() throws JSONException {
        setUp("departments/");
        Deserialization.parseOutJSON(json, "Departments");
    }

    void getType() throws JSONException {
        setUp("types/");
        Deserialization.parseOutJSON(json, "Types");
    }

    void getSemester() throws JSONException {
        setUp("semesters/");
        Deserialization.parseOutJSON(json, "Semesters");
    }
}
