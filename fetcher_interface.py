from abc import ABC, abstractmethod

class FetcherInterface(ABC):
    @abstractmethod
    def setUrl(self, url: str) -> None:
        """Setzt die Basis-URL für die API."""
        pass

    @abstractmethod
    def setAuth(self, grant_type: str, client_id: str, client_secret: str) -> None:
        """Konfiguriert die Authentifizierung."""
        pass

    @abstractmethod
    def fetch(self, entityname: str, page: int, limit: int) -> dict:
        """
        Ruft Daten für ein bestimmtes Entity ab.
        Erwartet ein JSON-ähnliches Dict als Antwort.
        """
        pass
