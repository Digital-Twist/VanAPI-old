"""
ngpvan_api.people
~~~~~~~~~~~~~~~
This module contains people-related API calls.
"""

import json
from ngpvan_api import base

class NGPVANPeopleAPI(base.NGPVANAPI):

    def get_person(self, mycampaign_id, expand='', params={}):
        """Gets a single person matching mycampaign_id."""

        params['$expand'] = expand
        response = self.client.get(
            '%speople/%s' % (self.base_url, mycampaign_id),
            params = params
        )
        return {'results': [response], 'person': response.json()}

    def get_or_create_person(self, first_name, last_name, person_data={}):
        """
        Gets existing person matching person_data, or creates new
        person from person_data if no match is found.
        """

        person_data['firstName'] = first_name
        person_data['lastName'] = last_name
        result = self.client.post(
            '%s/people/findOrCreate' % (self.base_url),
            data=json.dumps(person_data)
        )
        return {'results': [result], 'person': result.json()}
    
    def get_person_notes(self, vanid, params={}):
        """
        Params
        -------
            text: (str)	Required; the content of the description of the Person.
            isViewRestricted: (str) Required; set to true if the note should be restricted only to certain users within the current context; set to false if the note may be viewed by any user in the current context.
            category: (object) Optional; if specified, must be an object whose noteCategoryId corresponds to a Note Category which may be applied to People, and which is available at ,
        """
        params['$expand'] = expand
        response = self.client.get(
            '%speople/%s/notes' % (self.base_url, vanid),
            params = params
        )
        return {'results': [response], 'person_notes': response.json()}
