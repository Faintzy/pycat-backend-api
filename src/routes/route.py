from routes.cat.catRouter import catRoutes
from routes.user.userRouter import userRoutes
from routes.page.pageRouter import pageRoutes
from middlewares.auth import AuthMiddleware
import falcon

class Router():
    
    def route():

        global catRoutes

        routes = []

        routes.append(catRoutes)
        routes.append(userRoutes)
        routes.append(pageRoutes)

        app = falcon.App(
            middleware=[AuthMiddleware()]
        )

        for x in range(len(routes)):

            dictRoutes = routes[x]

            for key, val in dictRoutes.items():

                app.add_route(key, val)

        return app
    



    
