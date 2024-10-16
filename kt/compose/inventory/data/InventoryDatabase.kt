/*
 * Copyright (C) 2023 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.inventory.data

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

/**
 * Database class with a singleton Instance object.
 */
// Todas as entidades são declaradas/atualizadas na database:
@Database(entities = [Item::class], version = 1, exportSchema = false)
// version <= controle de versionamento do bd (banco de dados).
abstract class InventoryDatabase : RoomDatabase() {

    //  Função abstrata que retorna o ItemDao para que o bd saiba sobre o DAO.
    abstract fun itemDao(): ItemDao

    //permite acesso aos métodos criar ou acessar o bd e usa o nome da classe como qualificador.
    companion object {
        @Volatile // @Volatile para não gravar em cache - garante a atualização da Instance.
        private var Instance: InventoryDatabase? = null
        /**
         *A variável Instance mantém uma referência ao banco de dados, quando uma tiver sido criada.
         *  Isso ajuda a manter uma única instância do banco de dados aberta em determinado momento,
         *  porque ela é um recurso com criação e manutenção caras.
        */

        fun getDatabase(context: Context): InventoryDatabase {
            // if the Instance is not null, return it, otherwise create a new database instance.
            return Instance ?: synchronized(this) {
                /**
                 *  Envolver o código para receber o banco de dados em um bloco synchronized
                 *  significa que somente uma linha de execução poderá entrar nesse bloco de código
                 *  por vez, garantindo que o banco de dados será inicializado apenas uma vez.
                 *  Usar o bloco synchronized{} para evitar a disputa.
                 *
                 */

                //Use o builder do banco de dados para acessar um banco de dados:
                Room.databaseBuilder(context, InventoryDatabase::class.java, "item_database")
                    /**
                     * Setting this option in your app's database builder means that Room
                     * permanently deletes all data from the tables in your database when it
                     * attempts to perform a migration with no defined migration path.
                     */
                    // Estratégia de migração necessária ao builder:
                    .fallbackToDestructiveMigration()
                    .build()
                    // Ver material sobre estratégias de migração e build.


                    .also { Instance = it }
            }
        }
    }
}
