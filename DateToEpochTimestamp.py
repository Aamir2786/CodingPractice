"""
@author: aamir
"""
from datetime import datetime, timezone
import re

def util_func(date_string, date_format):
    my_Date = datetime.strptime(date_string, date_format)     # Return a datetime corresponding to date_string, parsed according to date_format. (string parse time)
    my_Date = my_Date.replace(tzinfo = timezone.utc)        # Change the timezone from None to UTC (Universal Time Coordinated)
    print("Output: {}".format(int(my_Date.timestamp())))        #Get timestamp from a datetime object


def date_to_epoch_timestamp(input_date):        # Check the format of input_date and convert into epoch time according
    if re.match("^\d{2}/\d{2}/\d{4}$", input_date) and int(input_date[3:5]) < 13:
        util_func(input_date, "%d/%m/%Y")

    elif re.match("^\d{2}/\d{2}/\d{4}$", input_date):
        util_func(input_date, "%m/%d/%Y")
        
    elif re.match("^\d{2}-\d{2}-\d{4}$", input_date) and int(input_date[3:5]) < 13:
        util_func(input_date, "%d-%m-%Y")
    
    elif re.match("^\d{2}-\d{2}-\d{4}$", input_date):
        util_func(input_date, "%m-%d-%Y")

    elif re.match("^\d{2}\.\d{2}\.\d{4}$", input_date)  and int(input_date[3:5]) < 13:
        util_func(input_date, "%d.%m.%Y")
        
    elif re.match("^\d{2}\.\d{2}\.\d{4}$", input_date):
        util_func(input_date, "%m.%d.%Y")
    
    elif re.match("^\d{8}$", input_date) and int(input_date[2:4]) < 13:
        util_func(input_date, "%d%m%Y")

    elif re.match("^\d{8}$", input_date):
        util_func(input_date, "%m%d%Y")
    else:
        print("Unable to convert the provided date")
       
if __name__ == "__main__":
    input_date = input()
    print("Input: {}".format(input_date))
    date_to_epoch_timestamp(input_date)