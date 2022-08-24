def register_routers(app, logger):
    from controllers.hello import HelloController

    HelloController(app, logger)
