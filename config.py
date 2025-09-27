"""
Configuration file for Supabase connection
"""

# Supabase Configuration
SUPABASE_CONFIG = {
    "url": "https://yyrwwxgfbeisquzwixuk.supabase.co",  # Replace with your actual Supabase URL
    "key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl5cnd3eGdmYmVpc3F1endpeHVrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg5OTU5NTIsImV4cCI6MjA3NDU3MTk1Mn0.3VqefG5756l8cmodw8dqxEto4U-q6DSOgwITtp2NR94",  # Replace with your actual anon key
    "email": "DaVinciLock-Brad",
    "password": "pled0!Naples",
    "project": "rental-property-analysis-supabase",
    "database": "practice_dataset"
}

# SQLAlchemy Database Configuration
# Supabase PostgreSQL connection details
DB_CONFIG = {
    "host": "db.yyrwwxgfbeisquzwixuk.supabase.co",  # Supabase direct host
    "port": "5432",  # Standard PostgreSQL port
    "database": "postgres",
    "username": "postgres",
    "password": "pled0!Naples",  # Your database password (may need to be updated)
    "schema": "public"
}

# Database table name
TABLE_NAME = "practice_dataset"
