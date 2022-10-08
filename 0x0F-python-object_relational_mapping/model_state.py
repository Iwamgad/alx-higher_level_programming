#!/usr/bin/python3
"""
This is a python file that contains the class definition of a
State and an instance Base = declarative_base()
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
