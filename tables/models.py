from database.connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean, ColumnDefault

class Accounts(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(240))
    mobile_number = Column(String(20))
    subscription_id = Column(Integer, ForeignKey("subscription.id"))

class ChoiceGroups(Base):
    __tablename__ = "choice_groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(240))
    option_type_id = Column(Integer, ForeignKey("option_type.id"))
    menu_items_id = Column(Integer, ForeignKey("menu_items.id"))
    allow_multiple_selection = Column(Boolean, ColumnDefault(False))
    status = Column(Integer, ForeignKey("choice_status.id"), ColumnDefault(1))

class ChoiceItems(Base):
    __tablename__ = "choice_items"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Float)
    choice_groups_id = Column(Integer, ForeignKey("choice_groups.id"))
    status = Column(Integer, ForeignKey("choice_status.id"), ColumnDefault(1))

class ChoiceStatus(Base):
    __tablename__ = "choice_status"
    id = Column(Integer, primary_key=True)
    status = Column(String(20))

class MenuCategories(Base):
    __tablename__ = "menu_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    restaurants_id = Column(Integer, ForeignKey("restaurants.id"))
    description = Column(String(240))

class MenuItems(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(240))
    price = Column(Float)
    menu_categories_id = Column(Integer, ForeignKey("menu_categories.id"))
    icon_url = Column(String(500))

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
    status = Column(String(20))

class OrderType(Base):
    __tablename__ = "order_type"
    id = Column(Integer, primary_key=True)
    type = Column(String(20))

class RestaurantCategories(Base):
    __tablename__ = "restaurant_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
class RestaurantToCategory(Base):
    __tablename__ = "restaurant_to_category"
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    restaurant_categories_id = Column(Integer, ForeignKey("restaurant_categories.id"))

class Restaurants(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    icon_url = Column(String(500))
    background_url = Column(String(500))

class OptionType(Base):
    __tablename__ = "option_type"
    id = Column(Integer, primary_key=True)
    type = Column(String(20))

class Subscription(Base):
    __tablename__ = "subscription"
    id = Column(Integer, primary_key=True)
    type = Column(String(20))