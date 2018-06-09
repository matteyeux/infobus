import sys
import os
import mysql.connector

from bs4 import BeautifulSoup as bs


# this function does an SQL request, then write data to PARCOURS2
def sql_request(db_con):
	curs = db_con.cursor()
	req = "SELECT lati, longi from parcours2"
	curs.execute(req)
	rows = curs.fetchall()
	i = 0

	file = open("PARCOURS2", "w")
	for row in rows:
		if i == 0:
			str2write = " new google.maps.LatLng({0}, {1})\n".format(row[0], row[1])	
		else: 
			str2write = ",new google.maps.LatLng({0}, {1})\n".format(row[0], row[1])
		
		print(str2write)
		file.write(str2write)
		i += 1
	file.close()

# merge parcours1, parcours2 and parcours3 to page
def merge_files(files_to_merge, out):
	for i in range(len(files_to_merge)):
		file_to_read = open(files_to_merge[i], "r")
		data = file_to_read.read()
		file_to_read.close()

		file_to_write = open(out, "a")
		file_to_write.write(data)
		file_to_write.close()

# format data from page to real HTML
def format_html(page):
	html = open(page).read()
	soup = bs(html, 'html.parser')

	prettyHTML = soup.prettify()
	print(prettyHTML)
	file = open("page.html", "w")
	file.write(prettyHTML)
	file.close()

if __name__ == '__main__':
	conn = mysql.connector.connect(host="localhost", user="root", password="root", database="ratp")
	sql_request(conn)
	try :
		os.remove("page.html")
	except:
		pass
	files = ["PARCOURS1", "PARCOURS2", "PARCOURS3"]
	merge_files(files, "page")
	conn.close()

	format_html("page")
	os.remove("page")