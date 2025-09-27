"""
Simple script to verify the data in your Supabase table
"""

import pandas as pd
from supabase import create_client, Client
from config import SUPABASE_CONFIG, TABLE_NAME

def verify_supabase_data():
    """Verify and display the data in Supabase table"""
    print("Verifying Supabase Table Data")
    print("=" * 40)
    
    try:
        # Create Supabase client
        supabase: Client = create_client(SUPABASE_CONFIG["url"], SUPABASE_CONFIG["key"])
        print("[SUCCESS] Supabase client created")
        
        # Query all data
        response = supabase.table(TABLE_NAME).select("*").execute()
        
        if response.data:
            print(f"[SUCCESS] Data retrieved successfully!")
            print(f"   Total records: {len(response.data)}")
            print(f"   Columns: {list(response.data[0].keys())}")
            
            # Convert to DataFrame for better display
            df = pd.DataFrame(response.data)
            
            print(f"\nDataFrame Info:")
            print(f"   Shape: {df.shape}")
            print(f"   Columns: {list(df.columns)}")
            print(f"   Data types:")
            for col, dtype in df.dtypes.items():
                print(f"     {col}: {dtype}")
            
            print(f"\nAll Data:")
            print(df.to_string(index=False))
            
            # Show some statistics
            if 'unit_sf' in df.columns and 'rental_rate' in df.columns:
                print(f"\nStatistics:")
                print(f"   Average unit size: {df['unit_sf'].mean():.1f} sq ft")
                print(f"   Average rental rate: ${df['rental_rate'].mean():.2f}")
                print(f"   Total units: {df['unit_sf'].sum()} sq ft")
                print(f"   Total rental income: ${df['rental_rate'].sum():.2f}")
            
            return True
        else:
            print("[WARNING] No data found in table")
            return False
            
    except Exception as e:
        print(f"[ERROR] Failed to verify data: {str(e)}")
        return False

def main():
    """Main function"""
    success = verify_supabase_data()
    
    if success:
        print(f"\n[SUCCESS] Your Supabase table is ready to use!")
        print("You can now:")
        print("  - Query this data in your Streamlit app")
        print("  - Use it for data analysis")
        print("  - Add more records as needed")
    else:
        print(f"\n[ERROR] Could not verify data")
    
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = main()
    print(f"\nVerification completed with exit code: {exit_code}")
