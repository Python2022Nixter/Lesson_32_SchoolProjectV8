import datetime
import os
import pathlib
import sqlite3
import time
import classes.school_constants as c

class Person():  
    
    def __init__(self, person_data: tuple[str]) -> None:  #  Person(res[0])
        # 
        self.person_id = int(person_data[0])
        self.first_name = person_data[1]
        self.last_name = person_data[2]
        self.email = person_data[3]
        self.address = person_data[4]
        self.tel = person_data[5]
        self.salary = float(person_data[6])
        self.login = person_data[7]
        self.password = person_data[8]
        self.position_id = int(person_data[9])
        self.course_id = int(person_data[10])
        pass
    
    def __str__(self) -> str:
        out_string = "Person: "
        out_string += F"id: {self.person_id} "
        out_string += F"name: {self.first_name} "
        out_string += F"last name: {self.last_name} "
        out_string += F"email: {self.email} "
        out_string += F"address: {self.address} "
        out_string += F"tel: {self.tel} "
        out_string += F"salary: {self.salary} "
        out_string += F"login: {self.login} "
        out_string += F"password: {self.password} "
        out_string += F"position id: {self.position_id} "
        out_string += F"course id: {self.course_id} "
        
        return out_string
    
    pass

class School:
    __default_admin = Person((0,"","","","","",0.0,"","",1,0))
    def __init__(self) -> None:
        os.system("\n")# set console to accept colors
        self.last_message = ""
        self.PATH_TO_FILE_DATABASE = pathlib.Path(__file__).parent.parent.joinpath(c.FOLDER_DATABASE).joinpath(c.FILE_DATABASE)
        self.PATH_TO_CSV_PERSONS = pathlib.Path(__file__).parent.parent.joinpath(c.FOLDER_CSV).joinpath(c.FILE_CSV_PERSONS)
        self.PATH_TO_CSV_COURSES = pathlib.Path(__file__).parent.parent.joinpath(c.FOLDER_CSV).joinpath(c.FILE_CSV_COURSES)
        self.PATH_TO_CSV_POSITIONS = pathlib.Path(__file__).parent.parent.joinpath(c.FOLDER_CSV).joinpath(c.FILE_CSV_POSITIONS)
        pass
    
    def start(self):
        self.__login()
        pass
    
    def __login(self):
        print (F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Login{c.RESET_COLOR}")
        
        # Check if PERSONS table exists
        # handle error: sqlite3.OperationalError: no such table: 
        try:
            # query database
            with sqlite3.connect(self.PATH_TO_FILE_DATABASE) as conn:
                cursor = conn.cursor() # Create cursor object to operate with DB
                # Check if table persond exists in DB
                res = cursor.execute(c.SQL_CHECK_TABLE_EXISTS, [c.TABLE_NAME_PERSONS])
                table_found = True if res.fetchone()[0] == 1 else False
                if table_found:
                    # Check if table has any administrators 
                    res = cursor.execute(c.SQL_CHECK_ADMINISTRATORS)
                    admins_found = True if res.fetchone()[0] == 1 else False
                    if admins_found:
                        while True: # BEGIN login loop
                            user_name = input("Enter login name: ")
                            user_password = input("Enter password: ")
                            pass
                            res = cursor.execute(c.SQL_GET_USER_BY_LOGIN, 
                                                (user_name, user_password)
                                                ).fetchall()  # Method chainig: 1. call a = cursor.execute(),  2 res =  a.fetchall()
                            print (F"Query result: \nresults: {res}\tlen: {len(res)}\n") # list of tuples" [(result row1), (result row2)]
                            print (len(res) != 0)
                            if len(res) != 0 :
                                self.__registered_user = Person(res[0]) # call class constructor: pass tuple with single user data to class constructor
                                print (111)
                                break
                            print ("Incorrect user credentials, try again")
                            pass # END login loop
                        pass
                    else: # No administrators found
                        self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_ERROR_MESSAGE_COLOR}No administrators found. Default admin created{c.RESET_COLOR}\n"
                        self.__registered_user = School.__default_admin
                        pass
                    pass
                else: # Table not found
                    self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_ERROR_MESSAGE_COLOR}Table {c.TABLE_NAME_PERSONS} not found. Default admin created{c.RESET_COLOR}\n"
                    self.__registered_user = School.__default_admin
                    pass
                pass # END SQL with 
        except sqlite3.Error as err:
            self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_ERROR_MESSAGE_COLOR}{err}{c.RESET_COLOR}\n"
            pass
        finally:
            self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Login process finished{c.RESET_COLOR}\ncurrent user: {self.__registered_user.first_name}\n"
            pass 
        
        print (F"\n{datetime.datetime.now()}\tWelcome, user:\n{self.__registered_user.__str__()}")
        self.__process_menu()
        pass
     
    def __process_menu(self):        
        # Display menu
        match self.__registered_user.position_id:
            case 2:
                # Teacher detected (self.__registered_user.position_id = 1)
                
                pass
            case 3:
                # Sales person detected (self.__registered_user.position_id = 2)
                
                pass
            case 4:
                # Student detected
                
                pass
            case 5:
                # educationManager detected
                
                pass
            case 1:
                # Administrator detected (self.__registered_user.position_id = 5)
                # create menu text string
                
                # START - creating menu string 
                menu_string = F"\n{datetime.datetime.now()}\n{c.SET_HEADER_COLOR} Administrator menu:{c.RESET_COLOR} \n"
                menu_string += F"{c.SET_HIGHLIGHT_TEXT_COLOR}{0:>4d}{c.RESET_COLOR} to EXIT\n"
                for i in range(len(c.MENU_ADMIN)):
                    menu_string += F"{c.SET_HIGHLIGHT_TEXT_COLOR}{i+1:>4d}{c.RESET_COLOR} to {c.MENU_ADMIN[i]}\n"
                    pass
                # END - creating menu string 
                
                while True:
                    time.sleep(3)
                    # os.system("cls")
                    print(F"\n{datetime.datetime.now()}\t{c.SET_ERROR_MESSAGE_COLOR}Console cleaned{c.RESET_COLOR}\n")
                    print(self.last_message)
                    self.last_message = ""
                    match input(menu_string):
                        case "0":
                            # EXIT
                            break
                        # Manage PERSONS
                        case "1":
                            # Create table: PERSONS
                            self.__create_table(c.SQL_CREATE_TABLE_PERSONS)
                            pass
                        case "2":
                            # Add record to table: PERSONS
                            self.__add_table_record(c.SQL_ADD_RECORD_PERSONS)
                            pass
                        case "3":
                            # Import table PERSONS from csv
                            self.__drop_table(c.SQL_DROP_TABLE_PERSONS)
                            self.__create_table(c.SQL_CREATE_TABLE_PERSONS)
                            self.__import_from_csv(path_to_csv = self.PATH_TO_CSV_PERSONS, sql = c.SQL_ADD_RECORD_PERSONS)
                            pass
                        case "4":
                            # Drop table: PERSONS
                            self.__drop_table(c.SQL_DROP_TABLE_PERSONS)
                            
                            pass
                        case "5":
                            # Update table record: PERSONS
                            self.__update_table(c.SQL_UPDATE_TABLE_PERSONS)
                            
                            pass
                        
                        # Manage POSITIONS table 
                        case "6":
                            # Create table: POSITIONS
                            self.__create_table(c.SQL_CREATE_TABLE_POSITIONS)
                            pass
                        case "7":
                            # Add record to table: POSITIONS
                            self.__add_table_record(c.SQL_ADD_RECORD_POSITIONS)
                            pass
                        case "8":
                            # Import table POSITIONS from csv
                            self.__drop_table(c.SQL_DROP_TABLE_POSITIONS)
                            self.__create_table(c.SQL_CREATE_TABLE_POSITIONS)
                            self.__import_from_csv(self.PATH_TO_CSV_POSITIONS, c.SQL_ADD_RECORD_POSITIONS)
                            pass
                        case "9":
                            # Drop table: POSITIONS
                            self.__drop_table(c.SQL_DROP_TABLE_POSITIONS)
                            
                            pass
                        
                        # Manage courses table 
                        case "10":
                            # Create table: COURSES
                            self.__create_table(c.SQL_CREATE_TABLE_COURSES)
                            pass
                        case "11":
                            # Add record to table: COURSES
                            self.__add_table_record(c.SQL_ADD_RECORD_COURSES)
                            pass
                        case "12":
                            self.__drop_table(c.SQL_DROP_TABLE_COURSES)
                            self.__create_table(c.SQL_CREATE_TABLE_COURSES)
                            # Import table COURSES from csv
                            self.__import_from_csv(self.PATH_TO_CSV_COURSES, c.SQL_ADD_RECORD_COURSES)
                            pass
                        case "13":
                            # Drop table: COURSES
                            self.__drop_table(c.SQL_DROP_TABLE_COURSES)
                            
                            pass
 
                        case _:
                            self.last_message = F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Incorrect input{c.RESET_COLOR}\n"

                            pass
                    
                    
                    
                pass
            
        # end match block

        
        
        pass
    
    def __import_from_csv (self, path_to_csv: str, sql: str) -> None:
        self.last_message = F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Import startsed, wait ...{c.RESET_COLOR}\n"
        # read from file
        with open(path_to_csv) as f: rows_from_file = list (filter(lambda x: x[0].isdigit(), f.readlines()))         

        values_list = []
        for n_row in rows_from_file: values_list.append(n_row.strip().split(",")[1:])         
        # populate DB table
        self.__execute_sql_query(sql, values_list)
        pass
    
    def __add_table_record(self, sql: str):
        #   CURRENTLY _ PERSONS ONLY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.last_message = F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Wait ...{c.RESET_COLOR}\n"
        values_list = [] # single record data list
        #CREATE INPUT MENU
        table_columns = c.get_fields_list(c.PERSONS_HEADERS )[1:]
        
        for i in range(len(table_columns)):
            if i == len(table_columns) - 2:
                # position id input
                ## Query DB -> get id, names
                try:
                    # query database
                    with sqlite3.connect(self.PATH_TO_FILE_DATABASE) as conn:
                        cursor = conn.cursor() # Create cursor object to operate with DB
                        self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Reading database started at{c.RESET_COLOR}\n"
                        res = cursor.execute(c.SQL_GET_POSITIONS).fetchall()
                        position_menu = F"{c.SET_HIGHLIGHT_TEXT_COLOR}{c.SET_HEADER_COLOR} Select position:{c.RESET_COLOR} \n"
                        id_list = []
                        for position_id, position_name in res:
                            id_list.append(position_id)
                            position_menu += F"{c.SET_HIGHLIGHT_TEXT_COLOR}{position_id:>2d}{c.RESET_COLOR} - {position_name}\n"                            
                            pass
                        position_menu += "\n"
                        pass # END SQL
                except sqlite3.Error as err:
                    self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_ERROR_MESSAGE_COLOR}{err}{c.RESET_COLOR}\n"
                    pass
                finally:
                    self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Reading database ended{c.RESET_COLOR}\n"
                    pass 
                while True:
                    entered_position_id = int(input(position_menu))
                    if entered_position_id in id_list : break
                    print (F"{c.SET_ERROR_MESSAGE_COLOR}Incorrect position id{c.RESET_COLOR}\n")
                    pass
                values_list.append (entered_position_id)                
                pass
            
            elif i == len(table_columns) - 1:
                # courses id input
                #
                try:
                    # query database
                    with sqlite3.connect(self.PATH_TO_FILE_DATABASE) as conn:
                        cursor = conn.cursor() # Create cursor object to operate with DB
                        self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Reading database started at{c.RESET_COLOR}\n"
                        res = cursor.execute(c.SQL_GET_COURSES).fetchall()
                        courses_menu = F"{c.SET_HIGHLIGHT_TEXT_COLOR}{c.SET_HEADER_COLOR} Select course:{c.RESET_COLOR} \n"
                        id_list = []
                        for course_id, course_name in res:
                            id_list.append(course_id)
                            courses_menu += F"{c.SET_HIGHLIGHT_TEXT_COLOR}{course_id:>2d}{c.RESET_COLOR} - {course_name}\n"                            
                            pass
                        courses_menu += "\n"
                        pass # END SQL
                except sqlite3.Error as err:
                    self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_ERROR_MESSAGE_COLOR}{err}{c.RESET_COLOR}\n"
                    pass
                finally:
                    self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Reading database record ended{c.RESET_COLOR}\n"
                    pass 
                while True:
                    entered_course_id = int(input(courses_menu))
                    if entered_course_id in id_list : break
                    print (F"{c.SET_ERROR_MESSAGE_COLOR}Incorrect course id{c.RESET_COLOR}\n")
                    pass
                values_list.append (entered_course_id)                
                pass

            elif i == len(table_columns) - 4:
                # login names input
                #
                # res = self.__execute_sql()
                try:
                    # query database
                    with sqlite3.connect(self.PATH_TO_FILE_DATABASE) as conn:
                        cursor = conn.cursor() # Create cursor object to operate with DB
                        self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Reading database started at{c.RESET_COLOR}\n"
                        res = cursor.execute(c.SQL_GET_LOGIN_NAMES).fetchall()
                        login_list = []
                        for next_person in res:
                            login_list.append(next_person[0])
                            pass
                        pass # END SQL
                except sqlite3.Error as err:
                    self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_ERROR_MESSAGE_COLOR}{err}{c.RESET_COLOR}\n"
                    pass
                finally:
                    self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Reading database record ended{c.RESET_COLOR}\n"
                    pass 
                
                while True:
                    entered_login = input("Select login name: ")
                    if entered_login not in login_list : break
                    print (F"{c.SET_ERROR_MESSAGE_COLOR}Selected login name in use already{c.RESET_COLOR}\n")
                    pass
                values_list.append (entered_login)                
                pass
            
            else:
                values_list.append (input(F"Enter {table_columns[i]}: "))         
            pass
        
        try:
            # query database
            with sqlite3.connect(self.PATH_TO_FILE_DATABASE) as conn:
                cursor = conn.cursor() # Create cursor object to operate with DB
                self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Adding record started at{c.RESET_COLOR}\n"
                
                cursor.execute(sql,values_list)
                pass # END SQL
        except sqlite3.Error as err:
            self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_ERROR_MESSAGE_COLOR}{err}{c.RESET_COLOR}\n"
            pass
        finally:
            self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Adding record ended{c.RESET_COLOR}\n"
            pass 
        
        
        pass
    
    def __create_table(self, sql: str) -> None: self.__execute_sql_query(sql)  # TO DO -> Remove method
    
    def __drop_table(self, sql: str) -> None: self.__execute_sql_query(sql)  # TO DO -> Remove method
    
    def __update_table(self, sql: str) -> None:
        # Prepare data
        ## menu - input search field name
        ## menu - input field name to change
        table_name = sql.split()[1].replace("\"", "")  # get table name from sql string
        
        match table_name:
            case c.TABLE_NAME_PERSONS: fields_list = c.get_fields_list(c.PERSONS_HEADERS)
            case c.TABLE_NAME_POSITIONS: fields_list = c.get_fields_list(c.POSITIONS_HEADERS)
            case c.TABLE_NAME_COURSES: fields_list = c.get_fields_list(c.COURSES_HEADERS)
            
        change_menu = F"{c.SET_HEADER_COLOR} Select field name to change data in:{c.RESET_COLOR}\n"
        filter_menu = F"{c.SET_HEADER_COLOR}Select filter field name:\n{c.RESET_COLOR}"
        for ind, next_item in enumerate(fields_list):
            filter_menu += F"\t{c.SET_HIGHLIGHT_TEXT_COLOR}{ind:3d}{c.RESET_COLOR} - {next_item}\n"
            if ind == 0: continue
            change_menu += F"\t{c.SET_HIGHLIGHT_TEXT_COLOR}{ind:3d}{c.RESET_COLOR} - {next_item}\n"
            pass
        change_menu += ": "
        filter_menu += ": "
        
        field_name_to_filter = fields_list[ int(input(filter_menu))]
        filter_value = input("Value for search filter: ")
        field_name_to_change = fields_list [int (input(change_menu))]
        data_value = input("New walue: ")
        
        params =[ [data_value,filter_value ]]  #
        #  UPDATE "persons" SET "FIELD_NAME_TO_CHANGE" = ? WHERE "filter_field_name" = ? 
        sql = sql.replace("__FIELD_NAME_TO_CHANGE__",field_name_to_change).replace("__FIELD_NAME_TO_FILTER__", field_name_to_filter)    
        
        # UPDATE "persons" SET "first_name" = ? WHERE "person_id" = ?
        
        # Execute query 
        self.__execute_sql_query(sql, query_parameters = params)  
        
        
        pass

    

    def __execute_sql_query(self, query_string: str, query_parameters: list | None = None) -> str | None:
        res = None
        self.last_message = F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Query database started{c.RESET_COLOR}\n"
        # common part
        try:
            # query database
            with sqlite3.connect(self.PATH_TO_FILE_DATABASE) as conn:
                cursor = conn.cursor() # Create cursor object to operate with DB
                match (query_string.split()[0], query_parameters): # structural pattern matching 
                    case ("SELECT", None):
                        self.last_message = F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Select started, wait ...{c.RESET_COLOR}\n"
                        res = cursor.execute(query_string).fetchall()
                        pass
                    case ("DROP", None):
                        self.last_message = F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Drop table started, wait ...{c.RESET_COLOR}\n"
                        if input("Sure?[y]: ") == 'y': cursor.execute(query_string)
                        pass
                    case ("CREATE", None):
                        self.last_message = F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Create table started, wait ...{c.RESET_COLOR}\n"
                        cursor.execute(query_string)
                        pass
                    case ("INSERT" | "UPDATE", *parameters):
                        self.last_message = F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}ISERT | UPDATE started, wait ...{c.RESET_COLOR}\n"
                        cursor.executemany(query_string, query_parameters)
                        pass
                    case _:print ("Undefiner query type")
                        
                pass # END SQL
        except sqlite3.Error as err:
            self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_ERROR_MESSAGE_COLOR}{err}{c.RESET_COLOR}\n"
            pass
        finally:
            self.last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Query database ended{c.RESET_COLOR}\n"
            pass 
        return res

    
    pass
