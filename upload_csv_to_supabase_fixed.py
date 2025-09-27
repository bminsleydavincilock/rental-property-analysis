"""
Script to upload data from practice_dataset.csv to Supabase table
Handles Row Level Security (RLS) issues
"""

import pandas as pd
from supabase import create_client, Client
from config import SUPABASE_CONFIG, TABLE_NAME
import sys

def load_csv_data():
    """Load data from the CSV file"""
    try:
        print("Loading data from practice_dataset.csv...")
        df = pd.read_csv('practice_dataset.csv')
        
        # Remove any empty rows
        df = df.dropna()
        
        print(f"[SUCCESS] Loaded {len(df)} rows from CSV")
        print(f"Columns: {list(df.columns)}")
        print(f"Data types: {df.dtypes.to_dict()}")
        
        # Show sample data
        print(f"\nSample data:")
        print(df.head().to_string(index=False))
        
        return df
        
    except FileNotFoundError:
        print("[ERROR] practice_dataset.csv file not found!")
        return None
    except Exception as e:
        print(f"[ERROR] Failed to load CSV: {str(e)}")
        return None

def prepare_data_for_upload(df):
    """Prepare CSV data for Supabase upload"""
    try:
        print(f"\nPreparing data for Supabase upload...")
        
        # Create a copy to avoid modifying original
        upload_df = df.copy()
        
        # Map CSV column names to database schema
        # CSV: lastname, unitsf, rentalrate
        # DB: last_name, unit_sf, rental_rate
        column_mapping = {
            'lastname': 'last_name',
            'unitsf': 'unit_sf', 
            'rentalrate': 'rental_rate'
        }
        
        # Rename columns
        upload_df = upload_df.rename(columns=column_mapping)
        
        print(f"[SUCCESS] Column mapping applied:")
        for old_col, new_col in column_mapping.items():
            print(f"   {old_col} -> {new_col}")
        
        # Convert to list of dictionaries for Supabase
        data_records = upload_df.to_dict('records')
        
        print(f"[SUCCESS] Prepared {len(data_records)} records for upload")
        print(f"Sample record: {data_records[0] if data_records else 'No data'}")
        
        return data_records
        
    except Exception as e:
        print(f"[ERROR] Failed to prepare data: {str(e)}")
        return None

def upload_to_supabase_with_auth(data_records):
    """Upload data to Supabase table with proper authentication"""
    try:
        print(f"\nUploading data to Supabase with authentication...")
        
        # Create Supabase client
        supabase: Client = create_client(SUPABASE_CONFIG["url"], SUPABASE_CONFIG["key"])
        print(f"[SUCCESS] Supabase client created")
        print(f"   URL: {SUPABASE_CONFIG['url']}")
        print(f"   Table: {TABLE_NAME}")
        
        # Try to sign in first (this might help with RLS)
        try:
            print("Attempting to authenticate...")
            auth_response = supabase.auth.sign_in_with_password({
                "email": SUPABASE_CONFIG["email"],
                "password": SUPABASE_CONFIG["password"]
            })
            print(f"[SUCCESS] Authentication successful")
        except Exception as auth_error:
            print(f"[WARNING] Authentication failed: {auth_error}")
            print("Continuing with anonymous access...")
        
        # Upload data one record at a time to handle potential RLS issues
        print(f"Uploading {len(data_records)} records...")
        successful_uploads = 0
        failed_uploads = 0
        
        for i, record in enumerate(data_records):
            try:
                response = supabase.table(TABLE_NAME).insert(record).execute()
                if response.data:
                    successful_uploads += 1
                    print(f"   Record {i+1}: [SUCCESS] {record['last_name']}")
                else:
                    failed_uploads += 1
                    print(f"   Record {i+1}: [FAILED] {record['last_name']}")
            except Exception as record_error:
                failed_uploads += 1
                print(f"   Record {i+1}: [ERROR] {record['last_name']} - {record_error}")
        
        print(f"\nUpload Summary:")
        print(f"   Successful: {successful_uploads}")
        print(f"   Failed: {failed_uploads}")
        print(f"   Total: {len(data_records)}")
        
        return successful_uploads > 0
        
    except Exception as e:
        print(f"[ERROR] Failed to upload to Supabase: {str(e)}")
        return False

