from flask_restful import Resource, reqparse

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome':'alpha hotel',
        'estrelas':4.3,
        'diaria': 420.00,
        'cidade':'Sao Paulo'
    },
     {
        'hotel_id': 'beta',
        'nome':'beta hotel',
        'estrelas':4.5,
        'diaria': 480.00,
        'cidade':'Rio de Janeiro'
    },
     {
        'hotel_id': 'alpha',
        'nome':'alpha hotel',
        'estrelas':4.9,
        'diaria': 720.00,
        'cidade':'Sao Paulo'
    }
]

class Hoteis(Resource):

    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    def get(self,hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] ==  hotel_id:
                return hotel
        return {'message':'Hotel not found'}, 404
        pass

    def post(self,hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')

        dados = argumentos.parse_args()
        novohotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas':float(dados['estrelas']),
            'diaria':float(dados['diaria']),
            'cidade':dados['cidade']
        }
        hoteis.append(novohotel)
        return novohotel, 200
    def put(self,hotel_id):
        pass
    
    def delete(self,hotel_id):
        pass