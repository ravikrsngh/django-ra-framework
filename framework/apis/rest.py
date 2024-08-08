import logging
from time import perf_counter

from rest_framework.viewsets import ViewSet

from framework.apis.aspect import ResourceOperation

operation_map = {
    "list": ResourceOperation.LIST,
    "listing": ResourceOperation.LIST,
    "retrieve": ResourceOperation.RETRIEVE,
    "create": ResourceOperation.CREATE,
    "partial_update": ResourceOperation.UPDATE,
    "destroy": ResourceOperation.DELETE
}

logger = logging.getLogger("")

class RestAPIViewset(ViewSet):
    resource_class = None

    def dispatch(self, request, *args, **kwargs):
        start = perf_counter()
        super().dispatch(request, *args, **kwargs)
        end = perf_counter()
        msg = f'URL - {request.path}, METHOD - {request.method}, DURATION - {end - start}.'
        logger.info(msg)
        return self.response

    def get_resource(self, request, *args, **kwargs):
        assert self.resource_class is not None, f'{self.__class__.__name__} should have a resource class.'
        resource_instance = self.resource_class(*args, **kwargs)
        return resource_instance