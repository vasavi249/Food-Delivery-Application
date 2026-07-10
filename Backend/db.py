from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["FoodDeliveryDB"]

customers = db["customers"]
restaurants = db["restaurants"]
foods = db["foods"]
cart = db["cart"]
orders = db["orders"]