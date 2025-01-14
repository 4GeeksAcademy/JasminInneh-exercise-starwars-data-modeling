import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    date_joined = Column(String)
    Favorites = relationship("Favorites", back_populates="user")
    favorite_id = Column(Integer, ForeignKey("favorites.id"))

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship("Planet", back_populates="characters")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    planet_id = Column(Integer, ForeignKey('character.id'))
    resident = relationship("Character", back_populates="plantets", uselist=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user = relationship("User")
    user_id = Column(Integer, ForeignKey('user.id'))
    planet = relationship("Planets")
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character = relationship("Characters")
    character_id = Column(Integer, ForeignKey('characters.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')




# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}
