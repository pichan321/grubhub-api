from database.connection import Base
from sqlalchemy import Integer, Float, String

class Accounts(Base):
    __tablename__ = "accounts"

class ChoiceGroups(Base):
    __tablename__ = "choice_groups"

class ChoiceItems(Base):
    __tablename__ = "choice_items"

class MenuCategories(Base):
    __tablename__ = "menu_categories"

class MenuItems(Base):
    __tablename__ = "menu_items"

class OrderDetails(Base):
    __tablename__ = "order_details"

class OrderStatus(Base):
    __tablename__ = "order_status"

class OrderType(Base):
    __tablename__ = "order_type"

class RestaurantCategories(Base):
    __tablename__ = "restaurant_categories"

class RestaurantToCategory(Base):
    __tablename__ = "restaurant_to_category"

class Restaurants(Base):
    __tablename__ = "restaurants"

class Subscription(Base):
    __tablename__ = "subscription"