import pymysql

class Results:

    db = None
    def __init__(self):
        try:
            self.db = pymysql.connect("remotemysql.com", "GSaXLUNgo4", "GSaXLUNgo4", "D4eS0fGmMk", 3306)
            print("db connected")
        except:
            print("Failed in DB connection")
            self.db.close()

    def getResult(self,phone_num):
        try:
            cursor = self.db.cursor()
            query = "select * from student_result where contactno = \'" + phone_num + "\'"
            print(query)
            cursor.execute(query)
            record = cursor.fetchone()
            print(record)
            cursor.close()
            total = record[3]+record[4]+record[5]+record[6]+record[7]
            marks = 'Name:'+str(record[0])+' Rollno:'+str(record[1])+' DS:'+str(record[3])+' CS:'+str(record[4])+\
                        ' DBMS:'+str(record[5])+' JAVA:'+str(record[6])+' OS:'+str(record[7])+' Total:'+str(total)
            #  marks = get result from executing query
            if marks is not None:
                return marks
            else:
                return 'not found'
        except Exception as ex:
            print(ex)
            print("Failed to read data from table")
            self.db.close()

if __name__ == "__main__":
    result = Results()
    print(result.getResult('09877177020'))