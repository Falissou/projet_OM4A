Projet OM4A

Ce fichier présente le projet OM4A dans son ensemble en termes d'organisation et de fichiers relatifs. 
Le projet, nommé PROJET_OMA4, vise à gérer, traiter et charger des données, principalement extraites de divers sources comme site web et base de données

Description :
Le projet OM4A est une initiative visant à collecter, transformer et charger des données énergétiques brutes dans une base de données pour une analyse ultérieure. 
Il inclut des scripts d'extraction à partir d'API, des notebooks pour le traitement des données, et des utilitaires pour la gestion des datasets.

Prérequis :
Avant de commencer, assurez-vous d'avoir les éléments suivants installés :
- Python 3.11 ou version supérieure
- Bibliothèques Python nécessaires (voir requirements.txt pour la liste complète)
- Environnement virtuel (optionnel mais recommandé)

Utilisation :
  1- Extraction des données :
    - Utilisez les notebooks dans src/extraction/ (par exemple, extraction_prod_elect.ipynb) pour extraire les données brutes à partir d'API a l’exemple de celle de l'EIA.
    - Les données extraites sont stockées dans data/raw/.
  2- Transformation des données :
    - Ouvrez les notebooks dans src/transformation/ (par exemple, transformation_prod_elect.ipynb) pour nettoyer et transformer les données.
    - Les données transformées sont sauvegardées dans data/processed/.
  3- Chargement dans la base de données :
    - Exécutez les scripts dans src/chargement/ (par exemple, post_fuels.py) pour charger les données transformées dans une base de données.
  4- Vérification :
    - Consultez les fichiers JSON (par exemple, fuels_results_20250428_103453.json) pour les résultats intermédiaires.

Fichiers et dossiers :
 - data/ : Contient toutes les données du projet.
    - data_visu/ : Stocke les datasets nettoyés et prêts à être la visualisation via Power BI.
        - etc.
    - processed/ : Stocke les datasets nettoyés et prêts à être chargés dans une base de données.
        - consom_elect_processed.xlsx, 
        - prod_elect_processed.xlsx 
        - etc : Données transformées.
    - raw/ : Contient les datasets bruts extraits de diverses sources.
        - consom_elect_fromEIA.xlsx, 
        - prod_elect_fromEIA.xlsx, 
        - Data_from_CMP.xlsx 
        - etc : Données brutes.
 - src/ : Contient l'ensemble des fichiers relatifs à l'extraction, la transformation et le chargement.
    - chargement/ : Méthodes, fonctions, scripts et utilitaires pour charger les données dans une base de données.
        - clear_table.py, post_countries.py, etc. : Scripts de chargement.
        - utils/ : Fonctions utilitaires (par exemple, fonction_utils.py, sauvegarde.py).
        - config.py : Fichier de configuration.
    - extraction/ : Notebooks et utilitaires pour extraire les données de diverses sources (API, fichiers, etc.).
        - extraction_consom_elect.ipynb, extraction_prod_elect.ipynb : Notebooks d'extraction.
        - utils.py : Utilitaires d'extraction.
    - transformation/ : Notebooks pour transformer les données brutes en données exploitables.
        - transformation_capa_prod.ipynb, 
        - transformation_consom_elect.ipynb, 
        - transformation_prod_elect.ipynb 
        - etc (Notebooks de transformation)
 - venv/ : Environnement virtuel Python pour isoler les dépendances.
 - requirements.txt : Liste des dépendances Python nécessaires.

Contributeurs : 
    - Falissou AMBOUSSIDI - Développeur principal (Stagiaire Data Scientist)
    - Sébastien AHMANY DAN-BAIBE (Modélisateur)

Contact:
Pour toute question ou suggestion, contactez falissouamboussidi@esp.sn ou ouvrez une issue sur le dépôt GitHub.

