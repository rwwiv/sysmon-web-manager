from django.http import Http404, JsonResponse
from .heartbeatService import update_agent_status
from .heartbeatService import create_agent
from logging_service import heartbeat_logging_service as log


def index(request, id):
    if request.method == 'PUT':
        log.debug("PUT request recieved at /heartbeat/<UUID> endpoint")
        values = update_agent_status(id, request)
        return JsonResponse(values)
    elif request.method == 'POST':
        log.debug("POST request recieved at /heartbeat/<UUID> endpoint")
        values = create_agent(id, request.META.get('REMOTE_ADDR'))
        return JsonResponse(values)
    else:
        log.warn("request without a mapping recieved raising a 404")
        raise Http404()
