from database.connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Accounts(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)

class ChoiceGroups(Base):
    __tablename__ = "choice_groups"
    id = Column(Integer, primary_key=True)

class ChoiceItems(Base):
    __tablename__ = "choice_items"
    id = Column(Integer, primary_key=True)

class MenuCategories(Base):
    __tablename__ = "menu_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    restaurants_id = Column(Integer, ForeignKey("restaurants.id"))
    description = Column(String)

class MenuItems(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    menu_categories_id = Column(Integer, ForeignKey("menu_categories.id"))
    icon_url = Column(String)

class OrderDetails(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True)

class OrderStatus(Base):
    __tablename__ = "order_status"
    id = Column(Integer, primary_key=True)

class OrderType(Base):
    __tablename__ = "order_type"
    id = Column(Integer, primary_key=True)

class RestaurantCategories(Base):
    __tablename__ = "restaurant_categories"
    id = Column(Integer, primary_key=True)
    

class RestaurantToCategory(Base):
    __tablename__ = "restaurant_to_category"
    id = Column(Integer, primary_key=True)

class Restaurants(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    icon_url = Column(String)
    background_url = Column(String)

class Subscription(Base):
    __tablename__ = "subscription"
    id = Column(Integer, primary_key=True)