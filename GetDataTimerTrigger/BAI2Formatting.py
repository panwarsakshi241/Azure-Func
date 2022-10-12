from datetime import datetime
import copy
import decimal
import logging
from FileHandling import FileHandler


class BAI2:

    def headerFormating():
        now = datetime.now()
        date = str(now).split(" ")
        dt = f"{date[0].replace('-','')},{date[1][:5].replace(':','')}"

        FileHeader = f"01,122241255,122241255,{dt},01,80,,2/"
        GroupHeader = f"02,122241255,122241255,1,{dt},,3/"

        dataHeaderTemplate = {
            "File-Header": FileHeader,
            "Group-Header": GroupHeader
        }
        logging.info("DataHeaderTemplate=", dataHeaderTemplate)
        print("DataHeaderTemplate=", dataHeaderTemplate)

        return dataHeaderTemplate

    """
    Function to format the Account and tranction data.
    """

    def Formatting(ListOfTransactionDetail):

        AccountIdentifierTemplate = {"Record-Code": "03",
                                     "Customer-Account-Number": "",
                                     "Currency-Code": "",
                                     "Type-Code": "",
                                     "Amount": "",
                                     "Item-Count": "",
                                     "Funds-type": "",
                                     "Value-Date": "",
                                     "One-Day-Availablity": "",
                                     "Two-or-more-days-Availability": "",
                                     "Delimiters": "/"
                                     }
        TransactionDetailTemplate = {"Record-Code": "16",
                                     "Type-Code": "",
                                     "Amount": "",
                                     "Funds-Type": "",
                                     "Value-Date": "",
                                     "One-day-Availability": "",
                                     "Two-or-days-availability": "",
                                     "Bank-reference-Number": "",
                                     "Customer-reference-number": "",
                                     "Text": "",
                                     "Delimiters": "/"
                                     }

        continuationTemplate = {"Record-code": "88",
                                "Next-field": ""}
        AccountTrailerTemplate = "49,+24592,5/"
        GroupTrailerTemplate = "98,+1869592,2,14/"
        FileTransferTemplate = "99,+1869592,1,16/"

        dataTemplate = {"Account-Identifier": "",
                        "Transaction-Detail": "",
                        "Account-Trailer": ""
                        }
        AccountTrailerTemplate={
            "Record-code":"49",
            "AccountControlTotal":"",
            "NumberOfRecords":"",
            "Delimiter":"/"
        }

        BAI2Template = copy.deepcopy(dataTemplate)

        transactionInfoList = []
        continuationList = []
        ContinuationFields = {"tranId": 3,
                              "debitCreditIndicator": 4, "TraceNumber": 5}

        AccountControlTotal=0
        Records49=0
        for i in ListOfTransactionDetail:
            Records49+=1
            transactionInfoSublist = []
            AccountIdentifierTemplate["Customer-Account-Number"] = i[0]
            TypeCode = i[1]
            Amount = i[2]
            deciAmt=float(Amount)
            print("deciAmt : ",deciAmt)
            AccountControlTotal+=deciAmt
            transactionInfoStr = f"16,{TypeCode},{Amount},0,,,,,,,/"
            transactionInfoSublist.append(transactionInfoStr)
            continuationsubList = []
            for fld, ind in ContinuationFields.items():
                logging.info(fld, "=", i[ind])
                Records49+=1
                key = fld
                value = i[ind]
                continuationStr = f"88,{key}={value}"
                continuationsubList.append(continuationStr)
            transactionInfoList.append(transactionInfoSublist)
            continuationList.append(continuationsubList)

        logging.info("continuationList: ", continuationList)
        logging.info("TransactionInforList: ", transactionInfoList)

        account = ""
        for v in AccountIdentifierTemplate.values():
            account = f"{account}{v},"
        account = account.rstrip(account[-1])

        # TotalRecords=FileHandler.Totalrecords()
        Account49=Records49+2

        AccountTrailerTemplate["AccountControlTotal"]=AccountControlTotal
        AccountTrailerTemplate["NumberOfRecords"]=Account49

        AccountTrailer = ""
        for v in AccountTrailerTemplate.values():
            AccountTrailer = f"{AccountTrailer}{str(v)},"
        AccountTrailer = AccountTrailer.rstrip(AccountTrailer[-1])

        print("AccountTrailerTemplatestring: ",AccountTrailer)

        logging.info("accountIdentifier: ", account)
        logging.info("transactionDetailsList: ", transactionInfoList)

        dataTemplate["Account-Identifier"] = account
        dataTemplate["Transaction-Detail"] = transactionInfoList
        dataTemplate["Account-Trailer"] = AccountTrailer

        print(dataTemplate, "\n Writing data in file.")
        logging.info(dataTemplate, "\n Writing data in file.")

        FileHandler.WriteIntoFile(dataTemplate, continuationList)

    def TrailerFormatting():
        """
        This function is :
            1. To compute the document's trailer part.
            2. To format the document's trailer part.
        """
        dataTrailerTemplate = {"Group-Trailer": "",
                               "File-Transfer": ""
                            }
        RecordsCount= FileHandler.Totalrecords()
        
        Account03=RecordsCount["TotalAccounts"]//2

        GroupTrailerTemplate={"Record-Code":"98",
        "Group-Control-Total":RecordsCount["Amount49"],
        "Number-of-Accounts":Account03,
        "Number-of-Records":RecordsCount["TotalGroupsRecords"],
        "Delimiters":"/"
        }

        FileTransferTemplate={"Record-Code":"99",
        "File-Control-Total":RecordsCount["Amount49"],
        "Number-of-Groups":RecordsCount["TotalGroups"],
        "Number-of-Records":RecordsCount["TotalFilesRecords"],
        "Delimiters":"/"
        }

        Group = ""
        for v in GroupTrailerTemplate.values():
            Group = f"{Group}{str(v)},"
        Group = Group.rstrip(Group[-1])

        fileTransfer = ""
        for v in FileTransferTemplate.values():
            fileTransfer = f"{fileTransfer}{str(v)},"
        fileTransfer = fileTransfer.rstrip(fileTransfer[-1])

        dataTrailerTemplate["Group-Trailer"]=Group
        dataTrailerTemplate["File-Transfer"]=fileTransfer

        return dataTrailerTemplate
