from rethinkdb import RethinkDB

# initialize rethinkdb driver
rethink = RethinkDB()

# connect to server
connection = rethink.connect('localhost', 28015)

# allows calling .run() on queries without specifying a connection.
connection.repl()

# create database 'library'
#rethink.db_create('library').run()

# drop database 'test' - it's automatically created by rethinkdb
#rethink.db_drop('test').run()

"""
# ok, now we create some tables
rethink.db('library').table_create('books').run()
rethink.db('library').table_create('authors').run()
rethink.db('library').table_create('users').run()
rethink.db('library').table_create('address').run()
rethink.db('library').table_create('rental').run()
rethink.db('library').table_create('movies').run()
rethink.db('library').table_create('directors').run()

# we created to many tables, so we need to delete some
rethink.db('library').table_drop('movies').run()
rethink.db('library').table_drop('directors').run()

# we are going to add 1 address
rethink.db('library').table('address').insert({
  'city': 'Warszawa',
  'postal_code': '00-002',
  'street': 'Leśna',
  'house_number': '18',
  'flat_number': '',
	}
).run()
"""
# and now, many address with the same insert
rethink.db('library').table('address').insert([
    {'city': 'Warszawa', 'postal_code': '00-002', 'street': 'Rolna', 'hause_number': '24A', 'flat_number': '15'},
    {'city': 'Warszawa', 'postal_code': '00-002', 'street': 'Anczyca Władysława Ludwika', 'hause_number': '5', 'flat_number': ''},
    {'city': 'Warszawa', 'postal_code': '00-002', 'street': 'Antonia Corazziego', 'hause_number': '2B', 'flat_number': '1'},
    {'city': 'Warszawa', 'postal_code': '00-002', 'street': 'Wały Jagiellońskie', 'hause_number': '1', 'flat_number': ''},
    {'city': 'Warszawa', 'postal_code': '00-002', 'street': 'Kombatantów', 'hause_number': '4', 'flat_number': '24'},
    {'city': 'Warszawa', 'postal_code': '00-002', 'street': 'Grenadierów', 'hause_number': '2', 'flat_number': ''},
    {'city': 'Warszawa', 'postal_code': '00-002', 'street': 'Lanckorońska', 'hause_number': '3', 'flat_number': '7'},
    {'city': 'Warszawa', 'postal_code': '00-002', 'street': 'Przestrzenna', 'hause_number': '5B', 'flat_number': '7'},
]).run()


















