import os
import sys


class AppException(Exception):
    """
    Organization: iNeuron Intelligence Pvt. Ltd.
    AppException is customized exception class designed to capture refined details about exception
    such as python script file line number along with error message 
    with custom exception one can easily spot the error and debug the code.
     
    """

    def __init__(self, error_message: Exception, error_detail: sys):
        """
        :param error_message: error message in string format
        """

        super().__init__(error_message)
        self.error_message = AppException.get_detailed_error_message(error_message=error_message,error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detail: sys):
        """
        erroe : Exception object raise from module
        error_detail : object of sys module
        """

        _,_, exc_tb = error_detail.exc_info()
        #extracting file name from the exception traceback 
        file_name = exc_tb.tb_frame.f_code.co_filename

        #preparing error message with file name and line number where exception has occured
        detailed_error_message = f"Error occured in script: [{file_name}] at line number: [{exc_tb.tb_lineno}] error message: [{error_message}]"

        return detailed_error_message
    
    def __repr__(self):
        """
        Formatting object of AppExecution
        """
        return AppException.__name__.str()
    
    def __str__(self):
        """
        Formatting how a object should visible if used in print statement or logging module
        """
        return self.error_message
                                                                            