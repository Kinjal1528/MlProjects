#exception.py — Defines custom exception classes for consistent error handling.
import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()# this will tell u in which line no. and in which particular file the exception has occured 
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in Python script name[{0}] line no. [{1}] error message[{2}]".format(
        #this is common it will not be changing again and again 
    file_name,exc_tb.tb_lineno,str(error)

    return error_message
    )
class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message