from abc import ABC, abstractmethod

class ProviderInterface(ABC):
    @abstractmethod
    def getEndpoints(self):
        """Sollte eine Liste oder ein Dictionary von Endpoints zurückgeben."""
        pass

    @abstractmethod
    def getValue(self, key, endpoint):
        """Sollte den Wert für einen gegebenen Schlüssel und Endpoint zurückgeben."""
        pass

    @abstractmethod
    def fetch(self, endpoint):
        """Sollte den Inhalt vom gegebenen Endpoint abrufen und in die Datenbank speichern."""
        pass
