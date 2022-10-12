import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import logging
from pdb import post_mortem
from pickle import GET
import azure.functions as func
import pyodbc
# from dataFormat import Format
from DatabaseOperations import DBOperations


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Inserting the data in the Accounts Table.')
    req_body = req.get_json()
    accountData = req_body
    connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=USMUMSAPAN11\SQLEXPRESS;'
                      'Database=CurrentDayTransaction;'
                      'Trusted_Connection=yes;')

    cursor= connection.cursor()

    if req.method == "POST":
        try:
            message,status=DBOperations.PostAccountData(accountData)
        except Exception as err:
            print("Exception occured while inserting the data into Accounts: ",err)
            return func.HttpResponse(err,status_code=400)
        finally:
            cursor.close()
            connection.close()
        return func.HttpResponse(message,
                                        status_code=200)
    else:
        return func.HttpResponse("GET METHOD",status_code=200)