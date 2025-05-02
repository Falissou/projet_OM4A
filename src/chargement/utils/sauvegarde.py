from datetime import datetime
import json

def save_results(results, prefix=""):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}results_{timestamp}.json"
    
    with open(filename, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Fichier sauvegardé : {filename}")
    return filename