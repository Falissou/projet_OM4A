import requests
import time
from datetime import datetime
from src.chargement.utils.fonction_utils import FonctionUtils
from src.chargement.config import BASE_URL

class DatabaseCleaner:
    def __init__(self):
        self.client = FonctionUtils()
        
    def delete_all_records(self, endpoint):
        """Supprime tous les enregistrements d'une table"""
        if not self.client.authenticate():
            return False

        try:
            # Récupération des IDs
            response = self.client.get_all(endpoint)
            if not response:
                return False

            records = response.json()
            print(f"🔍 {len(records)} enregistrements trouvés dans {endpoint}")

            # Suppression
            success_count = 0
            for record in records:
                if self.client.delete(f"{endpoint}/{record['id']}"):
                    success_count += 1
                time.sleep(0.1)  # Pause anti-surcharge

            print(f"✅ {success_count}/{len(records)} suppressions réussies")
            return True

        except Exception as e:
            print(f"🚨 Erreur critique: {str(e)}")
            return False

def main():
    cleaner = DatabaseCleaner()
    
    # Liste de toutes les tables à vider
    TABLES = [
        "years"
        # Ajoutez d'autres tables ici
    ]

    print("⚠️ ATTENTION: Cette opération va vider les tables de la base!")
    
    for table in TABLES:
        print(f"\n🧹 Nettoyage de la table: {table}")
        cleaner.delete_all_records(table)

if __name__ == "__main__":
    main()