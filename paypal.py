import requests

def test_account(username, password):
    # Construire une URL pour envoyer une requête de connexion
    login_url = "https://fake-paypal.com/signin"
    # Construire un objet de données de connexion avec le nom d'utilisateur et le mot de passe
    login_data = {"username": username, "password": password}
    # Envoyer une requête POST avec les données de connexion
    response = requests.post(login_url, data=login_data)
    # Analyser la réponse pour déterminer si le compte est valide ou non
    if response.status_code == 200:
        return f"Compte valide: {username}"
    else:
        return f"Compte non valide: {username}"

# Tester un compte fictif
username = "test_user"
password = "password123"
result = test_account(username, password)
print(result)
