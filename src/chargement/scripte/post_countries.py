from src.utils.fonction_utils import FonctionUtils
from src.utils.sauvegarde import save_results

COUNTRIES = [
    {"code": "BJ", "name": "Benin"},
    {"code": "BF", "name": "Burkina_faso"},
    {"code": "CV", "name": "Cape_verde"},
    {"code": "CI", "name": "Cote_d_ivoire"},
    {"code": "GM", "name": "Gambia"},
    {"code": "GH", "name": "Ghana"},  # Correction: HG -> GH
    {"code": "GN", "name": "Guinea"},
    {"code": "GW", "name": "Guinea_bissau"},
    {"code": "LR", "name": "Liberia"},
    {"code": "ML", "name": "Mali"},
    {"code": "MR", "name": "Mauritania"},
    {"code": "NE", "name": "Niger"},
    {"code": "NG", "name": "Nigeria"},
    {"code": "SN", "name": "Senegal"},
    {"code": "SL", "name": "Sierra_leone"},
    {"code": "TG", "name": "Togo"}
]

def main():
    client = FonctionUtils()
    if client.authenticate():
        results = client.batch_create("countries", COUNTRIES)
        save_results(results, "countries_")
        print(f"\n📊 Résultats : {len(results['success'])} succès | {len(results['errors'])} erreurs")

if __name__ == "__main__":
    main()