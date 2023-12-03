from database.connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime

class Accounts(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    mobile_number = Column(String)
    subscription = Column(Integer, ForeignKey("subscriptions.id"))

class ChoiceGroups(Base):
    __tablename__ = "choice_groups"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    option_type_id = Column(Integer, ForeignKey("option_type.id"))
    menu_items_id = Column(Integer, ForeignKey("menu_items.id"))

class ChoiceItems(Base):
    __tablename__ = "choice_items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    choice_groups_id = Column(Integer, ForeignKey("choice_groups.id"))

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

class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    accounts_id = Column(Integer, ForeignKey("accounts.id"))
    time_stamp = Column(DateTime)
    order_type_id = Column(Integer, ForeignKey("order_type.id"))
    order_status_id = Column(Integer, ForeignKey("order_status.id"))

class OrderDetails(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True)
    orders_id = Column(Integer, ForeignKey("orders.id"))
    menu_items_id = Column(Integer, ForeignKey("menu_items.id"))
    choice_items_id = Column(Integer, ForeignKey("choice_items.id"))

class OrderStatus(Base):
    __tablename__ = "order_status"
    id = Column(Integer, primary_key=True)
    status = Column(String)

class OrderType(Base):
    __tablename__ = "order_type"
    id = Column(Integer, primary_key=True)
    type = Column(String)

class RestaurantCategories(Base):
    __tablename__ = "restaurant_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
class RestaurantToCategory(Base):
    __tablename__ = "restaurant_to_category"
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    restaurant_categories_id = Column(Integer, ForeignKey("restaurant_categories.id"))

class Restaurants(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    icon_url = Column(String)
    background_url = Column(String)

class OptionType(Base):
    __tablename__ = "option_type"
    id = Column(Integer, primary_key=True)
    type = Column(String)

class Subscription(Base):
    __tablename__ = "subscription"
    id = Column(Integer, primary_key=True)
    type = Column(String)