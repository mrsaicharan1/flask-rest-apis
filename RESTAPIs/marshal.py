# from flask import Flask
from flask_restful import fields, marshal_with

required_fields = {'name': fields.Raw }
@marshal_with(required_fields)
def get():
    return { 'age': 36, 'name': 'Philips' }

