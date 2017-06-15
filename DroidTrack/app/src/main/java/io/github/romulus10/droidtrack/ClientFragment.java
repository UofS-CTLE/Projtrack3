package io.github.romulus10.droidtrack;

import android.content.Context;
import android.os.Bundle;
import android.app.Fragment;
import android.support.v7.widget.GridLayoutManager;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;

import com.loopj.android.http.JsonHttpResponseHandler;
import com.loopj.android.http.RequestParams;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import cz.msebera.android.httpclient.Header;
import io.github.romulus10.droidtrack.dummy.DummyContent;
import io.github.romulus10.droidtrack.dummy.DummyContent.DummyItem;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * A fragment representing a list of Items.
 * <p/>
 * Activities containing this fragment MUST implement the {@link OnListFragmentInteractionListener}
 * interface.
 */
public class ClientFragment extends Fragment {

    // TODO: Customize parameter argument names
    private static final String ARG_COLUMN_COUNT = "column-count";
    // TODO: Customize parameters
    private int mColumnCount = 1;
    private OnListFragmentInteractionListener mListener;

    JSONArray jArray;

    /**
     * Mandatory empty constructor for the fragment manager to instantiate the
     * fragment (e.g. upon screen orientation changes).
     */
    public ClientFragment() {
    }

    // TODO: Customize parameter initialization
    @SuppressWarnings("unused")
    public static ClientFragment newInstance(int columnCount) {
        ClientFragment fragment = new ClientFragment();
        Bundle args = new Bundle();
        args.putInt(ARG_COLUMN_COUNT, columnCount);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        if (getArguments() != null) {
            mColumnCount = getArguments().getInt(ARG_COLUMN_COUNT);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_client_list, container, false);

        // Set the adapter
        if (view instanceof RecyclerView) {
            Context context = view.getContext();
            RecyclerView recyclerView = (RecyclerView) view;
            if (mColumnCount <= 1) {
                recyclerView.setLayoutManager(new LinearLayoutManager(context));
            } else {
                recyclerView.setLayoutManager(new GridLayoutManager(context, mColumnCount));
            }
            recyclerView.setAdapter(new MyClientRecyclerViewAdapter(DummyContent.ITEMS, mListener));
        }
        return view;
    }

    public void apiCall() throws JSONException {
        RequestParams rp = new RequestParams();
        String username = ((MainActivity)getActivity()).username;
        String password = ((MainActivity)getActivity()).password;
        rp.add("username", username);
        rp.add("password", password);
        String url = "api_clients";
        HttpUtils.get(url, rp, new JsonHttpResponseHandler() {
            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONObject response) {

            }

            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONArray response) {
                try {
                    jArray = new JSONArray(response);
                    Log.d("CLIENT FRAGMENT", response.toString());
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        });
        ArrayList<String> lst = new ArrayList<String>();
        if (jArray != null) {
            for (int i = 0; i < jArray.length(); i++) {
                try {
                    lst.add(jArray.getString(i));
                } catch (JSONException e) {
                    Log.d("CLIENT_FRAGMENT", "JSONException.");
                }
            }
        }
        final ArrayAdapter<String> aa = new ArrayAdapter<String>(getActivity(),android.R.layout.simple_list_item_1, lst);
    }


    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        if (context instanceof OnListFragmentInteractionListener) {
            mListener = (OnListFragmentInteractionListener) context;
        } else {
            throw new RuntimeException(context.toString()
                    + " must implement OnListFragmentInteractionListener");
        }
    }

    @Override
    public void onDetach() {
        super.onDetach();
        mListener = null;
    }

    /**
     * This interface must be implemented by activities that contain this
     * fragment to allow an interaction in this fragment to be communicated
     * to the activity and potentially other fragments contained in that
     * activity.
     * <p/>
     * See the Android Training lesson <a href=
     * "http://developer.android.com/training/basics/fragments/communicating.html"
     * >Communicating with Other Fragments</a> for more information.
     */
    public interface OnListFragmentInteractionListener {
        // TODO: Update argument type and name
        void onListFragmentInteraction(DummyItem item);
    }
}
