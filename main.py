
from api.router import Router

def handler(event, context):
    router = Router()
    router.serve(**event)
