import json
import os
from datetime import datetime

def generate_report(output_dir: str = "data"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = os.path.join(output_dir, f"report_{timestamp}.json")
    
    data = {
        "status": "success",
        "generated_at": timestamp,
        "metrics": {
            "users": 150,
            "sales": 2500.50
        }
    }
    
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
        
    print(f"Report generated at {filepath}")
    return filepath

if __name__ == "__main__":
    generate_report()
