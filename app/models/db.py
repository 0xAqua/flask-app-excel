import sqlite3


DATABASE: str = 'invoice_master.db'


class DataBase(object):
    """ DataBase Class object

    * create_db: Crate Table
    * all_data:  Get all data
    * one_data: Get one data
    * delete: Delete one data

    Attributes:
        table_name: Table name to create in database.
    """
    def __init__(self, table_name: str) -> None:
        """Init DataBase with blah."""
        self.table_name = table_name

    def create_db(self, value: str) -> None:
        """ Create Table

        * Create a table
        * Create a new database if it doesn't exist
        * Write a SQL statement to create a table in a sql variable

        Returns:
            None
        """
        con = sqlite3.connect(DATABASE, check_same_thread=False)
        sql: str = f'''
            CREATE TABLE IF NOT EXISTS 
                {self.table_name}({value}) 
            '''
        con.execute(sql)
        con.close()

    def all_data(self) -> list:
        """ Get all data

        * Receive in an array by setting the data connected to the database to Row.
        * Write a SQL statement that retrieves all data.
        * Table uses attribute values
        * Execute SQL, get everything and store in "data" variable

        Returns:
            data: Array for all data in the table
        """
        con = sqlite3.connect(DATABASE, check_same_thread=False)
        con.row_factory = sqlite3.Row
        sql = f'SELECT * FROM {self.table_name}'
        data = con.execute(sql).fetchall()
        con.close()

        return data

    def one_data(self, col_id: str, data_id: str) -> str:
        """ Get one data

        * Receive in an array by setting the data connected to the database to Row.
        * Write a SQL statement that retrieves one data.
        * Table uses attribute values
        * Execute SQL, get everything and store in "data" variable

        Args:
            col_id: Table id name
            data_id: data id
        Returns:
            data: string object
        """
        con = sqlite3.connect(DATABASE)
        con.row_factory = sqlite3.Row
        sql = f'''
            SELECT
                *
            FROM
                {self.table_name}
            WHERE
                {col_id} = ?
            '''
        data = con.execute(sql, data_id).fetchone()

        return data

    def delete(self, col_id, data_id) -> None:
        """ Delete one data

        * Write a SQL statement that delete one data.
        * Table uses attribute values
        * Execute SQL, get everything and store in "data" variable

        Args:
            col_id: Table id name
            data_id: data id
        """
        con = sqlite3.connect(DATABASE)
        sql = f'''
            DELETE FROM
                {self.table_name}
            WHERE
                {col_id} = ?
        '''
        con.execute(sql, data_id)
        con.commit()
