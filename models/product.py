from typing import Dict
from db import Base, session, engine, local_session
from sqlalchemy import Column, String, DateTime, Float, UUID
from sqlalchemy.sql import func
from uuid import uuid4
from pydantic import BaseModel
from pydantic.types import constr, conint
from datetime import datetime



class ProductModel(BaseModel):
    name            : constr(max_length=30)
    price           : conint(gt=0)
    category        : constr(max_length=10)


class Product(Base):
    __tablename__ = "product"
    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name        = Column(String, nullable=False)
    price       = Column(Float, default=0)
    category    = Column(String, nullable=True)
    created_at  = Column(DateTime, default=func.now())
    updated_at  = Column(DateTime, default=func.now(), onupdate=func.now())
    status      = Column(String, default="pending")

    def save(self):
        with session as s:
            s.add(self)
            s.commit()
            s.refresh(self)
            return self

    @classmethod
    def delete(cls, id: str):
        with session as s:
            product = s.query(cls).filter(cls.id == id).one()
            s.delete(product)
            s.commit()
    @classmethod
    def update(cls, id: str, name: str = None, price: int = None, category: str = None):
        with session as s:
            s.query(cls).filter(cls.id == id).update({'name':name if name else cls.name, 'price': price if price else cls.price, 'category': category if category else cls.category})
            s.commit()


    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'status': self.status
        }
Base.metadata.create_all(engine)