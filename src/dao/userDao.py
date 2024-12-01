from src.db import get_db
import json

def getUserList():
     userList = list(get_db().users.find({}, {"_id": 0}))
     return userList

def insertUser(userData):
     new_user_id = get_next_sequence_userid_value("userId")
     new_user = {
     "_id": new_user_id,  # Auto-incremented ID
     "name": userData['name'],
     "email": userData['email']
     }
     get_db().users.insert_one(new_user)
     return new_user

# Find user by ID
def find_user_by_id(user_id):
    try:
        # Convert string ID to ObjectId
        user = get_db().users.find_one({"_id": int(user_id)})
        if user:
            return user
        else:
          raise ValueError(f"User with ID {user_id} not found")
    except Exception as e:
         raise e
    
# Update user by ID
def update_user_by_id(user_id,updatedata):
    try:
        
        updatedata.pop("id")  
        user = get_db().users.find_one_and_update(
            {"_id": user_id},  # Filter by _id
            {"$set": updatedata}     # Update operation
        )
        if user:
            return user
        else:
          raise ValueError(f"User with ID {user_id} not found")
    except Exception as e:
         raise e

# Function to delete a document by ID
def delete_user_by_id(user_id):
    try:
        # Delete the document with the specified _id
        result = get_db().users.delete_one({"_id": int(user_id)})
        
        if result.deleted_count == 0:
            raise ValueError(f"User with ID {user_id} not found")
        
        return f"Successfully deleted {result.deleted_count} document(s)"
    except Exception as e:
        raise e
    
def get_next_sequence_userid_value(sequence_name):
    # Increment the counter atomically
    result = get_db().counters.find_one_and_update(
        {"_id": sequence_name},
        {"$inc": {"sequence_value": 1}},
        return_document=True,  # Returns the updated document
        upsert=True           # Creates a new document if it doesn't exist
    )
    return result['sequence_value']

    