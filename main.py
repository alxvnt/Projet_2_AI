import os
from dotenv import load_dotenv

# Charge les variables d'environnement de .env dans le systeme Windows
load_dotenv()

def main():
    api_key = os.getenv("API_KEY")
    for i in range (9):
        print(api_key)

if __name__ == "__main__":
    main()
