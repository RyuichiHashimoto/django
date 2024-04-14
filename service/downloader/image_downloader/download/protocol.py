from enum import Enum


class Protocol(Enum):
    http = "http://"
    https = "https://"

    @classmethod
    def is_supported_protocol(self, url: str):
        for protocol in Protocol:
            if url.startswith(protocol.value):
                return True
        return False
