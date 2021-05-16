from sabi.api_client import ApiClient

class Clients(ApiClient):
    headers = None

    def __init__(self, api_key, host = None):
        version = 'v1'
        base = f'{version}/clients'
        super().__init__(api_key, base, host)
    
    def company_integration(self, company_integration_hash_id):
        response = self.get('company_integrations',company_integration_hash_id)
        return response

    def integrations(self, type):
        response = self.get('integrations',type)
        return response
