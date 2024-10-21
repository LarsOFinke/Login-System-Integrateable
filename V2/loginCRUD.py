import os, sqlite3

connection_String:str = os.path.abspath(__file__)   # Find the absolute location of the program-file
connection_String = connection_String[:-7]  # Remove the last 2 characters (py-extension)
connection_String = f"{connection_String}DB.db"  # Add the db-extension

def create_database(connection_String: str):   # Create the Login-DB
    con = sqlite3.connect(connection_String)    # Establish a SQLite3-connection
    cursor = con.cursor()   # Assign the SQLite3-cursor
    with con:
        sql: str =  "CREATE TABLE tblLogins(" \
                    "LoginID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                    "LoginUsername TEXT NOT NULL UNIQUE, " \
                    "LoginPassword TEXT NOT NULL, " \
                    "LoginType TEXT NOT NULL, " \
                    "LoginHashkey INTEGER)"
        cursor.execute(sql) # Create the Logins-Table
            
        sql: str = "INSERT INTO tblLogins(LoginUsername, LoginPassword, LoginType) VALUES ('admin', 'admin', 'admin')"
        cursor.execute(sql) # Create the Standard Admin
            
        con.commit()    # Commit the database-creation


def create_account(username: str, password: str): # Create a new Account in the database
    con = sqlite3.connect(connection_String)    # Establish a SQLite3-connection
    cursor = con.cursor()   # Assign the SQLite3-cursor
    with con: 
        sql: str = "INSERT INTO tblLogins(LoginUsername, LoginPassword, LoginType) VALUES (?,?, 'user')"
        cursor.execute(sql, (username, password))   # Insert new User-details into the database
            
        con.commit()


def compare_login(name: str, password: str) -> bool:  # Compare user input with database
    con = sqlite3.connect(connection_String)    # Establish a SQLite3-connection
    cursor = con.cursor()   # Assign the SQLite3-cursor
    with con:
        sql: str = "SELECT * FROM tblLogins WHERE LoginUsername = ?"
        cursor.execute(sql, (name,))
        
        for passw in cursor:    # Iterate over the SQL-result
            if password == passw[2]:    # Compare the input with the database-entry
                user_id = int(passw[0])
                return True, user_id # Match found
        return False, 0 # No match found


def check_database_exists() -> bool:    # Check for / create Login-database
    if not os.path.exists(connection_String):
        create_database(connection_String)
    return True