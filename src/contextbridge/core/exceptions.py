class ContextBridgeError(Exception):
    """Base exception."""


class InvalidExportError(ContextBridgeError):
    """Invalid export structure."""


class ProjectNotFoundError(ContextBridgeError):
    """Requested project not found."""