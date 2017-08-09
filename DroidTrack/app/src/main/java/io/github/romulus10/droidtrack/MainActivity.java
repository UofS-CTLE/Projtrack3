package io.github.romulus10.droidtrack;

import android.app.FragmentTransaction;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Toast;

import org.json.JSONException;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener,
        MainFragment.OnFragmentInteractionListener,
        AddProjectFragment.OnFragmentInteractionListener,
        ProjectFragment.OnListFragmentInteractionListener,
        ClientFragment.OnListFragmentInteractionListener,
        DepartmentFragment.OnListFragmentInteractionListener,
        TypeFragment.OnListFragmentInteractionListener,
        SemesterFragment.OnListFragmentInteractionListener {

    @Override
    public void onFragmentInteraction(Uri uri) {

    }

    @Override
    public void onListFragmentInteraction(Project item) {

    }

    @Override
    public void onListFragmentInteraction(Department item) {

    }

    @Override
    public void onListFragmentInteraction(Client item) {

    }

    @Override
    public void onListFragmentInteraction(Type item) {

    }

    @Override
    public void onListFragmentInteraction(Semester item) {

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);

        ProjtrackService projtrackService = new ProjtrackService();
        projtrackService.execute();

        if (!projtrackService.logged_in) {
            Toast.makeText(getApplicationContext(),
                    "Login failed. Check your username and password.",
                    Toast.LENGTH_LONG).show();
        }

        MainFragment fragment = new MainFragment();
        getFragmentManager().beginTransaction()
                .add(R.id.content, fragment).addToBackStack(null)
                .commit();
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_home) {
            MainFragment newFragment = new MainFragment();
            FragmentTransaction ft = getFragmentManager().beginTransaction();
            ft.replace(R.id.content, newFragment).addToBackStack(null).commit();
        } else if (id == R.id.nav_my_projects) {
            ProjectFragment newFragment = new ProjectFragment();
            FragmentTransaction ft = getFragmentManager().beginTransaction();
            ft.replace(R.id.content, newFragment).addToBackStack(null).commit();
        } else if (id == R.id.nav_add_project) {
            AddProjectFragment newFragment = new AddProjectFragment();
            FragmentTransaction ft = getFragmentManager().beginTransaction();
            ft.replace(R.id.content, newFragment).addToBackStack(null).commit();
        } else if (id == R.id.nav_clients) {
            ClientFragment newFragment = new ClientFragment();
            FragmentTransaction ft = getFragmentManager().beginTransaction();
            ft.replace(R.id.content, newFragment).addToBackStack(null).commit();
        } else if (id == R.id.nav_departments) {
            DepartmentFragment newFragment = new DepartmentFragment();
            FragmentTransaction ft = getFragmentManager().beginTransaction();
            ft.replace(R.id.content, newFragment).addToBackStack(null).commit();
        } else if (id == R.id.nav_types) {
            TypeFragment newFragment = new TypeFragment();
            FragmentTransaction ft = getFragmentManager().beginTransaction();
            ft.replace(R.id.content, newFragment).addToBackStack(null).commit();
        } else if (id == R.id.nav_semesters) {
            SemesterFragment newFragment = new SemesterFragment();
            FragmentTransaction ft = getFragmentManager().beginTransaction();
            ft.replace(R.id.content, newFragment).addToBackStack(null).commit();
        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
