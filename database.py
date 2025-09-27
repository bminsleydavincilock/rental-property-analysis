"""
Database connection module using Supabase client
Updated to use working Supabase client instead of SQLAlchemy
"""

import pandas as pd
import streamlit as st
from supabase import create_client, Client
from config import SUPABASE_CONFIG, TABLE_NAME

@st.cache_resource
def get_supabase_client():
    """Create and cache Supabase client"""
    try:
        supabase: Client = create_client(SUPABASE_CONFIG["url"], SUPABASE_CONFIG["key"])
        return supabase
    except Exception as e:
        st.error(f"Error creating Supabase client: {str(e)}")
        return None

@st.cache_data(ttl=300)  # Cache for 5 minutes
def load_data_from_database():
    """Load data from Supabase using Supabase client"""
    try:
        supabase = get_supabase_client()
        if supabase is None:
            return None
        
        # Query the data from Supabase
        response = supabase.table(TABLE_NAME).select("*").execute()
        
        if not response.data:
            st.warning("No data found in the Supabase table")
            return None
        
        # Convert to DataFrame
        df = pd.DataFrame(response.data)
        
        if df.empty:
            st.warning("No data found in the database")
            return None
        
        # Rename columns to match expected format (with spaces)
        column_mapping = {
            'last_name': 'lastname',
            'unit_sf': 'unitsf', 
            'rental_rate': 'rentalrate'
        }
        df = df.rename(columns=column_mapping)
        
        # Add calculated columns
        df['rate_per_sf'] = df['rentalrate'] / df['unitsf']
        df['size_category'] = pd.cut(df['unitsf'], 
                                   bins=[0, 100, 150, 200], 
                                   labels=['Small (<=100)', 'Medium (101-150)', 'Large (151-200)'])
        
        return df
        
    except Exception as e:
        st.error(f"Error loading data from Supabase: {str(e)}")
        return None

def load_data_fallback():
    """Fallback to CSV if database connection fails"""
    try:
        df = pd.read_csv('practice_dataset.csv')
        
        # CSV already has the correct column names: lastname, unitsf, rentalrate
        # No renaming needed - use them directly
        
        df['rate_per_sf'] = df['rentalrate'] / df['unitsf']
        df['size_category'] = pd.cut(df['unitsf'], 
                                   bins=[0, 100, 150, 200], 
                                   labels=['Small (<=100)', 'Medium (101-150)', 'Large (151-200)'])
        return df
    except FileNotFoundError:
        st.error("Neither database nor CSV file found!")
        return None

# Note: Table creation and data insertion are now handled by the upload scripts
# This module focuses on data loading for the Streamlit app

def load_data():
    """Main function to load data - tries Supabase first, then CSV"""
    # Try to load from Supabase first
    df = load_data_from_database()
    
    if df is not None:
        st.success("✅ Data loaded from Supabase database")
        return df
    else:
        st.warning("⚠️ Supabase connection failed, falling back to CSV file")
        return load_data_fallback()