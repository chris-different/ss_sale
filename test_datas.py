from faker import Faker
from ss_sale.models import db,User,Server
from random import randint



fake = Faker()


def iter_user():
    for i in range(200):
        yield User(
            username = fake.word()+str(randint(400,500)),
            email = fake.word()+str(randint(1,1000))+'@'+'gmail.com',
            password = '123456'
            )


def iter_server():
    for i in range(100):
        yield Server(
            ip_address = str(randint(0,255))+'.'+str(randint(0,255))+'.'+str(randint(0,255))+'.'+str(randint(0,255)),
            city_address = fake.word()+fake.word(),
            timeout = randint(100,1000),
            port = randint(10,10000),
            password = '123456'
            )



def run():
    for user in iter_user():
        db.session.add(user)
         
    for server in iter_server():
        db.session.add(server)

        
    for i in User.query.all():
        servers = Server.query.all()
        a = randint(0,99)
        b = randint(0,99)
        server = servers[a]
        server.users.append(i)
        db.session.add(server)
        if a!=b:
            server = servers[b]
            server.users.append(i)
            db.session.add(server)
        else:
            pass

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()










