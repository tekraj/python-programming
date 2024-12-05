import math
import logging
from db.user import create_student_table, get_users, insert_users
from mathematics.trigonometry import cosine, sine


# Configure logging (log to console by default)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# different log levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


sin_45 = sine(math.pi/4)
print(sin_45)

cos_45 = cosine(math.pi/4)

try:
    100 / 0  
except ZeroDivisionError as e:  
    logging.error(f"Error: {e}")


# create user table
create_student_table()
# insert user
insert_users('tekrajpant@gmail.com','test@123')

users = get_users()
print(users)