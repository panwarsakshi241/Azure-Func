import logging
from datetime import datetime

"""
This file is to handle the All file operations.
"""


class FileHandler:

    def writeHeaderTrailer(Template):
        try:
            # version = Methods.fileversion('version')
            # filename = f"AcountTransactionData_{version}.bai"
            message = "Success"
            writeHeader = open("samplebai5.bai", "a")
            for v in Template.values():
                writeHeader.write(v)
                writeHeader.write("\n")
                status = True
        except Exception as err:
            message = f"Exception Occurred while adding the header:{err}"
            status = False
            return message, status
        finally:
            writeHeader.close()
        return message, status

    """
    Function to write the data in the samplaBai2.bai file
    """
    def WriteIntoFile(dataTemplate, continuationList):
        message = "Success"
        try:
            # version = Methods.fileversion('version')
            # filename = f"AcountTransactionData_{version}.bai"
            writedatatofile = open("samplebai5.bai", "a")
            for K, v in dataTemplate.items():
                if K == "Transaction-Detail":
                    for i in range(len(v)):
                        writedatatofile.write(v[i][0])
                        writedatatofile.write("\n")
                        """
                            write logic for continuation.
                            """
                        for desc in continuationList[i]:
                            writedatatofile.write(desc)
                            writedatatofile.write("\n")
                else:
                    writedatatofile.write(v)
                    writedatatofile.write("\n")
            status = True
        except Exception as err:
            message = f"Exception occured while writing the data in file: {err}"
            status = False
            logging.info(
                f"Exception occured while writing the data in file: {err}")
            print(
                f"Exception occured while writing the data in file: {err}")
            return message, status
        finally:
            writedatatofile.close()
        return message, status

    def fileCloser(filename):
        try:
            """
            subversion computation
            """
            now = datetime.now()
            date = str(now).split(" ")
            subvers = f"{date[0].replace('-','')}.{date[1][:8].replace(':','.')}"
            message = "Success"
            # version = Methods.fileversion('version')
            # filename = f"AcountTransactionData_{version}.bai"
            closingFile = open(filename, "a")
            closingFile.write(
                f"===================={subvers}===================")
            closingFile.write("\n")
            status = True
        except Exception as err:
            message = f"Excpetion occurred while running the fileCloser:{err}"
            status = False
            print(f"Excpetion occurred while running the fileCloser:{err}")
            logging.info(
                f"Excpetion occurred while running the fileCloser.{err}")
            return message, status
        finally:
            closingFile.close()
        return message, status

    def Totalrecords():
        TotalAccounts= 0
        TotalGroups= 0
        TotalFiles=0
        TotalTransactions=0
        TotalContinuations=0

        with open('samplebai5.bai') as fp:
            Amount49=0
            Amount98=0
            for line in fp:
                if line.startswith("01") or line.startswith("99"):
                    TotalFiles+=1
                if line.startswith("02"):
                    TotalGroups+=1
                if line.startswith("98"):
                    f=line.find(',')
                    l=line.find(',',f+1,len(line))
                    amt=line[f+1:l]
                    Amount98+=float(amt)
                    TotalGroups+=1
                if line.startswith("03"):
                    TotalAccounts+=1
                if line.startswith("49"):
                    print("Line: ",line)
                    f=line.find(',')
                    l=line.find(',',f+1,len(line))
                    amt=line[f+1:l]
                    Amount49+=float(amt)
                    TotalAccounts+=1
                if line.startswith("16"):
                    TotalTransactions+=1
                if line.startswith("88"):
                    TotalContinuations+=1
        
        TotalTransactionsRecords=TotalTransactions+TotalContinuations
        TotalAccountsRecords=TotalAccounts+TotalTransactionsRecords
        TotalGroupsRecords=TotalGroups+TotalAccountsRecords+1
        TotalfilesRecords=TotalFiles+TotalGroupsRecords+1

        RecordsCount={
            "Amount49":Amount49,
            "Amount98":Amount98,
            "TotalFiles":TotalFiles,
            "TotalGroups":TotalGroups,
            "TotalAccounts":TotalAccounts,
            "TotalTransations":TotalTransactions,
            "TotalContinuations":TotalContinuations,
            "TotalTransactionsRecords":TotalTransactionsRecords,
            "TotalAccountsRecords":TotalAccountsRecords,
            "TotalGroupsRecords":TotalGroupsRecords,
            "TotalFilesRecords":TotalfilesRecords
        }

        print("RecordCount: ",RecordsCount)

        return RecordsCount
