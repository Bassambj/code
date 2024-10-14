package kt.compose.data

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "tab01")
data class Table01(
    @PrimaryKey(autorgenarete = true)
    val name: String,
    val numberInt: Int,
    val numberDouble: Double,
    val boolen: Boolean,
    val image: Long,
    val text: String
)