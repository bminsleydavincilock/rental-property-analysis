"""
Script to get all last names from the Supabase table
"""

from supabase import create_client, Client
from config import SUPABASE_CONFIG, TABLE_NAME

def get_lastnames():
    """Get all last names from the Supabase table"""
    try:
        print("Accessing Supabase table to get last names...")
        print(f"URL: {SUPABASE_CONFIG['url']}")
        print(f"Table: {TABLE_NAME}")
        print()
        
        # Create Supabase client
        supabase: Client = create_client(SUPABASE_CONFIG["url"], SUPABASE_CONFIG["key"])
        print("[SUCCESS] Connected to Supabase")
        
        # Query only the last_name column
        response = supabase.table(TABLE_NAME).select("last_name").execute()
        
        if response.data:
            print(f"[SUCCESS] Retrieved {len(response.data)} records")
            print()
            
            # Extract last names
            lastnames = [record['last_name'] for record in response.data]
            
            print("Last Names in the table:")
            print("=" * 30)
            for i, name in enumerate(lastnames, 1):
                print(f"{i:2d}. {name}")
            
            print()
            print(f"Total: {len(lastnames)} last names")
            
            return lastnames
        else:
            print("[WARNING] No data found in the table")
            return []
            
    except Exception as e:
        print(f"[ERROR] Failed to access Supabase: {str(e)}")
        return None

if __name__ == "__main__":
    lastnames = get_lastnames()
    
    if lastnames is not None:
        print(f"\n[SUCCESS] Retrieved {len(lastnames)} last names from Supabase")
    else:
        print(f"\n[ERROR] Could not retrieve last names")
