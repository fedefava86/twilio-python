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


class TollFreeTestCase(IntegrationTestCase):

    def test_read_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .available_phone_numbers(country_code="US") \
                                 .toll_free.read()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/TollFree.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "available_phone_numbers": [
                    {
                        "address_requirements": "none",
                        "beta": false,
                        "capabilities": {
                            "MMS": true,
                            "SMS": true,
                            "voice": true
                        },
                        "friendly_name": "(800) 100-0052",
                        "iso_country": "US",
                        "lata": null,
                        "latitude": null,
                        "longitude": null,
                        "phone_number": "+18001000052",
                        "postal_code": null,
                        "rate_center": null,
                        "region": null
                    }
                ],
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/TollFree.json?PageSize=1"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .available_phone_numbers(country_code="US") \
                                      .toll_free.read()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "available_phone_numbers": [],
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/TollFree.json?PageSize=1"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .available_phone_numbers(country_code="US") \
                                      .toll_free.read()
        
        self.assertIsNotNone(actual)
