import falcon
from controllers.PageController import PageController

pageRoutes = {}

pageRoutes['/myprofile'] = PageController()