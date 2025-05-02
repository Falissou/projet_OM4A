import requests
import time
from datetime import datetime
from src.chargement.config import BASE_URL, USERNAME, PASSWORD

class FonctionUtils:
    def __init__(self):
        self.token = None
    
    def authenticate(self):
        try:
            response = requests.post(
                f"{BASE_URL}/authenticate",
                json={"username": USERNAME, "password": PASSWORD},
                verify=False,
                timeout=10
            )
            self.token = response.json()["id_token"]
            return True
        except Exception as e:
            print(f"❌ Échec authentification : {str(e)}")
            return False
    
    def create_entity(self, endpoint, data, delay=0.2):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        
        try:
            response = requests.post(
                f"{BASE_URL}/{endpoint}",
                headers=headers,
                json=data,
                verify=False,
                timeout=5
            )
            time.sleep(delay)
            return response
        except Exception as e:
            print(f"🚨 Erreur réseau : {str(e)}")
            return None

    def batch_create(self, endpoint, entities):
        results = {"success": [], "errors": []}
        for entity in entities:
            response = self.create_entity(endpoint, entity)
            if response and response.status_code == 201:
                results["success"].append({
                    "id": response.json().get("id"),
                    "data": entity
                })
                print(f"✅ {entity.get('name', entity.get('code'))} créé")
            else:
                error = {
                    "data": entity,
                    "status": getattr(response, 'status_code', 'N/A'),
                    "error": response.text if response else "Erreur réseau"
                }
                results["errors"].append(error)
                print(f"⚠️ Erreur sur {entity.get('name', entity.get('code'))}")
        return results
    
    def _get_headers(self):
        """Retourne les headers avec le token JWT"""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
    
    def get_all(self, endpoint):
        """Récupère tous les enregistrements d'une table"""
        try:
            return requests.get(
                f"{BASE_URL}/{endpoint}",
                headers=self._get_headers(),
                verify=False,
                timeout=30
            )
        except Exception as e:
            print(f"❌ Erreur GET {endpoint}: {str(e)}")
            return None
    
    def delete(self, endpoint):
        """Supprime un enregistrement"""
        try:
            response = requests.delete(
                f"{BASE_URL}/{endpoint}",
                headers=self._get_headers(),
                verify=False,
                timeout=5
            )
            return response.status_code == 204
        except Exception as e:
            print(f"❌ Erreur DELETE {endpoint}: {str(e)}")
            return False
