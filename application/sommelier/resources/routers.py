from .wine import WinesApi

def initialize_routes(api):
    api.add_resource(WinesApi, '/wines')