import sqlite3

DB_FILE = "students.db"

def create_connection():
	conn =  sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	sql_create_table = """CREATE TABLE IF NOT EXISTS marksheet(id INTEGER PRIMARY KEY, stdclass text, fname text, lname text, eng varchar,
	nep varchar, maths varchar, social varchar, hp varchar, sci varchar, comp varchar, optm varchar)"""
	cur.execute(sql_create_table)
	conn.commit()
	conn.close()

def addDataRec(stdclass, fname, lname, eng, nep, maths, social, hp, sci, comp, optm):
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	data = (stdclass, fname, lname, eng, nep, maths, social, hp, sci, comp, optm)
	insert_query = """INSERT INTO marksheet (stdclass, fname, lname, eng, nep, maths, social, hp, sci, comp, optm) 
	VALUES(?,?,?,?,?,?,?,?,?,?,?)"""
	cur.execute(insert_query,data)

	conn.commit()
	conn.close()

def viewData():
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	select_query = """SELECT * FROM marksheet"""
	cur.execute(select_query)
	rows = cur.fetchall()
	conn.close()
	return rows

def deleteRec(id):
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	data = (id,)
	delete_query = """DELETE FROM marksheet WHERE id = ?"""

	cur.execute(delete_query,data)
	conn.commit()
	conn.close()

def updateData(id, stdclass = "", fname = "", lname = "", eng = "", nep = "", maths = "", social = "", hp = "", sci = "", 
	comp = "", optm = ""):
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	data = (stdclass, fname, lname, eng, nep, maths, social, hp, sci, comp, optm,id)
	update_query = """UPDATE marksheet SET stdclass = ?, fname = ?, lname = ?, eng = ?, nep = ?, maths = ?, social = ?,
	hp = ?, sci = ?, comp = ?, optm = ? WHERE id = ?"""

	cur.execute(update_query,data)
	conn.commit()
	conn.close()

def searchData(stdclass = "", fname = "", lname = "", eng = "", nep = "", maths = "", social = "", hp = "", sci = "", 
	comp = "", optm = ""):
	conn = sqlite3.connect(DB_FILE)
	cur = conn.cursor()
	data = (stdclass, fname, lname, eng, nep, maths, social, hp, sci, comp, optm)

	search_query = """SELECT * FROM marksheet WHERE stdclass = ? OR fname = ? OR lname = ? OR eng = ? OR nep = ? OR maths = ?
	OR social = ? OR hp = ? OR sci = ? OR comp = ? OR optm = ?"""

	cur.execute(search_query,data)
	rows = cur.fetchall()
	conn.close()
	return rows


create_connection()
