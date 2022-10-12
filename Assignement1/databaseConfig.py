import pyodbc
import logging

"""
Create the MySQL database connection.
"""


class DBConnection:
    # def __init__(self):
    #     self.Driver = db_params('Driver')
    #     self.Server = db_params('Server')
    #     self.Database = db_params('Database')
    #     self.Trusted_Connection = db_params('Trusted_Connection')

    """
    Create the (local) DB Connections.
    """

    def createConnection():
        try:
            db = pyodbc.connect('Driver={SQL Server};'
                                'Server=USMUMSAPAN11\SQLEXPRESS;'
                                'Database=CurrentDayTransaction;'
                                'Trusted_Connection=yes;')
            status = True
            return (db, status)
        except Exception as dbException:
            logging.info("Exception occured while connecting to db")
            status = False
            return (f"Exception occured while connecting to db: {dbException}", status)
