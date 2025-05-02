from src.utils.fonction_utils import FonctionUtils
from src.utils.sauvegarde import save_results

FUELS = [
    {"name": "power"},
    {"name": "gas"},
    {"name": "coal"},
    {"name": "oil"}
]

def main():
    client = FonctionUtils()
    if client.authenticate():
        results = client.batch_create("fuels", FUELS)
        save_results(results, "fuels_")
        print(f"\n📊 Résultats : {len(results['success'])} succès | {len(results['errors'])} erreurs")

if __name__ == "__main__":
    main()