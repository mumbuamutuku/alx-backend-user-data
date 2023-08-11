Tasks
0. Et moi et moi et moi!
mandatory
Score: 0.0% (Checks completed: 0.0%)
Copy all your work of the 0x06. Basic authentication project in this new folder.

In this version, you implemented a Basic authentication for giving you access to all User endpoints:

GET /api/v1/users
POST /api/v1/users
GET /api/v1/users/<user_id>
PUT /api/v1/users/<user_id>
DELETE /api/v1/users/<user_id>
Now, you will add a new endpoint: GET /users/me to retrieve the authenticated User object.

Copy folders models and api from the previous project 0x06. Basic authentication
Please make sure all mandatory tasks of this previous project are done at 100% because this project (and the rest of this track) will be based on it.
Update @app.before_request in api/v1/app.py:
Assign the result of auth.current_user(request) to request.current_user
Update method for the route GET /api/v1/users/<user_id> in api/v1/views/users.py:
If <user_id> is equal to me and request.current_user is None: abort(404)
If <user_id> is equal to me and request.current_user is not None: return the authenticated User in a JSON response (like a normal case of GET /api/v1/users/<user_id> where <user_id> is a valid User ID)
Otherwise, keep the same behavior

1. Empty session
mandatory
Score: 0.0% (Checks completed: 0.0%)
Create a class SessionAuth that inherits from Auth. For the moment this class will be empty. It’s the first step for creating a new authentication mechanism:

validate if everything inherits correctly without any overloading
validate the “switch” by using environment variables
Update api/v1/app.py for using SessionAuth instance for the variable auth depending of the value of the environment variable AUTH_TYPE, If AUTH_TYPE is equal to session_auth:

import SessionAuth from api.v1.auth.session_auth
create an instance of SessionAuth and assign it to the variable auth
Otherwise, keep the previous mechanism.

2. Create a session
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update SessionAuth class:

Create a class attribute user_id_by_session_id initialized by an empty dictionary
Create an instance method def create_session(self, user_id: str = None) -> str: that creates a Session ID for a user_id:
Return None if user_id is None
Return None if user_id is not a string
Otherwise:
Generate a Session ID using uuid module and uuid4() like id in Base
Use this Session ID as key of the dictionary user_id_by_session_id - the value for this key must be user_id
Return the Session ID
The same user_id can have multiple Session ID - indeed, the user_id is the value in the dictionary user_id_by_session_id
Now you an “in-memory” Session ID storing. You will be able to retrieve an User id based on a Session ID.
