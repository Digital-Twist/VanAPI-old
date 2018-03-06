import json
from ngpvan_api import base

class NGPVANActivistCodesAPI(base.NGPVANAPI):
    def get_activistcodes(self, params={}, page_number=False):
        """List activist codes, params include name (filtering to activist codes with that name) and type (filtering by type of activist code) and statuses (Active, Inactive, Archived)"""

        return self.get_page_or_pages('activistCodes', page_number, params)

    def get_activistcode(self, activistCodeId):
        newpath='activistCodes/'+activistCodeId

        return self.get_page_or_pages(newpath)
