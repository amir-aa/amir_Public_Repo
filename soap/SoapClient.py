import requests
from lxml import etree

url = 'http://127.0.0.1:8000/webservice/?wsdl'

headers = {'content-type': 'application/soap+xml'}

request_body = """<?xml version="1.0" encoding="UTF-8"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
                 xmlns:tns="http://127.0.0.1:8000/webservice">
                   <soap:Body>
                      <tns:ConvertWeight>
                         <tns:weight>100</tns:weight>
                         <tns:from_unit>Grams</tns:from_unit>
                         <tns:to_unit>Ounces</tns:to_unit>
                      </tns:ConvertWeight>
                   </soap:Body>
                </soap:Envelope>"""

response = requests.post(url, data=request_body, headers=headers)

soap_response = etree.fromstring(response.content)

result = soap_response.xpath('//ConvertWeightResponse/return/text()')
print(response.content.decode())

