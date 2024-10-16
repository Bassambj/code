package com.bassam.database.data

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import kotlinx.coroutines.flow.Flow

@Dao
interface TableDao {
    @Query("SELECT * from tab ORDER BY name ASC")
    fun getAllItens(): Flow<List<Table>>

    @Insert(onConflict = OnConflictStrategy.IGNORE)
    suspend fun insert(table: Table)

    @Update
    suspend fun update(table: Table)

    @Delete
    suspend fun delete(table: Table)
    }