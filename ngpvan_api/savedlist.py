import json
from ngpvan_api import base

class NGPVANSavedListsAPI(base.NGPVANAPI):
    def get_savedlists(self, params={}, page_number=False):
        """Retrieves metadata about available Saved Lists. The list of people in a 
        Saved List is not available via this endpoint.
        Potential Params:
          folderId (int): If indicated, retrieve only Saved Lists from this .
          maxDoorCount (int): If indicated, retrieve only Saved Lists containing this number of doors or fewer.
          maxPeopleCount (int): If indicated, retrieve only Saved Lists containing this number of people or fewer.
        """

        return self.get_page_or_pages('savedLists', page_number, params)

    def get_savedlist(self, savedListId):

        response = self.client.get(
            '%savedLists/%s' % (self.base_url, savedLists)
        )
        return {'results': [response], 'Saved List': response.json()}
