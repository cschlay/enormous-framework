import datetime
from typing import Optional


class AuditLogger:
    """Logger for audit statistics and proofs if something goes wrong."""

    def info(self, message: str, user_id: Optional[int] = None):
        """
        Log INFO -level events the actions may be linked to particular user.

        :param user_id: if supplied, then the event is linked to a user
        :param message: to log
        """
        # TODO: Implement audit logging for INFO level events.

        # Temporary for development only info:
        timestamp = datetime.datetime.now()
        print(timestamp, "INFO", message)
