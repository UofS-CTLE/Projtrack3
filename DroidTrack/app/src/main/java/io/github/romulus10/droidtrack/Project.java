package io.github.romulus10.droidtrack;

/**
 * Created by Sean Batzel on 6/17/2017.
 */

public class Project {
    public int id;
    public String title;
    public String description;
    public String date;
    public Type type;
    public boolean walk_in;
    public Client client;
    public Semester semester;
    public int hours;
    public boolean completed;
    public boolean deleted;

    @Override
    public String toString() {
        return this.title;
    }
}
