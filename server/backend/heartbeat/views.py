from django.http import Http404, JsonResponse, HttpResponseNotAllowed, HttpResponse
from .heartbeat_service import update_agent_status
from .heartbeat_service import create_agent
from logging_service import heartbeat_logging_service as log


def index(request, uuid):
    if request.method == 'PUT':
        log.debug("PUT request recieved at /heartbeat/<UUID> endpoint")
        values = update_agent_status(uuid, request)
        return JsonResponse(values)
    elif request.method == 'POST':
        log.debug("POST request recieved at /heartbeat/<UUID> endpoint")
        result = create_agent(uuid, request.META.get('REMOTE_ADDR'))
        if result != 0:
            return HttpResponseNotAllowed('Agent already exists')
        else:
            return HttpResponse('OK')
    else:
        log.warn("request without a mapping recieved raising a 404")
        raise Http404()
