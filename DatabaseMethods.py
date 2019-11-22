import pymysql
import time


def ConnectToDB():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='passwd17',
        port=3306,
        db='NFL',
        local_infile=1
    )


def getTable(fname):
    temp = fname.split('/')
    temp1 = temp[-1]
    temp = temp1.split('.')
    print(temp[0])
    return temp[0]


def LoadDataInsert(filename):
    try:
        table = getTable(filename)
        if "players" in table.lower():
            table = "players"
        table = table.lower()
        connection = ConnectToDB()
        cursor = connection.cursor()
        starttime = time.time()
        sql = "LOAD DATA local INFILE '" + filename + "' INTO TABLE NFL." + table + " fields terminated BY ',' lines " \
                                                                                    "terminated BY '\n';"
        cursor.execute(sql)
        cursor.close()
        connection.commit()
        endtime = time.time()
        print(f"Load data insertion runtime: {endtime - starttime}")
    except Exception as e:
        return str(e)
    finally:
        connection.close()
    return 'Success'


def MultiRowInsert(filename):
    try:
        table = getTable(filename)
        if "players" in table.lower():
            table = "players"
        table = table.lower()
        connection = ConnectToDB()
        cursor = connection.cursor()
        f = open(filename, "r")
        starttime = time.time()
        tuples = []
        start = 'INSERT INTO ' + table + ' VALUES '
        for x, line in enumerate(f):
            line = line.strip("\n")
            data = line.split(",")
            for i in range(len(data)):
                if i == 0:
                    if x == 0:
                        tuples.append(start + "('" + data[i] + "'")
                    else:
                        sql = "('" + data[i] + "'"
                        tuples.append(sql)
                elif i == len(data) - 1:
                    sql = "'" + data[i] + "')"
                    tuples.append(sql)
                else:
                    sql = "'" + data[i] + "'"
                    tuples.append(sql)
        cursor.execute(','.join(tuples) + ';')
        f.close()
        cursor.close()
        connection.commit()
        endtime = time.time()
        print(f"Multi-row insertion runtime: {endtime - starttime}")
    except Exception as e:
        return str(e)
    finally:
        connection.close()

    return 'Success'


def SingleInsert(filename):
    try:
        table = getTable(filename)
        if "players" in table.lower():
            table = "players"
        table = table.lower()
        connection = ConnectToDB()
        cursor = connection.cursor()
        f = open(filename, "r")
        starttime = time.time()
        for line in f:
            line = line.strip("\n")
            data = line.split(",")
            sql = "INSERT INTO " + table + " VALUES ("
            for i in range(len(data)):
                if i == 0:
                    sql = sql + "'" + data[i] + "'"
                else:
                    sql = sql + ",'" + data[i] + "'"
            sql = sql + ");"
            cursor.execute(sql)
        f.close()
        cursor.close()
        connection.commit()
        endtime = time.time()
        print(f"Single insertion runtime: {endtime - starttime}")
    except Exception as e:
        return str(e)
    finally:
        connection.close()

    return 'Success'


def delete(tableName):
    try:
        connection = ConnectToDB()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM " + tableName + ";")
        cursor.close()
        connection.commit()
    except Exception as e:
        return str(e)
    finally:
        connection.close()

    return 'Success'


def retrieve(tableName):
    output = []
    try:
        connection = ConnectToDB()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM " + tableName + ";")
        rows = cursor.fetchall()
        desc = cursor.description
        if tableName.lower() == "players":
            output.append(("{0:>8} {1:>10} {2:>15} {3:>8} {4:>12} {5:>12} {6:>12} {7:>10}".format(desc[0][0], desc[1][0],
                                                                                            desc[2][0], desc[3][0],
                                                                                            desc[4][0], desc[5][0],
                                                                                            desc[6][0],
                                                                                            desc[7][0])))
            for row in rows:
                output.append((
                    "{0:>8} {1:>10} {2:>15} {3:>8} {4:>12} {5:>12} {6:>12} {7:>10}".format(row[0], row[1], row[2],
                                                                                            str(row[3]), row[4], row[5],
                                                                                            row[6], row[7])))
        elif (tableName.lower() == "games"):
            output.append(("{0:>8} {1:>10} {2:>20} {3:>10} {4:>15} {5:>15}".format(desc[0][0], desc[1][0], desc[2][0],
                                                                                desc[3][0], desc[4][0],
                                                                                desc[5][0])))
            for row in rows:
                output.append((
                    "{0:>8} {1:>10} {2:>20} {3:>10} {4:>15} {5:>15}".format(row[0], str(row[1]), row[2], row[3], row[4],
                                                                            row[5])))
        elif (tableName.lower() == "teams"):
            output.append(("{0:>8} {1:>12} {2:>15}".format(desc[0][0], desc[1][0], desc[2][0])))
            for row in rows:
                output.append(("{0:>8} {1:>12} {2:>15} ".format(row[0], row[1], row[2])))
        elif (tableName.lower() == "play"):
            output.append(("{0:>8} {1:>10}".format(desc[0][0], desc[1][0])))
            for row in rows:
                output.append(("{0:>8} {1:>10}".format(row[0], row[1])))
        cursor.close()
        connection.commit()
    except Exception as e:
        return str(e)
    finally:
        connection.close()
    return "\n".join(output)


def average(tableName, columnName):
    try:
        connection = ConnectToDB()
        cursor = connection.cursor()
        cursor.execute("SELECT AVG(" + columnName + ") FROM " + tableName + ";")
        value = cursor.fetchall()
        cursor.close()
        connection.commit()
    except Exception as e:
        return str(e)
    finally:
        connection.close()

    return value
