# import logging

# logging.basicConfig(filename="log.txt",level=logging.WARNING )  #-----> This will create a log.txt in current working directory and only higher level msg are stored in log.txt

# print("Logging Demo....!")                       # If not mentioned level then by default level is WARNING level
#                                                    # If level = warning then warning and higher level data is stored 
#                                                    # therefore if want denug level = logging.DEBUG can be used as similar for others 

# logging.debug("DEBUG MESSAGE....")
# logging.info("INFO MESSAGE....")
# logging.critical("CRITICAL MESSAGE....")            # only criticsl , warning , error --> this are higher level msg are stored in log.txt because we mentioned level=logging.WARNING
# logging.warning("WARNING MESSAGE....")
# logging.error("ERROR MESSAGE....")






#How to write python program exceptions to the log file 

import logging

logging.basicConfig(filename="Try_except_log.txt", level=logging.INFO)
logging.info("The new request arrives..")



try:
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print(x/y)
except ZeroDivisionError as msg:
    print("Cannot divide by zero")
    logging.exception(msg)

except ValueError as msg:
    print("Only int values is applicable..")
    logging.exception(msg)

logging.info("Execution completed..")