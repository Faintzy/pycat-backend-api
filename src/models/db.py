from pony.orm import *

db = Database()

class User(db.Entity):
    
    username = Required(str)
    password = Required(str)

    @db_session
    def create(username, password):
        
        usr = User(username=username, password=password)
        commit()
    
    @db_session
    def auth(username, password):
    
        usr = db.select('username FROM user WHERE username = $username AND password = $password')

        if len(usr) == 0:

            return '0'
        
        return usr[0]

def createConnection():

    db.bind(
        provider='mysql', host='localhost',
        user='root', passwd='',
        db='pycat'
    )

    db.generate_mapping(create_tables=True)