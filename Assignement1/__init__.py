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
            v = tuple(accountData.values())
            cursor.execute("Insert INTO Account (bankCode, accountNumber, userGroupId, accountName, currencyCode, accountType, accountState, accountSubType, BIC, ABA, address1, address2, address3, address4, city, state, province, postalCode, countryCode, status, branchId, emailAddress, clientAccountName, imageAccessSetting, tranType) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9],v[10],v[11],v[12],v[13],v[14],v[15],v[16],v[17],v[18],v[19],v[20],v[21],v[22],v[23],v[24])
            connection.commit()
            print("Data Inserted Successfully.")
        except Exception as err:
            print("Exception occured while inserting the data into Accounts: ",err)
            return func.HttpResponse(err,status_code=400)
        finally:
            cursor.close
            connection.close
        return func.HttpResponse("DATA INSERTED",
                                        status_code=200)
    else:
        return func.HttpResponse("GET METHOD",status_code=200)