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


class PhoneNumberTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .phone_numbers(sid="PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2010-12-10T17:27:34Z",
                "date_updated": "2015-10-09T11:36:32Z",
                "friendly_name": "(415) 867-5309",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "phone_number": "+14158675309",
                "api_version": "2010-04-01",
                "voice_caller_id_lookup": null,
                "voice_url": "",
                "voice_method": "POST",
                "voice_fallback_url": null,
                "voice_fallback_method": null,
                "status_callback": "",
                "status_callback_method": "POST",
                "voice_application_sid": null,
                "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sms_url": "",
                "sms_method": "POST",
                "sms_fallback_url": "",
                "sms_fallback_method": "POST",
                "sms_application_sid": "",
                "address_requirements": "none",
                "beta": false,
                "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "capabilities": {
                    "voice": true,
                    "sms": true,
                    "mms": true
                },
                "links": {
                    "phone_number": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .phone_numbers(sid="PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .phone_numbers(sid="PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .phone_numbers(sid="PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .phone_numbers.create(phone_number_sid="PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        values = {
            'PhoneNumberSid': "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        }
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2010-12-10T17:27:34Z",
                "date_updated": "2015-10-09T11:36:32Z",
                "friendly_name": "(415) 867-5309",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "phone_number": "+14158675309",
                "api_version": "2010-04-01",
                "voice_caller_id_lookup": null,
                "voice_url": "",
                "voice_method": "POST",
                "voice_fallback_url": null,
                "voice_fallback_method": null,
                "status_callback": "",
                "status_callback_method": "POST",
                "voice_application_sid": null,
                "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sms_url": "",
                "sms_method": "POST",
                "sms_fallback_url": "",
                "sms_fallback_method": "POST",
                "sms_application_sid": "",
                "address_requirements": "none",
                "beta": false,
                "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "capabilities": {
                    "voice": true,
                    "sms": true,
                    "mms": true
                },
                "links": {
                    "phone_number": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .phone_numbers.create(phone_number_sid="PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        self.assertIsNotNone(actual)

    def test_read_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                   .phone_numbers.read()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers?PageSize=1&Page=0",
                    "key": "phone_numbers",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 1,
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers?PageSize=1&Page=0"
                },
                "phone_numbers": [
                    {
                        "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2010-12-10T17:27:34Z",
                        "date_updated": "2015-10-09T11:36:32Z",
                        "friendly_name": "(415) 867-5309",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "phone_number": "+14158675309",
                        "api_version": "2010-04-01",
                        "voice_caller_id_lookup": null,
                        "voice_url": "",
                        "voice_method": "POST",
                        "voice_fallback_url": null,
                        "voice_fallback_method": null,
                        "status_callback": "",
                        "status_callback_method": "POST",
                        "voice_application_sid": null,
                        "trunk_sid": "TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sms_url": "",
                        "sms_method": "POST",
                        "sms_fallback_url": "",
                        "sms_fallback_method": "POST",
                        "sms_application_sid": "",
                        "address_requirements": "none",
                        "beta": false,
                        "url": "https://trunking.twilio.com/v1/Trunks/TKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "capabilities": {
                            "voice": true,
                            "sms": true,
                            "mms": true
                        },
                        "links": {
                            "phone_number": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                        }
                    }
                ]
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .phone_numbers.read()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers?PageSize=1&Page=0",
                    "key": "phone_numbers",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 1,
                    "previous_page_url": null,
                    "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers?PageSize=1&Page=0"
                },
                "phone_numbers": []
            }
            '''
        ))
        
        actual = self.client.trunking.v1.trunks(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .phone_numbers.read()
        
        self.assertIsNotNone(actual)
