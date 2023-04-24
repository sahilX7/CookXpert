package com.app.android.cookxpert;
import android.os.Build;
import android.os.Bundle;
import android.view.Window;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import org.json.JSONException;
import org.json.JSONObject;
import java.util.HashMap;
import java.util.Map;

public class RecipeActivity extends AppCompatActivity {
    String url="http://ec2-52-193-241-178.ap-northeast-1.compute.amazonaws.com:8000//predict";
    TextView name_tv,nutrient_info_tv,prep_time_tv,ingredients_tv,instructions_tv;
    String food;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recipe);

        //setting status bar
        Window window = RecipeActivity.this.getWindow();
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            window.setStatusBarColor(ContextCompat.getColor(RecipeActivity.this,R.color.theme));
        }

        initViews();

        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            food = extras.getString("key");
        }

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,
            new com.android.volley.Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    try {
                        JSONObject jsonObject = new JSONObject(response);
                        String name = jsonObject.getString("Name");
                        String nutrient_info = jsonObject.getString("Nutrient Info");
                        String prep_time = jsonObject.getString("Preparation Time");
                        String ingredients = jsonObject.getString("Ingredients");
                        String instructions = jsonObject.getString("Instructions");

                        setViews(name,nutrient_info,prep_time,ingredients,instructions);

                    } catch (JSONException e) {
                        Toast.makeText(RecipeActivity.this, "Error!", Toast.LENGTH_SHORT).show();
                        e.printStackTrace();
                    }
                }
            }, new com.android.volley.Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(RecipeActivity.this, "Oops! Couldn't connect to server\nCheck internet connectivity", Toast.LENGTH_SHORT).show();
            }
            }) {

            @Override
            protected Map<String, String> getParams() {
                Map<String, String> params = new HashMap<String, String>();
                params.put("Food", food);
                return params;
            }
        };

        RequestQueue queue = Volley.newRequestQueue(RecipeActivity.this);
        queue.add(stringRequest);
    }

    private void initViews(){
        name_tv=findViewById(R.id.name);
        nutrient_info_tv=findViewById(R.id.nutrient_info);
        prep_time_tv=findViewById(R.id.prep_time);
        ingredients_tv=findViewById(R.id.ingredients);
        instructions_tv=findViewById(R.id.instructions);
    }

    private void setViews(String name,String nutrient_info,String prep_time,String ingredients,String instructions){
        name_tv.setText(name);
        nutrient_info_tv.setText(nutrient_info);
        prep_time_tv.setText(prep_time);
        ingredients_tv.setText(ingredients);
        instructions_tv.setText(instructions);
    }
}