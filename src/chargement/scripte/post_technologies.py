from src.utils.fonction_utils import FonctionUtils
from src.utils.sauvegarde import save_results


TECHNOLOGIES = [
    {"name": "p_solar", "category": "RENEWABLE"},
    {"name": "p_nuclear", "category": "THERMAL"},
    {"name": "p_wind", "category": "RENEWABLE"},
    {"name": "p_hydro", "category": "RENEWABLE"},
    {"name": "p_oil", "category": "THERMAL"},
    {"name": "p_coal", "category": "THERMAL"},
    {"name": "p_gas", "category": "THERMAL"},
    {"name": "p_biomass", "category": "RENEWABLE"}
]

def main():
    client = FonctionUtils()
    if client.authenticate():
        results = client.batch_create("technologies", TECHNOLOGIES)
        save_results(results, "technologies_")
        print(f"\n📊 Résultats : {len(results['success'])} succès | {len(results['errors'])} erreurs")

if __name__ == "__main__":
    main()