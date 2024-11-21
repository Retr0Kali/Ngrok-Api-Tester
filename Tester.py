##coded by Retr0

import requests

def print_banner():
    cat_banner = r"""
      |\---/|
      | o_o |      === ngrok API Key Tester ===
       \_^_/       Validate your ngrok API keys with ease!
    """
    print(cat_banner)

def test_ngrok_api_key(api_key):
    url = "https://api.ngrok.com/api_keys"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Ngrok-Version": "2"
    }

    try:
        # Make the GET request to list API keys
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print("[+] API key is valid!")
            keys = response.json().get('keys', [])
            print(f"Found {len(keys)} API keys associated with this account.")
            for i, key in enumerate(keys, start=1):
                print(f"  {i}. ID: {key['id']} - Description: {key['description']}")
            return True
        elif response.status_code == 401:
            print("[-] API key is invalid.")
        else:
            print(f"[-] Unexpected response: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error: {e}")

    return False

if __name__ == "__main__":
    print_banner()
    api_key = input("Enter your ngrok API key: ").strip()
    test_ngrok_api_key(api_key)
