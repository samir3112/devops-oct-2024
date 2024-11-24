import os
mongo_user=os.environ.get("MONGO_USERNAME", "adminuser")
mongo_password=os.environ.get("MONGO_PASSWORD", "chandra")
mongo_address_write=os.environ.get("MONGO_ADDRESS_WRITE")
mongo_address_read=os.environ.get("MONGO_ADDRESS_READ")

mongo_connection_string_write = f"mongodb://{mongo_user}:{mongo_password}@{mongo_address_write}:27017/fruits_db?authSource=admin"
mongo_connection_string_read = f"mongodb://{mongo_user}:{mongo_password}@{mongo_address_read}:27017/fruits_db?authSource=admin"