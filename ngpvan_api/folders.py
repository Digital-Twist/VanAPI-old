import json
from ngpvan_api import base

class NGPVANFoldersAPI(base.NGPVANAPI):
    def get_folders(self, params={}, page_number=False):
        """List folders the API user has access to retreive"""

        return self.get_page_or_pages('folders', page_number, params)

    def get_folder(self, folderId):

        response = self.client.get(
            '%folders/%s' % (self.base_url, folders)
        )
        return {'results': [response], 'Folder': response.json()}
