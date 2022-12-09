import requests, json

class APITemplateIO:
    def __init__(self, api_key):
        self.api_key = api_key

    def download(self, download_url, save_to):
        with open(save_to, 'wb') as output:
            response_get = requests.get( download_url, stream=True)
            for chunck in response_get.iter_content():
                output.write(chunck)

    def create_pdf(self, template_id, data, pdf_file_path):
        return self.create(template_id, data, pdf_file_path, None)

    def create_image(self, template_id, data, jpeg_file_path, png_file_path):
        return self.create(template_id, data, jpeg_file_path, png_file_path)

    def create(self, template_id, data, save_to_1, save_to_2):
        response = requests.post(
            F"https://api.apitemplate.io/v1/create?template_id={template_id}",
            headers = {"X-API-KEY": F"{self.api_key}"},
            json = data
        )

        resp_json = json.loads(response.content)
        if resp_json['status'] == 'success':
            self.download(resp_json['download_url'], save_to_1)

            if 'download_url_png' in resp_json and save_to_2 is not None:
                self.download(resp_json['download_url_png'], save_to_2)

            return True

        return False

    def get_account_information(self):
        response = requests.get(
            F"https://api.apitemplate.io/v1/account-information",
            headers = {"X-API-KEY": F"{self.api_key}"}
        )

        resp_json = json.loads(response.content)
        if resp_json['status'] == 'success':
            return resp_json

        return None


    def list_templates(self):
        response = requests.get(
            F"https://api.apitemplate.io/v1/list-templates",
            headers = {"X-API-KEY": F"{self.api_key}"}
        )
        print(response.content)
        resp_json = json.loads(response.content)

        return resp_json
