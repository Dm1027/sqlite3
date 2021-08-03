import sqlite3
from mortgage_class import Mortgage
from mortgage_class import objs

#create new DB in memory
connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

#create mortgage data table in memory
cursor.execute("""CREATE TABLE mortgage (
					house_id integer PRIMARY KEY AUTOINCREMENT,
 					house_num integer,
 					street text,
 					city text,
					state text,
 					zip integer
 					)""")

cursor.execute("""CREATE TABLE pricing (
					house_id integer,
 					sell_price integer,
					list_price integer,
					FOREIGN KEY(house_id) REFERENCES mortgage(house_id)			
 					)""")



#add objects to DB by looping through list of created objects
for i in range(len(objs)):
	cursor.execute("""INSERT INTO mortgage VALUES(NULL, :num, :street, :city, :state, :zip)""", 
				{'num': objs[i].houseNumber,
				'street': objs[i].streetName,
				'city': objs[i].city,
				'state': objs[i].state,
				'zip': objs[i].zip
				})
	cursor.execute("""INSERT INTO pricing VALUES(LAST_INSERT_ROWID(),:list_price, :sell_price)""", 
				{
				'sell_price': objs[i].sellPrice,
				'list_price': objs[i].listPrice
				})



#query data from DB for all homes in zip 14214
print("Homes in 14214")
cursor.execute("""SELECT mortgage.house_id,
						house_num,
						street,
						city,
						state,
						zip,
						list_price,
						sell_price
						FROM mortgage
						JOIN pricing
						ON mortgage.house_id=pricing.house_id
						WHERE zip = 14214""")
queryResult = cursor.fetchall()
for each in queryResult:
	print(each)




#query data from DB for all homes listed above 200k
print("\nAll homes listed for > $200,000")
cursor.execute("""SELECT mortgage.house_id,
						house_num,
						street,
						city,
						state,
						zip,
						list_price
						FROM mortgage
						JOIN pricing
						ON mortgage.house_id=pricing.house_id
						WHERE list_price > 200000""")
queryResult = cursor.fetchall()
for each in queryResult:
	print(each)


#query data from DB for all homes which sold for less than asking
print("\n All homes selling for less than asking")
cursor.execute("""SELECT mortgage.house_id,
						house_num,
						street,
						city,
						state,
						zip,
						list_price,
						sell_price
						FROM mortgage
						JOIN pricing
						ON mortgage.house_id=pricing.house_id
						WHERE list_price > sell_price""")
queryResult = cursor.fetchall()
for each in queryResult:
	print(each)

#query for average list price in 14222
print("\n Average list price in 14222")
cursor.execute("""SELECT ROUND(AVG(list_price), 2)
						FROM mortgage
						JOIN pricing
						ON mortgage.house_id=pricing.house_id
						WHERE zip = 14222""")
queryResult = cursor.fetchall()
for each in queryResult:
	print(each)

#query for average list price in 14214
print("\n Average list price in 14214")
cursor.execute("""SELECT ROUND(AVG(list_price), 2)
						FROM mortgage
						JOIN pricing
						ON mortgage.house_id=pricing.house_id
						WHERE zip = 14214""")
queryResult = cursor.fetchall()
for each in queryResult:
	print(each)





#commit data to DB
connection.commit()

#close DB connection
connection.close()