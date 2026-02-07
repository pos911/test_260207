#!/usr/bin/env python3
"""
Periodic script that runs via GitHub Actions.
This template fetches data and logs a timestamp.
"""

import requests
from datetime import datetime

def main():
    """Main function to execute periodic task."""
    print(f"Script started at: {datetime.utcnow().isoformat()}")
    
    try:
        # Example: Fetch data from a public API
        response = requests.get("https://api.github.com/zen", timeout=10)
        
        if response.status_code == 200:
            print(f"GitHub Zen: {response.text}")
        else:
            print(f"Error: Received status code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    print(f"Script completed at: {datetime.utcnow().isoformat()}")

if __name__ == "__main__":
    main()
