import pymysql
import time


def LoadDataInsert(filename):
    try:
        temp = filename.split("/")
        temp1 = temp[-1]
        temp = temp1.split(".")
        table = temp[0]
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='passwd17',
            port=3306,
            db='NFL',
            local_infile=1
        )
        cursor = connection.cursor()
        starttime = time.time()
        sql = "LOAD DATA local INFILE '" + filename + "' INTO TABLE NFL." + table + "fields terminated BY ',' lines " \
                                                                                    "terminated BY '\n'; "
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
        temp = filename.split("/")
        temp1 = temp[-1]
        temp = temp1.split(".")
        table = temp[0]
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='passwd17',
            port=3306,
            db='NFL',
            local_infile=1
        )
        cursor = connection.cursor()
        f = open(filename, "r")
        starttime = time.time()
        sql = "INSERT INTO " + table + " VALUES "
        for line in f:
            line = line.strip("\n")
            data = line.split(",")
            for i in range(len(data)):
                if i == 0:
                    sql = sql + "('" + data[i] + "'"
                    print(sql)
                elif i == len(data) - 1:
                    sql = sql + ",'" + data[i] + "'),"
                else:
                    sql = sql + ",'" + data[i] + "'"
        sql = sql[:-1]
        sql = sql + ";"
        cursor.execute(sql)
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
        temp = filename.split("/")
        temp1 = temp[-1]
        temp = temp1.split(".")
        table = temp[0]
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='passwd17',
            port=3306,
            db='NFL',
            local_infile=1
        )
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
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='passwd17',
            port=3306,
            db='NFL',
            local_infile=1
        )
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
    output = ""
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='passwd17',
            port=3306,
            db='NFL',
            local_infile=1
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM " + tableName + ";")
        rows = cursor.fetchall()
        desc = cursor.description
        if tableName.lower() == "players":
            output = ("{0:>0} {1:>10} {2:>12} {3:>8} {4:>12} {5:>12} {6:>12} {7:>10}".format(desc[0][0], desc[1][0],
                                                                                             desc[2][0], desc[3][0],
                                                                                             desc[4][0], desc[5][0],
                                                                                             desc[6][0],
                                                                                             desc[7][0])) + "\n"
            for row in rows:
                output = output + (
                    "{0:>0} {1:>10} {2:>15} {3:>8} {4:>12} {5:>12} {6:>12} {7:>10}".format(row[0], row[1], row[2],
                                                                                           str(row[3]), row[4], row[5],
                                                                                           row[6], row[7])) + "\n"
        elif (tableName.lower() == "games"):
            output = ("{0:>0} {1:>10} {2:>35} {3:>10} {4:>15} {5:>15}".format(desc[0][0], desc[1][0], desc[2][0],
                                                                              desc[3][0], desc[4][0],
                                                                              desc[5][0])) + "\n"
            for row in rows:
                output = output + (
                    "{0:>0} {1:} {2:>35} {3:>10} {4:>15} {5:>15}".format(row[0], row[1], row[2], row[3], row[4],
                                                                         row[5])) + "\n"
        elif (tableName.lower() == "teams"):
            output = ("{0:>0} {1:>12} {2:>15}".format(desc[0][0], desc[1][0], desc[2][0])) + "\n"
            for row in rows:
                output = output + ("{0:>0} {1:>15} {2:>15} ".format(row[0], row[1], row[2])) + "\n"
        elif (tableName.lower() == "play"):
            output = ("{0:>0} {1:>7}".format(desc[0][0], desc[1][0])) + "\n"
            for row in rows:
                output = output + ("{0:>0} {1:>10}".format(row[0], row[1])) + "\n"
        cursor.close()
        connection.commit()
    except Exception as e:
        return str(e)
    finally:
        connection.close()
    return output


def average(tableName, columnName):
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='passwd17',
            port=3306,
            db='NFL',
            local_infile=1
        )
        command = "SELECT AVG(" + columnName + ") FROM " + tableName + ";"
        print(command)
        cursor = connection.cursor()
        cursor.execute(command)
        value = cursor.fetchall()
        cursor.close()
        connection.commit()
    except Exception as e:
        return str(e)
    finally:
        connection.close()

    return value
