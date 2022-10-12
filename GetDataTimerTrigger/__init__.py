import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import azure.functions as func
from dbOperations import DBOperations
import logging
from BAI2Formatting import BAI2
from FileHandling import FileHandler


def main(mytimer: func.TimerRequest) -> None:

    """
    Task :
    Read the data from the Account table and TransactionInfo Table {file : dbOperations.py}
    Format the data in BAI2 format {file : BAI2Formating.py}
    Writing the data in the file{file : FileHandling.py}

    """
    try:
        # """
		# Adding header in the file.
		# """
        # dataHeader=BAI2.headerFormating()
        # FileHandler.writeHeaderTrailer(dataHeader)

        DBOperations.readDataFromAccount()

        """
        Writing Trailer/closings in the file.
        """
        # DataTrailer = BAI2.TrailerFormatting()
        # logging.info("Data Trailer Template : ",DataTrailer)
        # print("DatatrailerTemplate: ",DataTrailer,"\n Adding the Trailer.")
        # FileHandler.writeHeaderTrailer(DataTrailer)
        # print("\n file closed trailer added")
        # FileHandler.fileCloser()

    except Exception as err:
        print("Exception: ",err)
