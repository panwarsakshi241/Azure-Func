from tkinter import E
from typing import final
from BAI2Formatting import BAI2
from FileHandling import FileHandler
from decimal import *
from dbConnection import DBConnection
import logging


# class DBOperations:
#     def readDataFromAccount():
connection, status = DBConnection.createConnection()
if status:
    cursor = connection.cursor()
else:
    exceptionMessage = connection
    # return exceptionMessage
    print(exceptionMessage)
try:
    dataHeader = BAI2.headerFormating()
    message, status = FileHandler.writeHeaderTrailer(dataHeader)
    if status:
        getAccountNumbersquery = "SELECT accountNumber FROM Account;"
        cursor.execute(getAccountNumbersquery)
        accountNumbers = cursor.fetchall()
        print("accountNumbers : ", accountNumbers)
        for accountNo in accountNumbers:

            cursor.execute(
                "SELECT acc.accountNumber,trans.transactionCode,trans.amount, trans.tranId,trans.debitCreditIndicator, trans.TraceNumber FROM Account acc INNER JOIN TransactionInfo trans ON acc.accountNumber=? and trans.AccountNo=?", accountNo[0], accountNo[0])
            accountTransactionDetails = cursor.fetchall()
            accountTransactionresults = [
                tuple(str(item) for item in t) for t in accountTransactionDetails]

            logging.info("Accoun Transacion Result",
                         accountTransactionresults)
            BAI2.Formatting(accountTransactionresults)
    else:
        # return message,status
        print(message, status)
except Exception as err:
    logging.info(
        "Exception occured while fetching data from the db.", err)
    print("Exception occured while fetching data from the db.", err)
finally:
    """
    Writing Trailer/closings in the file.
    """
    DataTrailer = BAI2.TrailerFormatting()
    logging.info("Data Trailer Template : ", DataTrailer)
    print("DatatrailerTemplate: ", DataTrailer, "\n Adding the Trailer.")
    # FileHandler.WriteIntoFile(DataTrailer,continuationList=continuationLst)
    message, status = FileHandler.writeHeaderTrailer(DataTrailer)
    if status:
        print("\n file closed!!!")
        filename="samplebai5.bai"
        message, status = FileHandler.fileCloser(filename)
        if status:
            pass
        else:
            # return message,status
            print(message)
    cursor.close()
    connection.close()
