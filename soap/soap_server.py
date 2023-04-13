from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class WeightConversionService(ServiceBase):
    @rpc(Integer, Unicode, Unicode, _returns=Unicode)
    def ConvertWeight(ctx, weight, from_unit, to_unit):
        if from_unit == 'Grams' and to_unit == 'Ounces':
            result = weight / 28.35
        else:
            result = 'Error: Invalid units'

        return str(result)

application = Application([WeightConversionService],
                          tns='http://127.0.0.1:8000/webservice',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, WsgiApplication(application))
    server.serve_forever()
