package kt.compose.data

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "tab02")
data class Table02(
    @PrimaryKey(autorgenarete = true)
    val name: String,
    val numberInt: Int,
    val numberDouble: Double,
    val boolen: Boolean,
    val image: Long,
    val text: String
)