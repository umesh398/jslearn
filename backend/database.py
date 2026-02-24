from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://127.0.0.1:27017"

client = AsyncIOMotorClient(MONGO_URL)

db = client["inspection_db"]

# collections
users = db["users"]
profiles = db["profiles"]
inspections = db["inspections"]
inspection_images = db["inspection_images"]
login_logs = db["login_logs"]
