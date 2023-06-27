import unittest
import requests
import json

class FlaskAPITest(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://app-scoring-heroku.herokuapp.com"


    def test_get_data(self):

        # Test de la requête GET avec une bonne clé dans l'URL
        good_key = 'proba=126367'
        response = requests.get(self.base_url + '/data?' + good_key)

        if response.status_code == 200:
            result = response.json()
            probability = result['acc']
            # Vérifier si le résultat est compris entre 0 et 1
            if 0 <= probability <= 1:
                print('Résultat valide :', probability)
            else:
                print('Résultat invalide :', probability)
        else:
            print('Erreur lors de la requête GET')

        # Test de la requête GET avec une mauvaise clé dans l'URL
        bad_key = 'proba=1263'
        response = requests.get(self.base_url + '/data?' + bad_key)
        
        if response.status_code == 400:
            result = response.json()
            # Vérifier le message d'erreur de l'API ici...
            print(result)
        else:
            print('Erreur lors de la requête GET')


    def test_post_prediction(self):

        # Test de la requête POST avec un JSON valide contenant 30 clés
        valid_data = {"Contrat": {"264838": 0.0}, "Genre": {"264838": 0.0}, "Voiture": {"264838": 0.0}, 
                      "AMT_CREDIT": {"264838": 414792.0}, "NAME_INCOME_TYPE": {"264838": 3.0}, 
                      "NAME_EDUCATION_TYPE": {"264838": 4.0}, "NAME_HOUSING_TYPE": {"264838": 1.0}, 
                      "REGION_POPULATION_RELATIVE": {"264838": 0.010966}, "DAYS_REGISTRATION": {"264838": -13269.0}, 
                      "DAYS_ID_PUBLISH": {"264838": -4578.0}, "FLAG_EMP_PHONE": {"264838": 0.0}, 
                      "FLAG_WORK_PHONE": {"264838": 0.0}, "FLAG_PHONE": {"264838": 0.0}, "OCCUPATION_TYPE": {"264838": 18.0}, 
                      "REGION_RATING_CLIENT_W_CITY": {"264838": 2.0}, "REG_REGION_NOT_WORK_REGION": {"264838": 0.0}, 
                      "REG_CITY_NOT_LIVE_CITY": {"264838": 0.0}, "REG_CITY_NOT_WORK_CITY": {"264838": 0.0}, 
                      "LIVE_CITY_NOT_WORK_CITY": {"264838": 0.0}, "ORGANIZATION_TYPE": {"264838": 57.0}, 
                      "DEF_30_CNT_SOCIAL_CIRCLE": {"264838": 1.0}, "DAYS_LAST_PHONE_CHANGE": {"264838": -1157.0}, 
                      "Age": {"264838": 61.983561643835614}, "Duree": {"264838": 22.54243091220347}, 
                      "Anciennete": {"264838": 0.0}, "count": {"264838": 1.0}, "max": {"264838": -86.0}, 
                      "ANCxCRED": {"264838": 0.0}, "ANC_par_CRED": {"264838": 0.0}, "Anc_Age": {"264838": 0.0}
                      }
  

        response = requests.post(self.base_url + '/prediction', json=valid_data)
        
        if response.status_code == 200:
            result = response.json()
            probability = result['probability']

            # Vérifier la réponse de l'API ici...
            print(result)
        else:
            print('Erreur lors de la requête POST')

        # Test de la requête POST avec un JSON invalide (moins de 30 clés)
        invalid_data = {"Contrat": {"264838": 0.0}, 
                        "Genre": {"264838": 0.0} }

        response = requests.post(self.base_url + '/prediction', json=invalid_data)
        
        if response.status_code == 400:
            result = response.json()
            # Vérifier le message d'erreur de l'API ici...
            print(result)
        else:
            print('Erreur lors de la requête POST')


if __name__ == "__main__":
    unittest.main()