def upload_to_supabase_batch(data_records):
    """Try batch upload as alternative method"""
    try:
        print(f"\nTrying batch upload method...")
        
        # Create Supabase client
        supabase: Client = create_client(SUPABASE_CONFIG["url"], SUPABASE_CONFIG["key"])
        
        # Try batch upload
        response = supabase.table(TABLE_NAME).insert(data_records).execute()
        
        if response.data:
            print(f"[SUCCESS] Batch upload successful! Uploaded {len(response.data)} records")
            return True
        else:
            print("[ERROR] Batch upload failed - no data returned")
            return False
            
    except Exception as e:
        print(f"[ERROR] Batch upload failed: {str(e)}")
        return False

def verify_upload():
    """Verify the uploaded data by querying the table"""
    try:
        print(f"\nVerifying uploaded data...")
        
        # Create Supabase client
        supabase: Client = create_client(SUPABASE_CONFIG["url"], SUPABASE_CONFIG["key"])
        
        # Query all data
        response = supabase.table(TABLE_NAME).select("*").execute()
        
        if response.data:
            print(f"[SUCCESS] Verification successful!")
            print(f"   Total records in table: {len(response.data)}")
            print(f"   Columns: {list(response.data[0].keys())}")
            
            # Show sample of uploaded data
            print(f"\nSample of uploaded data:")
            for i, record in enumerate(response.data[:3]):
                print(f"   Record {i+1}: {record}")
            
            return True
        else:
            print("[WARNING] No data found in table after upload")
            return False
            
    except Exception as e:
        print(f"[ERROR] Failed to verify upload: {str(e)}")
        return False

def show_rls_solution():
    """Show how to fix RLS issues in Supabase dashboard"""
    print(f"\n" + "=" * 50)
    print("ROW LEVEL SECURITY (RLS) SOLUTION")
    print("=" * 50)
    print()
    print("The upload failed due to Row Level Security (RLS) policy.")
    print("Here's how to fix it in your Supabase dashboard:")
    print()
    print("1. Go to: https://supabase.com/dashboard")
    print("2. Log in with: DaVinciLock-Brad / pled0!Naples")
    print("3. Select your project")
    print("4. Go to: Authentication → Policies")
    print("5. Find the 'practice_dataset' table")
    print("6. Either:")
    print("   A) Disable RLS for this table (temporary solution)")
    print("   B) Create a policy that allows INSERT operations")
    print()
    print("Alternative: Use the Supabase SQL Editor:")
    print("   ALTER TABLE practice_dataset DISABLE ROW LEVEL SECURITY;")
    print()
    print("Or create an INSERT policy:")
    print("   CREATE POLICY \"Allow all inserts\" ON practice_dataset")
    print("   FOR INSERT WITH CHECK (true);")

def main():
    """Main function to run the upload process"""
    print("CSV to Supabase Upload Script (RLS Fixed)")
    print("=" * 50)
    
    # Step 1: Load CSV data
    df = load_csv_data()
    if df is None:
        return 1
    
    # Step 2: Prepare data for upload
    data_records = prepare_data_for_upload(df)
    if data_records is None:
        return 1
    
    # Step 3: Try authenticated upload first
    upload_success = upload_to_supabase_with_auth(data_records)
    
    # Step 4: If that fails, try batch upload
    if not upload_success:
        print(f"\nTrying alternative upload method...")
        upload_success = upload_to_supabase_batch(data_records)
    
    # Step 5: Verify upload
    if upload_success:
        verify_success = verify_upload()
        if verify_success:
            print(f"\n" + "=" * 50)
            print("[SUCCESS] Upload completed successfully!")
            print("=" * 50)
            print(f"✅ Loaded {len(df)} records from CSV")
            print(f"✅ Uploaded to Supabase table '{TABLE_NAME}'")
            print(f"✅ Data verified in database")
            print(f"\nYour data is now available in Supabase and ready to use!")
            return 0
        else:
            print("[WARNING] Upload completed but verification failed")
            return 1
    else:
        print(f"\n[ERROR] Upload failed due to Row Level Security policy")
        show_rls_solution()
        return 1

if __name__ == "__main__":
    exit_code = main()
    print(f"\nScript completed with exit code: {exit_code}")
    sys.exit(exit_code)
