#coding=utf-8
import sys
import os
import csv
from enum import Enum
class CvsType(Enum):
    BOT = "BOT"
    CSF = "CSF"
    TCT = "TCT"
    TAB = "TAB"
csvFileName = [ "BOT","CSF","TCT","TAB", "UserUpdate" ]
csvFileType = [ ".csv", ".xls" ]
dicList = {}
commonTitle = ["MAC ADDRESS", "DESCRIPTION", "DIRECTORY NUMBER 1", "OWNER USER ID"]
updateTitle = ["USER ID", "MANAGER USER ID", "DEPARTMENT", "DEFAULT PROFILE",
                "USER LOCALE", "PASSWORD", "PIN", "TELEPHONE NUMBER", "PRIMARY EXTENSION",
                "ASSOCIATED PC", "IPCC EXTENSION", "MAIL ID", "PRESENCE GROUP", 
                "SUBSCRIBE CALLING SEARCH SPACE", "DIGEST CREDENTIALS", "REMOTE DESTINATION LIMIT",
                "MAXIMUM WAIT TIME FOR DESK PICKUP", 
                "ALLOW CONTROL OF DEVICE FROM CTI", 
                "ENABLE MOBILITY", "ENABLE MOBILE VOICE ACCESS", "PRIMARY USER DEVICE", "ENABLE EMCC",
                "NAME DIALING", "CONTROLLED DEVICE 1", "CONTROLLED DEVICE 2", 
                "CONTROLLED DEVICE 3", "CONTROLLED DEVICE 4"]

class CsvParser:

    location = ""
    filename = ""
    # readList =[]
    __readRows =[]
    def _init_(self):
        self.location = os.path.dirname(__file__)
        self.filename = os.path.join(self.location, 'source.csv')

    def __init__(self, loc, file):
        self.location = loc
        self.filename = os.path.join(loc, file)

    def readCsv(self, fileName):
        file = os.path.join(self.location, fileName)
        with open(file, mode ='r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                #print(', '.join(row))
                print(row)
                self.__readRows.append(row)
            # print("display row[1]: ")
            # print(self.__readRows[1])

    def createCsv(self):
        'create csv files'
        for fileName in csvFileName:
          with open(os.path.join(self.location, fileName+csvFileType[0]), mode ='w') as csvfile:
            writer = csv.writer(csvfile)
            title = []
            rowDetails = rowDetails1 = rowDetails2 = []
            user_id = manager_user_id = department = default_profile = user_locale = password =""
            pin = telephone_number = primary_extension = associated_pc = ipcc_extension ="" 
            mail_id = presence_group = subscribe_calling_search_space = digest_credentials ="" 
            remote_destination_limit = max_wait_time = allow_control_of_device = enable_mobility ="" 
            enable_mobile_voice = primary_user_device = enable_emcc = name_dialing = controlled_device1 ="" 
            controlled_device2 = controlled_device3 = controlled_device4 = ""

            mac_address=description=directory_number=owner_user_id=""
            if(fileName == "UserUpdate"):
                title = updateTitle
                # user_id = manager_user_id = department = default_profile = user_locale = password =""
                # pin = telephone_number = primary_extension = associated_pc = ipcc_extension ="" 
                # mail_id = presence_group = subscribe_calling_search_space = digest_credentials ="" 
                # remote_destination_limit = max_wait_time = allow_control_of_device = enable_mobility ="" 
                # enable_mobile_voice = primary_user_device = enable_emcc = name_dialing = controlled_device1 ="" 
                # controlled_device2 = controlled_device3 = controlled_device4 = ""

                rowDetails1 = [user_id, manager_user_id, department, default_profile, user_locale, password, pin,
                            telephone_number, primary_extension, associated_pc, ipcc_extension, mail_id, presence_group,
                            subscribe_calling_search_space, digest_credentials, remote_destination_limit, max_wait_time,
                            allow_control_of_device, enable_mobility, enable_mobile_voice, primary_user_device, enable_emcc,
                            name_dialing, controlled_device1, controlled_device2, controlled_device3, controlled_device4]
            else:
                title = commonTitle
                # mac_address=description=directory_number=owner_user_id=""
                rowDetails2 = [mac_address, description, directory_number, owner_user_id]

            writer.writerow(title)
            for row in self.__readRows[1:]:
                for i in range(10):
                    # writer.writerow(['quxie'+i,11, 48, 'jjf09 is mifeng'])
                   
                    mac_address = (fileName+row[0]).upper() if i == 0 else (fileName+row[0]+str(i)).upper()
                    description = mac_address
                    directory_number = row[1] + row[2] + str(i) + "0"
                    owner_user_id = row[0] if i==0 else row[0]+str(i)

                    user_id = owner_user_id
                    primary_extension = directory_number
                    allow_control_of_device = enable_mobility = enable_mobile_voice = "t"
                    user = row[0].upper() if i==0 else (row[0]+str(i)).upper()
                    controlled_device1 = csvFileName[0] + user
                    controlled_device2 = csvFileName[1] + user
                    controlled_device3 = csvFileName[3] + user
                    controlled_device4 = csvFileName[2] + user
                    rowDetails1 = [user_id, manager_user_id, department, default_profile, user_locale, password, pin,
                                                telephone_number, primary_extension, associated_pc, ipcc_extension, mail_id, presence_group,
                                                subscribe_calling_search_space, digest_credentials, remote_destination_limit, max_wait_time,
                                                allow_control_of_device, enable_mobility, enable_mobile_voice, primary_user_device, enable_emcc,
                                                name_dialing, controlled_device1, controlled_device2, controlled_device3, controlled_device4]
                    rowDetails2 = [mac_address, description, directory_number, owner_user_id]

                    rowDetails = rowDetails1 if fileName == "UserUpdate" else rowDetails2
                    # if(file)
                    # if(i==0):
                        

                    #     # writer.writerow([cell, cell, number, row[0]])
                    #     writer.writerow(rowDetails）
                        
                    # else:
                    #     cell = (fileName+row[0]+str(i)).upper()
                    #     writer.writerow([cell, cell, number, row[0]+str(i)])
                    writer.writerow(rowDetails)

    def writeCsv(self, fileName):
        with open(os.path.join(self.location, fileName), mode ='wb') as csvfile2:
            writer1 = csv.writer(csvfile2)
            writer1.writerow(['quxie1',11, 48, 'jjf09 is mifeng'])
            
        print("write a csvfile successfully")

    if __name__ == "_main_":
        pass

location = os.path.dirname(__file__)
# sourceFile = 'source.csv'
sourceFile = sys.argv[1]

filename = os.path.join(location, sourceFile)
csvParser = CsvParser(location, filename)
# csvParser2 = CsvParser()
print("read a csvfile: ")
csvParser.readCsv('source.csv')
# print("write a csvfile: ")
# csvParser.writeCsv("output3.csv")

# print("read a csvfile after write: ")
# csvParser.readCsv('output3.csv')

print("create  csvfiles: ")
csvParser.createCsv() 
