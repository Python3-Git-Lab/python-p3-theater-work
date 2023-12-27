#!/usr/bin/env python3

# Script goes here!
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Audition, Role

if __name__ == '__main__':
    engine = create_engine('sqlite:///theater.db')
    Session = sessionmaker(bind = engine)
    session = Session()

    session.query(Audition).delete()
    session.query(Role).delete()

    fake = Faker()

    hire= ['yes','no']
    locations= ['Muranga', 'Nairobi', 'Thika', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret', 'Bungoma', 'Kiambu', 'Naivasha', 'Nanyuki']
    Roles= ['Father', 'Mother', 'Son', 'Doctor', 'Nurse', 'Teacher', 'Daughter', 'Police1', 'Police2', 'Surgeon', 'Artist']

    roles= []
    for i in range(20):
        role= Role(
            character_name= random.choice(Roles)
        )

        session.add(role)
        session.commit()
        roles.append(role)

    auditions = []
    for role in roles:
        for i in range(random.randint(1,10)):
            audition = Audition(
                actor = fake.unique.name(),
                location = random.choice(locations),
                phone = random.randint(9000000, 1000000000),
                hired = random.choice(hire),
                role_id=role.id
            )

            auditions.append(audition)
    
    session.bulk_save_objects(auditions)
    session.commit()
    session.close()