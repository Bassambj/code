package com.bassam.database.data

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase


@Database(entities = [Table::class], version = 1, exportSchema = false)

abstract class TableDatabase : RoomDatabase(){

    // Retorna cada item Dao para conhecimento do BD
    abstract fun tab(): TableDao

    companion object{ // acesso aos metodos
        @Volatile // @Volatile para não gravar em cache - garante a atualização da Instance.
        private var Instance: TableDatabase? = null
        fun getDatabase(context: Context): TableDatabase{
            return Instance ?: synchronized(this){
                // Verificar erros
                Room.databaseBuilder(context, TableDatabase::class.java,"table_database")
                    .fallbackToDestructiveMigrationFrom()
                    .build()
                    .also{ Instance = it}
            }
        }
    }
}