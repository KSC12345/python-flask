from src.db import get_db,get_connection
from pymongo import WriteConcern
from config import load_config
from concurrent.futures import ThreadPoolExecutor
import os

num_threads = os.cpu_count() * 2 
print("num_threads: ",num_threads)
executor = ThreadPoolExecutor(max_workers=num_threads)

envConfig = load_config()

def getUserList():
     userList = list(get_db().users.find({}, {"_id": 0}))
     return userList

def insertUser(userData):
      future = executor.submit(threadSafeInsertUser, userData)
      result = future.result()
      return result
      
def threadSafeInsertUser(userData):
     if (envConfig.MONGO_REPLICA):
          return transactionInsertUser(userData)
     else:
          return withoutTransactionInsertUser(userData)
    

def withoutTransactionInsertUser(userData):
     new_user_id = get_next_sequence_userid_value("userId")
     new_user = {
     "_id": new_user_id,  # Auto-incremented ID
     "name": userData['name'],
     "email": userData['email']
     }
     get_db().users.insert_one(new_user)
     return new_user
          
    
    

def transactionInsertUser(userData):
     with get_connection().start_session() as session:
         try:
            with session.start_transaction():
                try:
                    print("start_transaction")
                    new_user_id = get_next_sequence_userid_value_trasaction("userId",session)
                    new_user = {
                    "_id": new_user_id,  # Auto-incremented ID
                    "name": userData['name'],
                    "email": userData['email']
                    }
                    users_collection =  get_db().users.with_options(write_concern=WriteConcern("majority")) 
                    users_collection.insert_one(new_user,session=session)
                    session.commit_transaction()
                    return new_user
                except Exception as e:
                 print("Transaction failed. Aborting...", e)
                 session.abort_transaction()
                 raise
         except Exception as e:
            print("Transaction failed. Aborting...", e)
            raise
         finally:
          session.end_session()
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
    
def get_next_sequence_userid_value_trasaction(sequence_name,session):
    # Increment the counter atomically
    counters_collection =  get_db().counters.with_options(write_concern=WriteConcern("majority")) 
    result = counters_collection.find_one_and_update(
        {"_id": sequence_name},
        {"$inc": {"sequence_value": 1}},
        return_document=True,  # Returns the updated document
        upsert=True,
        session=session           # Creates a new document if it doesn't exist
    )
    return result['sequence_value']

def get_next_sequence_userid_value(sequence_name):
    # Increment the counter atomically
     result = get_db().counters.find_one_and_update(
        {"_id": sequence_name},
        {"$inc": {"sequence_value": 1}},
        return_document=True,  # Returns the updated document
        upsert=True           # Creates a new document if it doesn't exist
    )
     return result['sequence_value']
    