import mysql.connector
#method1: save student information in database
def save_student_details(Roll_No, Name, Class, DOB, Physics_Marks, Maths_Marks, Chemistry_Marks, Computer_Marks, Total, Average, Percentage):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='studentDB',
                                            user='root',
                                            password='admin')

        mySql_insert_query = "INSERT INTO student (Roll_No, Name, Class, DOB, Physics_Marks, Maths_Marks, Chemistry_Marks, Computer_Marks, Total, Average, Percentage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = ( Roll_No, Name, Class, DOB, Physics_Marks, Maths_Marks, Chemistry_Marks, Computer_Marks, Total, Average, Percentage )
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, data)
        connection.commit()
        print("Record inserted successfully into Student table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into student table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

#method2: getting student details 
def get_student_details(Roll_No):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='studentDB',
                                            user='root',
                                            password='admin')

        sql_select_Query = "select Total, Average, Percentage from student where Roll_No={0}".format(Roll_No)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        if(cursor.rowcount==0):
            print('No Data Found')
        else:
            for row in records:
                print("Roll_No = ", Roll_No, )
                print("Total = ", row[0])
                print("Average  = ", row[1])
                print("Percentage  = ", row[2], "\n")

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

#method3: getting students rank list            
def get_student_rank_list():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='studentDB',
                                            user='root',
                                            password='admin')

        sql_select_Query = "select Roll_No, Total, Percentage, Name from student ORDER BY Percentage DESC"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        rank = 0
        print("Total number of rows in table: ", cursor.rowcount)

        if(cursor.rowcount==0):
            print('No Data Found')
        else:
            heading=["Rank"," Roll_No", "Total", "Percentage  ", "   Name"]
            for i in heading:
                print(i, end="  ")
            print("\n------------------------------------------------------")
            for row in records:
                rank = rank + 1
                print(rank, end="\t")
                print(row[0], end="\t")
                print(row[1], end="\t")
                print(row[2], end="\t\t")
                print(row[3], end="\n")
                

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
