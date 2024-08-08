from enum import Enum


class ResourceOperation(Enum):
    LIST = "list"
    RETRIEVE = "retrieve"
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
