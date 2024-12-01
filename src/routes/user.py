from flask import Blueprint,jsonify,abort,request

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
    return jsonify(users)

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
    user = users.get(user_id)
    if not user:
        abort(404, description=f"User with ID {user_id} not found.")
    return jsonify(user)

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
 
    user = users.get(int(user_id))
    if not user:
        abort(404, description=f"User with ID {user_id} not found.")
    return jsonify(user)



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
    
    dict_length = len(users)
    print("dict_length",dict_length)
    users[dict_length+1]=data
    print(users)
    return jsonify({"message": f"User {name} registered successfully!", "email": email}), 201