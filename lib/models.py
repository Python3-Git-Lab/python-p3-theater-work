from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String(100), nullable=False)
    location = Column(String(256))
    phone = Column(String(13))
    hired = Column(String())

    role_id = Column (Integer(), ForeignKey('roles.id'))

    def __repr__(self):
        return f'Audition(id={self.id}, ' + \
            f'actor={self.actor}, ' + \
            f'location={self.location})'

class Role(Base):
    __tablename__= 'roles'

    id= Column(Integer(), primary_key= True)
    character_name= Column(String())

    auditions = relationship('Audition', backref=backref('role'), cascade= 'all, delete-orphan')

    def __repr__(self):
        return f'Role(id= {self.id}, ' + \
            f'name= {self.character_name})'
