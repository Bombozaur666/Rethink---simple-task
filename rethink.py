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

rethink.db('library').table('authors').insert([
  {'name': 'William', 'last_name': 'Shakespeare', 'country': 'England', 'year_of_birth': '1564', 'year_of_death': '1616', },
  {'name': 'Andrzej', 'last_name': 'Sapkowski', 'country': 'Poland', 'year_of_birth': '1948', 'year_of_death': '', },
  {'name': 'Jacek', 'last_name': 'Piekara', 'country': 'Poland', 'year_of_birth': '1965 ', 'year_of_death': '', },
  {'name': 'John', 'last_name': 'Tolkien', 'country': 'England', 'year_of_birth': '', 'year_of_death': '', },
]).run()

rethink.db('library').table('books').insert([
  {'title': 'Macbeth', 'author': '09d3ca27-d906-4c81-93d0-4623c901f835', 'year': 1606, 'ISBN': '9780140707052', 'is_borrowed': 'true'},
  {'title': 'Macbeth', 'author': '09d3ca27-d906-4c81-93d0-4623c901f835', 'year': 1606, 'ISBN': '9780140707052', 'is_borrowed': 'false'},
  {'title': 'Macbeth', 'author': '09d3ca27-d906-4c81-93d0-4623c901f835', 'year': 1606, 'ISBN': '9780140707052', 'is_borrowed': 'false'},
  {'title': 'The Hobbit or There and Back Again', 'author': 'd192f8d8-b727  4-4b86-afe9-831cbc90ae3f', 'year': 1937, 'ISBN': '978026   41102217', 'is_borrowed': 'true'},
  {'title': 'The Hobbit or There and Back Again', 'author': 'd192f8d8-b727  4-4b86-afe9-831cbc90ae3f', 'year': 1937, 'ISBN': '978026   41102217', 'is_borrowed': 'false'},
  {'title': 'The Hobbit or There and Back Again', 'author': 'd192f8d8-b727  4-4b86-afe9-831cbc90ae3f', 'year': 1937, 'ISBN': '978026   41102217', 'is_borrowed': 'false'},
  {'title': 'Alicja', 'author': '30fbd29a-2ac7-45b9-8ee4-875f606f3f97', 'year': 2007, 'ISBN': '9788378780892', 'is_borrowed': 'true'},
  {'title': 'Alicja', 'author': '30fbd29a-2ac7-45b9-8ee4-875f606f3f97', 'year': 2007, 'ISBN': '9788375742008', 'is_borrowed': 'false'},
  {'title': 'Krew elfów', 'author': '3ca2bd3a-5169-42fb-afb6-bfd69b336251', 'year': 1994, 'ISBN': '9780316029193', 'is_borrowed': 'false'},
]).run()

rethink.db('library').table('users').insert([
  {'name': 'Adrian', 'last_name': 'Elwi', 'address': '1b5f0315-56b6-4c77-8f88-20628de770f0', 'date_of_birth': '05-06-1992', 'sex': 'male'},
  {'name': 'Karolina', 'last_name': 'Grechuta', 'address': '378afea8-8a31-4a9d-aaf7-0fb7c724fe21', 'date_of_birth': '23-01-2005', 'sex':'female'},
  {'name': 'Konstanty', 'last_name': 'Abrachamowicz', 'address': '4b42d0b2-ff17-404b-a4bb-d88361bce5da', 'date_of_birth': '06-07-1950', 'sex':'female'},
  {'name': 'Garwazy', 'last_name': 'Trąbke', 'address': '4eec8c20-d9f9-442f-97aa-933aaf27bc41', 'date_of_birth': '01-01-1905', 'sex':'male'},
  {'name': 'Alucja', 'last_name': 'Gawryl', 'address': '66a269f2-8dfd-4979-8ca5-a2017bf524a3', 'date_of_birth': '04-12-1997', 'sex':'female'},
]).run()

rethink.db('library').table('rental').insert([
  {'book_id': '2c0d8657-ee5c-4249-be88-707358de8d1b', 'user_id': '3c52b17d-ccd7-4a36-812e-3dfdfb09c248', 'date_of_loan': '24-04-2022', 'date_of_return': ''},
  {'book_id': 'f753819d-1327-4443-bb25-ef8fbee9fb9b', 'user_id': '3c52b17d-ccd7-4a36-812e-3dfdfb09c24', 'date_of_loan': '02-12-2021', 'date_of_return': ''},
  {'book_id': 'd5eca83a-0e60-44c2-ba39-d6d8eaa755b2', 'user_id': 'bae8b916-9dd9-4982-82b8-251fd8238c9a', 'date_of_loan': '05-03-2020', 'date_of_return': ''},
  {'book_id': '7b09273e-ad7f-4400-baae-c1da0d388da3', 'user_id': '79819c82-b97d-4f3e-beab-e71475c9b59a', 'date_of_loan': '13-11-2017', 'date_of_return': '12-11-2018'},
  {'book_id': '3a8b702f-9ab0-4bf1-a264-c0f3426a4e57', 'user_id': '3c52b17d-ccd7-4a36-812e-3dfdfb09c24', 'date_of_loan': '25-02-2016', 'date_of_return': '29-02-2016'},
  {'book_id': '23ed26ee-b1e2-4867-82a9-69488e827da6', 'user_id': '79819c82-b97d-4f3e-beab-e71475c9b59a', 'date_of_loan': '06-10-2016', 'date_of_return': '06-10-2021'},
]).run()


# update table
rethink.db('library').table('authors')\
    .filter({'id': '3fd60678-9b18-47e3-abc1-ca2adaed5221'})\
    .update({
        'year_of_birth': 1892,
        'year_of_death': 1973,
}).run()
"""

# retrieve some data
data = rethink.db('library').table('users').pluck(['name', 'last_name']).order_by(rethink.desc('last_name')).limit(3).run()
print(data)

# count users
user_count = rethink.db('library').table('users').count().run()
print(user_count)

# all books list
all_books = book_list = rethink.db('library').table('books').pluck('title').run()
print(all_books)

# distinct books list
book_list = rethink.db('library').table('books').pluck('title').distinct().run()
print(book_list)

# filtering
rethink.db('library').table('books').filter({'author': 'd192f8d8-b727-4b86-afe9-831cbc90ae3f'})

# join tables
join_tables = rethink.db('library').table('books').eq_join('author', rethink.db('library').table('authors')).zip()
print(join_tables)










