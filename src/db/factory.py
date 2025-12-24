from src.db.postgres import PostgresDatabase

def make_database(database_type: str = "postgres", **kwargs):
    """Factory function to create database instances."""
    
    if database_type == "postgres":
        return PostgresDatabase(**kwargs)
    else:
        raise ValueError(f"Unknown database type: {database_type}")
