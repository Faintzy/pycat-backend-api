import falcon
from controllers.UserController import UserController

userRoutes = {}

userRoutes['/user/create'] = UserController()
userRoutes['/user/auth'] = UserController()