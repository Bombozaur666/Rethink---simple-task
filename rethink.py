from rethinkdb import RethinkDB

# initialize rethinkdb driver
rethink = RethinkDB()

# connect to server
connection = rethink.connect('localhost', 28015).repl()

rethink.db_create('library').run(connection)

