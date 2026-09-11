from abc import ABC, abstractmethod

class Repository(ABC);
    @abstractmethod
    def get(self, id_:int) -> dict:
        """Fetch a record by identifier."""
        pass

    @abstractmethod
    def save(self, data:dict) -> None:
        """Persist a record."""
        pass
class SQLRepository(Repository):
    def __init__(self, connection_string: str):
        self.conn = connection_string

    def get(self, id_: int) -> dict:
        return {"id": id_, "source": "SQL"}

    #Implement the missing abstract method:
    def save(self, data: dict) -> None:
        print(f"Saved {data} to {self.conn}")

    # Omitting save will cause instantiation to fail
repos = SQLRepository("sqlote:///:memory:") #This will raise TypeError because
repos.save({"id": 1, "name": "John Doe"})        
