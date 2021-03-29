from hello_world.formater import plain_text_upper_case
from hello_world.formater import plain_text_lower_case
from hello_world.formater import plain_text
from hello_world.formater import format_to_json
from hello_world.formater import format_to_xml
import unittest
import json
import xml.etree.cElementTree as ET
import re


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_plain_lowercase(self):
        r = plain_text_lower_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.islower())
        self.assertTrue(msg.islower())

    def test_plain_case(self):
        r = plain_text("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name)
        self.assertTrue(msg)

    def test_msg_with_output_json(self):
        r = format_to_json("wwww", "EEEMSG")
        JSON_Result = json.loads(r)
        JSON_Expected = {"imie": "EEEMSG", "msg": "wwww"}
        self.assertDictEqual(JSON_Result, JSON_Expected)

    def test_msg_with_output_xml(self):
        r = format_to_xml("wwww", "EEEMSG")
        XML_Result = ET.fromstring(r)
        self.assertEqual(
            b"<greetings><name>EEEMSG</name><msg>wwww</msg></greetings>",
            r,
        )  # noqa
