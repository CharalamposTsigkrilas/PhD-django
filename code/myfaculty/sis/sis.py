import pymssql
from django.conf import settings

STUD_IP = settings.STUD_IP
STUD_USER = settings.STUD_USER
STUD_PASSWORD = settings.STUD_PASSWORD
STUD_DATABASE = settings.STUD_DATABASE

class estudiesdb:

    def __init__(self,
                 server = STUD_IP,
                 user = STUD_USER,
                 password = STUD_PASSWORD,
                 database = STUD_DATABASE):

        self.server = server
        self.password = password
        self.database = database
        self.user = user
        self.conn = pymssql.connect(server=STUD_IP,
                                    user=STUD_USER,
                                    password=STUD_PASSWORD,
                                    database=STUD_DATABASE,
                                    as_dict=True)
        

    def query(self, sqlQuery):
        cursor = self.conn.cursor()
        cursor.execute( sqlQuery )
        return cursor

    def get_personal_data(self, username):
        sql_query = """
        SELECT * FROM UriPersonalData
        WHERE (UriPersonalData.UserName = '{0}')
        """.format(username)
        cursor = self.query( sql_query )
        return cursor.fetchone()
    
    def get_student_data(self, username):
        sql_query = """
        SELECT * FROM UriPersonalData, UniStuStudent
        WHERE (UriPersonalData.UserName = '{0}') AND (UriPersonalData.uriId = UniStuStudent.uriId)
        """.format(username)
        cursor = self.query( sql_query )
        return cursor.fetchone()
    
    def filter_students(self, partial_name):
        if len(partial_name) >=3:
            sql_query = """
            SELECT TOP 10 UriPersonalData.SurName, UriPersonalData.FirstName, UniStuStudent.Mhtrwo, UniStuStudent.TrexonEksamFoit, UriPersonalData.UserName
            FROM UriPersonalData, UniStuStudent, UniCoDeptProgram
            WHERE ( ( UriPersonalData.SurName LIKE N'%{0}%') OR ( UniStuStudent.Mhtrwo LIKE '%{0}%') )
            AND ( UriPersonalData.uriId = UniStuStudent.uriId )
            AND ( UniStuStudent.DeptPrg = UniCoDeptProgram.hid ) 
            AND ( (UniCoDeptProgram.Dept = 550) OR (UniCoDeptProgram.Dept = 1550) )
            AND ( (UniStuStudent.KatFoithshs = 'active') OR (UniStuStudent.KatFoithshs = 'peranKanon') OR (UniStuStudent.KatFoithshs = 'epiPtyxio') )
            """.format(partial_name.upper())
            cursor = self.query( sql_query )
            return cursor.fetchall()   
        
    def __del__(self):
        self.conn.close()
    
