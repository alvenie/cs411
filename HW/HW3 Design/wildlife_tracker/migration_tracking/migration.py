from typing import Any

class Migration:

    def __init__(self, 
                migration_id: int, 
                species: str, 
                start_location: str, 
                destination: str, 
                start_date: str, 
                status: str = 'Scheduled'):
        
        self.migration_id: int = migration_id
        self.species: str = species
        self.start_location: str = start_location
        self.destination: str = destination
        self.start_date: str = start_date
        self.status: str = status

    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass
