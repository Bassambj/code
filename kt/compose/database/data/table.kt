package com.bassam.database.data

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "tab")
data class Table(
    @PrimaryKey
    val id: Int = 0,
    val name: String,
    val numberInt: Int,
    val numberDouble: Double,
    val logic: Boolean,
    val image: Long,
    val text: String
)