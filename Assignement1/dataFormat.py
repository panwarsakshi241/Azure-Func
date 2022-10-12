class Format:
    def format(**Accountdata):
        AccountDataTemplate = {"bankCode":"",
        "accountNumber":"",
        "userGroupId":"",
        "accountName":"",
        "currencyCode":"",
        "accountType":"",
        "accountState":"",
        "accountSubType":"",
        "BIC":"",
        "ABA":"",
        "address1":"",
        "address2":"",
        "address3":"",
        "address4":"",
        "city":"",
        "state":"",
        "province":"",
        "postalCode":"",
        "countryCode":"",
        "status":"",
        "branchId":"",
        "emailAddress":"",
        "clientAccountName":"",
        "imageAccessSetting":"",
        "tranType":""
        }

        # columns = tuple(Accountdata.keys())
        # values = tuple(Accountdata.values())
        try:
            for key, value in Accountdata.items():
                AccountDataTemplate[key] = value
        except Exception as exc:
            print("Exception occured while formatting the data :",exc)
        
        return AccountDataTemplate
