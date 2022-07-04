from math import lcm
from flask_restful import Resource, reqparse


class Math(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('numbers', type=int, help='Inputs must be a integer number type.',
                                   action='append', location='args')
        self.reqparse.add_argument(
            'number', type=int, help='Input must be a integer number type.', location='args')

    def get(self):
        """Mathematical operations

        Depending on the inputs, the operation will be performed.

        Args:
            numbers (list): List of numbers (optional)
            number (int): Number            (optional)

        Returns:
            json: if the imput was a list of numbers, the result will be the lcm of the list, 
            or if the imput was a number, the result will the number + 1.
        """
        args = self.reqparse.parse_args()

        if args['number']:
            number = args['number']
            return {"result": number + 1}, 200
        elif args['numbers']:
            numbers = args['numbers']

            return {"result": f"The lcm of {numbers} is: {lcm(*numbers)}"}, 200
        else:
            return {"message": "Please, input a number or a list of numbers."}, 400
