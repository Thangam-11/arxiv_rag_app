from contextlib import contextmanager
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

from src.db.interface.database import Database

class PostgresDatabase(Database):
    """PostgreSQL database implementation."""
    
    def __init__(self, database_url: str = None):
        self.database_url = database_url or os.getenv(
            "POSTGRES_DATABASE_URL",
            "postgresql+psycopg2://rag_user:rag_password@postgres:5432/rag_db"
        )
        
        self.engine = create_engine(
            self.database_url,
            pool_pre_ping=True,
            pool_size=10,
            max_overflow=20
        )
        
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )
    
    @contextmanager
    def get_session(self):
        """Get a database session context manager."""
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    
    def create_tables(self):
        """Create all database tables."""
        from src.models import Base
        
        print("Creating database tables...")
        Base.metadata.create_all(bind=self.engine)
        
        # Verify tables created
        with self.engine.connect() as conn:
            result = conn.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public' 
                  AND table_name IN ('papers', 'users', 'embeddings')
                ORDER BY table_name;
            """))
            tables = [row[0] for row in result]
            
        if tables:
            print(f"✓ Created {len(tables)} tables:")
            for table in tables:
                print(f"  • {table}")
        else:
            print("⚠ No tables created")
        
        return tables
    
    def drop_tables(self):
        """Drop all database tables."""
        from src.models import Base
        
        print("⚠ Dropping all tables...")
        Base.metadata.drop_all(bind=self.engine)
        print("✓ Tables dropped")
