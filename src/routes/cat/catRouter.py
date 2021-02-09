import falcon
from controllers.CatController import CatController

catRoutes = {}

catRoutes['/gabriel'] = CatController()
catRoutes['/guilherme'] = CatController()