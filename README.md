
# Rethink - simple task

Simple task of usage Rethink. 
We will use this to build simple library database


#


## Instalation

You can instal Rethink from this link [https://rethinkdb.com/docs/install/](https://rethinkdb.com/docs/install/)
## Create Database
First step is to create database. Let's name it 'library'.

```
r.dbCreate('library')
```

## Remove Database
As default Rethink create databse 'test', we don't need it.
```
r.dbDrop('test')
```

## Create tables
We create some basic tables. 
```
r.db('library').tableCreate('books');
r.db('library').tableCreate('authors');
r.db('library').tableCreate('users');
r.db('library').tableCreate('address');
r.db('library').tableCreate('rental');
r.db('library').tableCreate('movies');
r.db('library').tableCreate('directors');

```
## Remove tables
OOOPS we creaedted to many tables, we don't rent movies, so we don't need 2 tables.
```
r.db('library').tableDrop('movies');
r.db('library').tableDrop('directors');
```
## Add first address
We have database, we have tables. Why don't fill it up?

First we need to add first addres.
```
r.db('library').table('address').insert({
  city: 'Warszawa',
  postal_code: '00-002',
  street: 'Leśna',
  hause_number: '18',
  flat_number: '',
	}
)
```

OK, everything works.
## Add many address

```
r.db('library').table('address').insert([
  {city: 'Warszawa', postal_code: '00-002', street: 'Rolna', hause_number: '24A', flat_number: '15'},
  {city: 'Warszawa', postal_code: '00-002', street: 'Anczyca Władysława Ludwika', hause_number: '5', flat_number: ''},
  {city: 'Warszawa', postal_code: '00-002', street: 'Antonia Corazziego', hause_number: '2B', flat_number: '1'},
  {city: 'Warszawa', postal_code: '00-002', street: 'Wały Jagiellońskie', hause_number: '1', flat_number: ''},
  {city: 'Warszawa', postal_code: '00-002', street: 'Kombatantów', hause_number: '4', flat_number: '24'},
  {city: 'Warszawa', postal_code: '00-002', street: 'Grenadierów', hause_number: '2', flat_number: ''},
  {city: 'Warszawa', postal_code: '00-002', street: 'Lanckorońska', hause_number: '3', flat_number: '7'},
  {city: 'Warszawa', postal_code: '00-002', street: 'Przestrzenna', hause_number: '5B', flat_number: '7'},
		
])
```
## Fill up
We can now fill the whole databse. We will use foreignt keys from other tables - their Id's. Thanks to that we will be able to reduce data storage and extra data.


```
r.db('library').table('authors').insert([
  {name: 'William', last_name: 'Shakespeare', country: 'England', year_of_birth: '1564', year_of_death: '1616', },
  {name: 'Andrzej', last_name: 'Sapkowski', country: 'Poland', year_of_birth: '1948', year_of_death: '', },
  {name: 'Jacek', last_name: 'Piekara', country: 'Poland', year_of_birth: '1965 ', year_of_death: '', },
  {name: 'John', last_name: 'Tolkien', country: 'England', year_of_birth: '', year_of_death: '', },
])
```

```
r.db('library').table('books').insert([
  {title: 'Macbeth', author: '09d3ca27-d906-4c81-93d0-4623c901f835', year: 1606, ISBN: '9780140707052', is_borrowed: true},
  {title: 'Macbeth', author: '09d3ca27-d906-4c81-93d0-4623c901f835', year: 1606, ISBN: '9780140707052', is_borrowed: false},
  {title: 'Macbeth', author: '09d3ca27-d906-4c81-93d0-4623c901f835', year: 1606, ISBN: '9780140707052', is_borrowed: false},
  {title: 'The Hobbit or There and Back Again', author: 'd192f8d8-b727-4b86-afe9-831cbc90ae3f', year: 1937, ISBN: '9780261102217', is_borrowed: true,},
  {title: 'The Hobbit or There and Back Again', author: 'd192f8d8-b727-4b86-afe9-831cbc90ae3f', year: 1937, ISBN: '9780261102217', is_borrowed: false},
  {title: 'The Hobbit or There and Back Again', author: 'd192f8d8-b727-4b86-afe9-831cbc90ae3f', year: 1937, ISBN: '9780261102217', is_borrowed: false},
  {title: 'Alicja', author: '30fbd29a-2ac7-45b9-8ee4-875f606f3f97', year: 2007, ISBN: '9788378780892', is_borrowed: true,},
  {title: 'Alicja', author: '30fbd29a-2ac7-45b9-8ee4-875f606f3f97', year: 2007, ISBN: '9788375742008', is_borrowed:  false},
  {title: 'Krew elfów', author: '3ca2bd3a-5169-42fb-afb6-bfd69b336251', year: 1994, ISBN: '9780316029193', is_borrowed: false},
])
```

```
r.db('library').table('users').insert([
  {name: 'Adrian', last_name: 'Elwi', address: '1b5f0315-56b6-4c77-8f88-20628de770f0', date_of_birth: '05-06-1992', sex: 'male',},
  {name: 'Karolina', last_name: 'Grechuta', address: '378afea8-8a31-4a9d-aaf7-0fb7c724fe21', date_of_birth: '23-01-2005', sex:'female',},
  {name: 'Konstanty', last_name: 'Abrachamowicz', address: '4b42d0b2-ff17-404b-a4bb-d88361bce5da', date_of_birth: '06-07-1950', sex:'female',},
  {name: 'Garwazy', last_name: 'Trąbke', address: '4eec8c20-d9f9-442f-97aa-933aaf27bc41', date_of_birth: '01-01-1905', sex:'male',},
  {name: 'Alucja', last_name: 'Gawryl', address: '66a269f2-8dfd-4979-8ca5-a2017bf524a3', date_of_birth: '04-12-1997', sex:'female',},
])
```

```
r.db('library').table('rental').insert([
  {book_id: '2c0d8657-ee5c-4249-be88-707358de8d1b', user_id: '3c52b17d-ccd7-4a36-812e-3dfdfb09c248', date_of_loan: '24-04-2022', date_of_return: '',},
  {book_id: 'f753819d-1327-4443-bb25-ef8fbee9fb9b', user_id: '3c52b17d-ccd7-4a36-812e-3dfdfb09c24', date_of_loan: '02-12-2021', date_of_return: '',},
  {book_id: 'd5eca83a-0e60-44c2-ba39-d6d8eaa755b2', user_id: 'bae8b916-9dd9-4982-82b8-251fd8238c9a', date_of_loan: '05-03-2020', date_of_return: '',},
  {book_id: '7b09273e-ad7f-4400-baae-c1da0d388da3', user_id: '79819c82-b97d-4f3e-beab-e71475c9b59a', date_of_loan: '13-11-2017', date_of_return: '12-11-2018',},
  {book_id: '3a8b702f-9ab0-4bf1-a264-c0f3426a4e57', user_id: '3c52b17d-ccd7-4a36-812e-3dfdfb09c24', date_of_loan: '25-02-2016', date_of_return: '29-02-2016',},
  {book_id: '23ed26ee-b1e2-4867-82a9-69488e827da6', user_id: '79819c82-b97d-4f3e-beab-e71475c9b59a', date_of_loan: '06-10-2016', date_of_return: '06-10-2021',},
])
```
## Update row


We have now many data in tables, but data about Tolien is not complete. We must update his birth and death year.

```
r.db('library').table("authors").filter({
		id: 'd192f8d8-b727-4b86-afe9-831cbc90ae3f'
}).update({
    year_of_birth: 1892,
  	year_of_death: 1973,
})
```
## Advanced sorting

Show from user table only name and last, sorted by  last name desceding, and only first 3 of them.
```
r.db('library').table('users').pluck(['name', 'last_name']).orderBy(r.desc('last_name')).limit(3)
```
## Pluck
Show only chosen fields

## orderBy
Show results in incresing direction, to show in desceding we need add 
```
r.desc('field')
```

## Count

To cout users we use:
```
r.db('library').table('users').count()
```


## Distinct
To show user cities we use:
```
r.db('library').table('address').pluck('city').distinct()
```
## Filtring

To show all books writen by Tolkien we need to use filtring. 


```
r.db('library').table('books').filter({author: 'd192f8d8-b727-4b86-afe9-831cbc90ae3f'})
```



## Join
Filtring when we must give specifc id may be difficult, so we should join 2 tables - authors and books - to look for book with specific author.

```
r.db('library').table('books').eqJoin('author', r.db('library').table('authors')).zip()
```
Thanks to that we will have joined 2 tables. Function 
```
zip()
```
 will make that we have them connected, not separeted to left and right.



 ## Join Filtring
  Now we can add filtring to search for tolkien masterpieces.

 ```
 r.db('library').table('books').eqJoin('author', r.db('library').table('authors')).zip().filter({last_name: 'Tolkien'})
 ```

 
## Alter Table


Hmm we have some data, which can be reduced. In table address there is a lot of 'Warszawa' and the same 'postal code'. So we should place that data to anather table. First we create new table:

```
r.db('library').tableCreate('cities-with-postal-code');
```

Insert data:

```
r.db('library').table('cities-with-postal-code').insert({
  city: 'Warszawa',
  postal_code: '00-002',
	}
)
```

Now we can add field to all rows:
```
r.db('library').table('address').update({city_with_postal_code: "57c27fef-0ae8-4f23-b528-81c9fb603c49"})
```

Remove old fields. There should be only foreig keys to cities with postal code.
```
r.db('library').table('address').replace(r.row.without('city', 'postal_code'))
```
## Remove Row

One of the users want to delete account.  We can do it by:

```
r.db('library').table('users').filter({id: 'dc09dbd8-a833-41f9-b1ad-30b2b5e81939'}).delete()
```
