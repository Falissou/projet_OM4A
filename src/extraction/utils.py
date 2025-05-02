import requests
import pandas as pd

# Clé API EIA optenu sur le site de sur le site
api_key = "b1Ql7Dg3yAzZ0ZJIK9MqRBUtDBmO2QzsIP1egCIZ"

# Definition de la fonction pour extraire les données via l'API en DataFrame
def fetch_eia_data(api_key, base_url):
    """
    Récupère les données de l'API EIA et les convertit en DataFrame pandas.

    Parameters:
        api_key (str): Clé API pour accéder à l'EIA.
        base_url (str): URL de l'API sans la clé API.

    Returns:
        pandas.DataFrame or None: DataFrame contenant les données si succès, None sinon.
    """
    # Ajouter la clé API à l'URL
    url = f"{base_url}&api_key={api_key}"

    try:
        # Effectuer la requête GET
        response = requests.get(url)

        # Vérifier si la requête a réussi (code 200)
        if response.status_code == 200:
            # Extraire les données JSON
            data_json = response.json()

            # Vérifier si la clé 'data' existe dans la réponse
            if 'data' in data_json['response']:
                # Convertir les données en DataFrame
                df = pd.DataFrame(data_json['response']['data'])
                print("Données importées avec succès.")
                return df
            else:
                print("Erreur : Aucune donnée trouvée dans la réponse.")
                return None
        else:
            print(f"Erreur HTTP {response.status_code} : {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
        return None
    except ValueError as e:
        print(f"Erreur lors du traitement JSON : {e}")
        return None


# Definition d'une fonction pour la concatenation des DataFrame
def concatenate_eia_data(api_key, url_list, columns_to_keep=['countryRegionName', 'period','productName','value']):
    """
    Itère sur une liste d'URLs de l'API EIA, récupère les données et les concatène verticalement.

    Parameters:
        api_key (str): Clé API pour accéder à l'EIA.
        url_list (list): Liste des URLs de l'API sans la clé API.
        columns_to_keep (list): Colonnes à conserver dans les DataFrames (par défaut : ['countryRegionName', 'period', 'value']).

    Returns:
        pandas.DataFrame or None: DataFrame concaténé contenant toutes les données si succès, None sinon.
    """
    # Liste pour stocker les DataFrames
    dataframes = []

    # Itérer sur chaque URL
    for url in url_list:
        print(f"Récupération des données pour l'URL : {url}")
        df = fetch_eia_data(api_key, url)

        # Vérifier si les données ont été récupérées
        if df is not None:
            # Sélectionner les colonnes demandées
            try:
                df = df[columns_to_keep]
                dataframes.append(df)
                print(f"Données ajoutées pour l'URL : {url}")
            except KeyError as e:
                print(f"Erreur : Une ou plusieurs colonnes {columns_to_keep} absentes pour l'URL : {url}")
                continue
        else:
            print(f"Aucune donnée récupérée pour l'URL : {url}")

    # Concaténer les DataFrames (si la liste n'est pas vide)
    if dataframes:
        concatenated_df = pd.concat(dataframes, axis=0, ignore_index=True)
        print("Concaténation réussie.")
        return concatenated_df
    else:
        print("Aucune donnée à concaténer.")
        return None