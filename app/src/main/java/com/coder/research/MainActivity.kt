package com.coder.research

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.annotation.UiThread
import android.util.Log
import android.widget.Button
import android.widget.TextView
import org.jetbrains.anko.custom.async
import org.jetbrains.anko.doAsync
import org.jetbrains.anko.uiThread
import java.net.URL

class MainActivity : AppCompatActivity() {


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val jsonButton = findViewById<Button>(R.id.button_getJson)
        val textDisplay = findViewById<TextView>(R.id.text_json)


        jsonButton.setOnClickListener{

            doAsync{
               var result = URL(BuildConfig.APP_URL+"/CPU").readText()
                uiThread {
                    Log.d("Request", result)
                    textDisplay.text = result
                }
            }
        }

    }


}
