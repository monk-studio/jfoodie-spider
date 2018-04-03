from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String

from . import db
from ._utils import I18n


class RestaurantCategory(db.Model):
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    category_id = Column(Integer, ForeignKey('category.id'))


class Category(db.Model):
    id = Column(Integer, primary_key=True)
    name_ja = Column(String(100), unique=True)
    name_en = Column(String(100))
    name_cn = Column(String(100))

    def to_dict(self):
        return I18n.complex(
            self.name_ja,
            self.name_en or self.name_ja,
            self.name_cn or self.name_ja
        )