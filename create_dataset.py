"""
Script to create the practice dataset for data science work
Creates a dataset with 12 rows and 3 columns as specified
"""

import pandas as pd
import numpy as np
import random

def create_practice_dataset():
    """
    Create a practice dataset with:
    - 12 rows
    - 3 columns: 'last name', 'unit sf', 'rental rate'
    - Random last names
    - Unit sf: integers divisible by 10, range 50-200
    - Rental rate: floats 50-250 with correlation to unit sf
    """
    
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # Sample last names
    last_names = [
        'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia',
        'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez'
    ]
    
    # Generate unit sf values (integers divisible by 10, range 50-200)
    unit_sf = np.random.choice(range(50, 201, 10), size=12, replace=False)
    
    # Generate rental rates with correlation to unit sf
    # Base rate: 50 + (unit_sf - 50) * 1.2 + some noise
    base_rate = 50 + (unit_sf - 50) * 1.2
    noise = np.random.normal(0, 15, 12)  # Add some randomness
    rental_rate = np.clip(base_rate + noise, 50, 250)  # Keep within bounds
    
    # Create DataFrame
    df = pd.DataFrame({
        'last name': last_names,
        'unit sf': unit_sf,
        'rental rate': np.round(rental_rate, 2)
    })
    
    return df

def save_dataset(df, filename='practice_dataset.csv'):
    """Save the dataset to a CSV file"""
    df.to_csv(filename, index=False)
    print(f"Dataset saved to {filename}")
    return filename

if __name__ == "__main__":
    # Create the dataset
    dataset = create_practice_dataset()
    
    # Display the dataset
    print("Practice Dataset:")
    print("=" * 50)
    print(dataset)
    print("\nDataset Info:")
    print(f"Shape: {dataset.shape}")
    print(f"Columns: {list(dataset.columns)}")
    
    # Save to CSV
    save_dataset(dataset)
    
    # Show basic statistics
    print("\nBasic Statistics:")
    print(dataset.describe())

