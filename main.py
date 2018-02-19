""" Main """

from api.router import Router

def handler(event, _):
    """ Lambda handler for incoming requests. Will route
        event data based upon the 'route' parameter.

        {'route':'service.method'}
    """
    router = Router()
    return router.serve(**event)
