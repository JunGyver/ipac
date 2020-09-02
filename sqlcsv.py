import pymysql
import sys
import csv

db_opts = {
    'user' : 'root',
    'password' : '',
    'host': 'localhost',
    'database' : 'ipac'
}

db = pymysql.connect(**db_opts)
cur = db.cursor()

sql = 'SELECT * from st_master'
csv_file_path = 'patent.csv'

try:
    cur.execute(sql)
    rows = cur.fetchall()
finally:
    db.close()

# Continue only if there are rows returned.
if rows:
    # New empty list called 'result'. This will be written to a file.
    result = list()

    # The row name is the first entry for each entity in the description Tuple.
    column_names = list()
    for i in cur.description:
        column_names.append(i[0])

    result.append(column_names)
    for row in rows:
        result.append(row)

    # Write result to file.
    with open(csv_file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in result:
            csvwriter.writerow(row)
else:
    sys.exit("No rows found for query: {}".format(sql))
