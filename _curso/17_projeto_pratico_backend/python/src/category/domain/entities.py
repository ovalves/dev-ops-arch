from datetime import datetime

class Category:
    def __init__(self, name: str, description: str, is_active: bool, created_at: datetime=datetime):
        self.name = name
        self.description = description
        self.is_active = is_active
        self.created_at = created_at
