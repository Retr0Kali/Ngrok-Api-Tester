



![photo_2024-10-30_15-50-11](https://github.com/user-attachments/assets/813f4c3d-aa4c-4615-85a0-dca5e96a2c61)





# ngrok API Key Tester

A simple Python script that allows you to test if your **ngrok API key** is valid. The script uses ngrok's [API](https://ngrok.com/docs/api/resources/api-keys/) to validate the API key and list associated API keys.

## Features

- **API Key Validation**: Verifies whether the provided ngrok API key is valid by querying ngrok's `api_keys` endpoint.
- **List Associated Keys**: Displays all API keys linked to the account for further insight.
- **Error Handling**: Displays detailed error messages for invalid keys or issues with the request.
- **Fun ASCII Cat Banner**: Enjoy a fun cat graphic when starting the tool!

## Requirements

- Python 3.x
- `requests` library

You can install the required library with:

```bash
pip install requests
