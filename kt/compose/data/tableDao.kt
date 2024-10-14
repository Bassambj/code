@Dao
interface tabDao01 {
    @Query("SELECT * from tab01 ORDER BY ASC")
    fun getAllItems(): Flow<List<Table01>>

}

interface tabDao02 {
    @Query("SELECT * from tab02 ORDER BY ASC")
    fun getAllItems(): Flow<List<Table02>>

}