from router import Router

@Router.route("pools.list")
def list(id):
    print("Called pools.list with id: {}".format(id))

@Router.route("pools.get")
def get(id):
    print("Called: pools.get")
