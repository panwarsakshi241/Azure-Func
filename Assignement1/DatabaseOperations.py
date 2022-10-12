from multiprocessing.connection import Connection
from sqlite3 import Cursor
from typing import final
from decimal import Decimal
from GetDataTimerTrigger import BAI2Formatting
from databaseConfig import DBConnection

class DBOperations:

	def PostAccountData(accountData):
		connection, status = DBConnection.createConnection()
		if status:
			cursor = connection.cursor()
		else:
			return connection, status
		try:
			v = tuple(accountData.values())
			cursor.execute("Insert INTO Account (bankCode, accountNumber, userGroupId, accountName, currencyCode, accountType, accountState, accountSubType, BIC, ABA, address1, address2, address3, address4, city, state, province, postalCode, countryCode, status, branchId, emailAddress, clientAccountName, imageAccessSetting, tranType) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9],v[10],v[11],v[12],v[13],v[14],v[15],v[16],v[17],v[18],v[19],v[20],v[21],v[22],v[23],v[24])
			connection.commit()
			print("Data Inserted Successfully.")
		except Exception as err:
			return f"Exception occurred while writing the data in the database: {err}",False
		return "Successfully Inserted",True
		


		


