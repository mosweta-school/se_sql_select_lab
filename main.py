# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

c = conn.cursor()



# STEP 2
# Replace None with your code
df_first_five= pd.read_sql("SELECT employeeNumber, lastName FROM employees ",conn)
# print(df_first_five)


# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("SELECT  lastName, employeeNumber FROM employees ",conn)
# print(df_five_reverse)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("SELECT  lastName, employeeNumber as ID FROM employees ",conn)
# print(df_alias)

# STEP 5
# Replace None with your code
df_executive =  pd.read_sql("""SELECT  
                            jobTitle, 
                                CASE
                            WHEN jobTitle IN ( "President","VP Sales","VP Marketing")
                            THEN "Executive"
                            ELSE "Not Executive"
                            END AS "role"
                            FROM employees """,conn)

# print(df_executive)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""SELECT  
                            lastName, 
                                LENGTH(lastName) AS "name_length"
                            FROM employees """,conn)

# STEP 7

# Replace None with your code
df_short_title = pd.read_sql("""SELECT  
                            jobTitle,
                                SUBSTR(jobTitle,1,2) AS "short_title"
                            FROM employees """,conn)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderdetails
""", conn).sum().values
# print(sum_total_price)

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""SELECT 
    orderDate,
    strftime('%d', orderDate) AS day,   -- 01-31
    strftime('%m', orderDate) AS month, -- 01-12
    strftime('%Y', orderDate) AS year   -- 4-digit year
FROM orders; """, conn)

conn.commit()
conn.close()

