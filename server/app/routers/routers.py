def register_routes(app, logger):
    from controllers.hello import HelloController

    HelloController(app, logger)
