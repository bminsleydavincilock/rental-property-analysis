#!/usr/bin/env python3
"""
Setup script for Python data science environment
This script will install required packages for data science work
"""

import subprocess
import sys

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✓ Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"✗ Failed to install {package}")

def main():
    """Main setup function"""
    print("Setting up Python data science environment...")
    
    # Required packages
    packages = [
        "pandas",
        "numpy", 
        "jupyter",
        "matplotlib",
        "seaborn"
    ]
    
    print(f"Installing {len(packages)} packages...")
    
    for package in packages:
        install_package(package)
    
    print("\n✓ Environment setup complete!")
    print("You can now run: jupyter notebook")

if __name__ == "__main__":
    main()

