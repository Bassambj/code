package com.bassam.database

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.material3.Text
import androidx.compose.material3.Card
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.bassam.database.ui.theme.DatabaseTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            DatabaseTheme {
                test()
            }
        }
    }
}

object textos{
    var NameDb = "Table Database"
    var GreatDb = "Hello Database"

}



@Composable
fun test() {
    Card {
        "Database"
    }




}




@Preview(showBackground = true)
@Composable
    fun prev(){
     Text(
         "Database"
    )
}


