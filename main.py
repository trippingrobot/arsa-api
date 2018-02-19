
from api.router import Router

# TODO: Logging
def handler(event, context):
    router = Router()
    router.serve(**event)
