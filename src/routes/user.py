from flask import Blueprint,jsonify,abort,request
from src.dao.userDao import getUserList,insertUser,find_user_by_id,update_user_by_id,delete_user_by_id

user_blueprint = Blueprint('user', __name__)

users = {
    1: { "name": "Alice", "email": "alice@example.com"},
    2: { "name": "Bob", "email": "bob@example.com"},
}

# Add routes to the blueprint
@user_blueprint.route('', methods=['GET'])
def userList():
    """
        Get a list of all users
        ---
        responses:
          200:
            description: List of users retrieved successfully
            schema:
              type: array
              items:
                id: User
                properties:
                  id:
                    type: integer
                    example: 1
                  name:
                    type: string
                    example: "Leanne Graham"
                  email:
                    type: string
                    example: "Sincere@april.biz"
        """
  

    return jsonify(getUserList())

# Add routes to the blueprint
@user_blueprint.route('/<int:user_id>', methods=['GET'])
def findUser(user_id):
    """
        Get user details by user ID
        This will automatically be documented in Swagger UI.
        ---
        parameters:
          - name: user_id
            in: path
            type: integer
            required: true
            description: The user ID to retrieve data for
        responses:
          200:
            description: User data retrieved successfully
            schema:
              id: User
              properties:
                id:
                  type: integer
                  example: 1
                name:
                  type: string
                  example: "Leanne Graham"
                email:
                  type: string
                  example: "Sincere@april.biz"
          404:
            description: User not found
        """
    try:
        user = find_user_by_id(user_id)
        if not user:
            abort(404, description=f"User with ID {user_id} not found.")  
        return jsonify(user)
    except Exception as e:
            abort(404, description=f"User with ID {user_id} not found.")


@user_blueprint.route('/search', methods=['GET'])
def searchUser():
    """
        Get user details by user ID
        This will automatically be documented in Swagger UI.
        ---
        parameters:
          - name: id
            in: query
            type: integer
            required: true
            description: The user ID to retrieve data for
        responses:
          200:
            description: User data retrieved successfully
            schema:
              id: User
              properties:
                id:
                  type: integer
                  example: 1
                name:
                  type: string
                  example: "Leanne Graham"
                email:
                  type: string
                  example: "Sincere@april.biz"
          404:
            description: User not found
        """
    user_id = request.args.get('id')  # Returns the value of 'query'
 
    try:
        user = find_user_by_id(user_id)
        if not user:
            abort(404, description=f"User with ID {user_id} not found.")  
        return jsonify(user)
    except Exception as e:
            abort(404, description=f"User with ID {user_id} not found.")




# Add routes to the blueprint
@user_blueprint.route('', methods=['POST'])
def createUser():
    """
        Create a new user
        ---
        parameters:
          - name: user
            in: body
            required: true
            schema:
              id: User
              required:
                - name
                - email
              properties:
                name:
                  type: string
                  example: "John Doe"
                email:
                  type: string
                  example: "john.doe@example.com"
        responses:
          201:
            description: User created successfully
        """
    data = request.get_json()
      # Validate the received data
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400
       # Process the data
    name = data['name']
    email = data['email']
    newUser = insertUser(data)
   
    return jsonify({"message": f"User {name} registered successfully!", "email": email,"id":newUser['_id']}), 201

# Add routes to the blueprint
@user_blueprint.route('', methods=['PUT'])
def updateUser():
    """
        Update user details
        ---
        parameters:
          - name: user
            in: body
            required: true
            schema:
              id: UpdateUser
              required:
                - name
                - email
                - id
              properties:
                id:
                  type: string
                  example: "1"
                name:
                  type: string
                  example: "John Doe"
                email:
                  type: string
                  example: "john.doe@example.com"
        responses:
          201:
            description: User created successfully
        """
    data = request.get_json()
      # Validate the received data
    if not data or 'id' not in data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400
       # Process the data
    id = data['id']
    try:
        user = update_user_by_id(int(id),data)
        if not user:
            abort(404, description=f"User with ID {id} not found.")  
        return jsonify(user)
    except ValueError as e:
            print("Error:", e)
            abort(404, description=f"{e}")
    except Exception as e:
            print("Error:", e)
            abort(500, description=f"{e}")



# Add routes to the blueprint
@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    """
        Delete user by user ID
        This will automatically be documented in Swagger UI.
        ---
        parameters:
          - name: user_id
            in: path
            type: integer
            required: true
            description: The user ID to retrieve data for
        responses:
          201:
            description: User delete successfully
        """
    try:
        user = delete_user_by_id(user_id)
        return jsonify(description=f"{user}")
    except ValueError as e:
            print("Error:", e)
            abort(404, description=f"{e}")
    except Exception as e:
            abort(500, description=f"User with ID {user_id} not found.")