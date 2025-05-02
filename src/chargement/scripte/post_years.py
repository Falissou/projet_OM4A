from datetime import datetime
import json
from src.chargement.utils.fonction_utils import FonctionUtils
from src.chargement.utils.sauvegarde import save_results
from src.chargement.config import BASE_URL, USERNAME, PASSWORD

# Configuration des années
START_YEAR = 1900
END_YEAR = 2050

def generate_years_data():
    """Génère la liste des années à créer"""
    return [{"year": year} for year in range(START_YEAR, END_YEAR + 1)]

def main():
    # Initialisation du client API
    client = FonctionUtils()
    
    print(f"🔐 Authentification sur {BASE_URL}...")
    if not client.authenticate():
        print("❌ Arrêt suite à l'échec d'authentification")
        return

    # Préparation des données
    years_data = generate_years_data()
    print(f"🚀 Lancement de la création de {len(years_data)} années ({START_YEAR}-{END_YEAR})...")

    # Création des années
    results = client.batch_create("years", years_data)
    
    # Sauvegarde des résultats
    save_results(results, "years_")
    
    # Rapport final
    print(f"\n📊 Résultats : {len(results['success'])} succès | {len(results['errors'])} erreurs")

if __name__ == "__main__":
    main()