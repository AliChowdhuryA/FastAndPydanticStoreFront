# Table models for each product
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from databases import Database
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()