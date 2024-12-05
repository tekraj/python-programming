from db.database import Database


db = Database('localhost','student','xyz344324wW','students',3307)

# user 
def create_student_table():
    create_table_query = """CREATE TABLE IF NOT EXISTS `users` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `email` varchar(255) COLLATE utf8_bin NOT NULL,
        `password` varchar(255) COLLATE utf8_bin NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
    AUTO_INCREMENT=1"""
    db.execute_query(create_table_query)

def insert_users(email,password):
    create_user_query = f"INSERT INTO `users` (`email`, `password`) VALUES ('{email}','{password}' )"
    return db.execute_query(create_user_query)

def get_users():
    select_query = f"SELECT * from users order by id desc"
    return db.execute_query(select_query)
