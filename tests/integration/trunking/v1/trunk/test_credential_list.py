# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.exceptions import TwilioException
from twilio.http.response import Response


class CredentialListTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .credentials_lists(sid="CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Wed, 11 Sep 2013 17:51:38 -0000",
                "date_updated": "Wed, 11 Sep 2013 17:51:38 -0000",
                "friendly_name": "Low Rises",
                "sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .credentials_lists(sid="CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .credentials_lists(sid="CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .credentials_lists(sid="CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .credentials_lists.create(credential_list_sid="CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        values = {
            'CredentialListSid': "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        }
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Wed, 11 Sep 2013 17:51:38 -0000",
                "date_updated": "Wed, 11 Sep 2013 17:51:38 -0000",
                "friendly_name": "Low Rises",
                "sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .credentials_lists.create(credential_list_sid="CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertIsNotNone(actual)

    def test_read_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .credentials_lists.read()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "credential_lists": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Wed, 11 Sep 2013 17:51:38 -0000",
                        "date_updated": "Wed, 11 Sep 2013 17:51:38 -0000",
                        "friendly_name": "Low Rises",
                        "sid": "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists/CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "credential_lists"
                }
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .credentials_lists.read()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "credential_lists": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "credential_lists"
                }
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .credentials_lists.read()
        
        self.assertIsNotNone(actual)
