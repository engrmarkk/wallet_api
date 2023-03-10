from marshmallow import fields, Schema


class plainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    phone_number = fields.Str(required=True)
    account_number = fields.Int(load_only=True)
    is_admin = fields.Bool(load_only=True)


"""
"first_name": "",
"last_name": "",
"username": "",
"email": "",
"password": "",
"phone_number": ,
"account_number": ""
"""


class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    amount = fields.Int(required=True)
    account_number = fields.Int(required=True)


class transactionByUser(Schema):
    id = fields.Int(dump_only=True)
    transaction_type = fields.Str()
    date_posted = fields.DateTime()
    transaction_amount = fields.Int()
    sender = fields.Str()
    user_id = fields.Int(required=True, load_only=True)


class transaction2schema(Schema):
    id = fields.Int(dump_only=True, load_only=True)
    transaction_type = fields.Str()
    date_posted = fields.DateTime()
    transaction_amount = fields.Int()
    account_amount = fields.Int()
    sender = fields.Str()
    user_id = fields.Int(required=True, load_only=True)
    user = fields.Nested(plainUserSchema(), dump_only=True)


class UserSchema(plainUserSchema):
    account_number = fields.Int()
    account_balance = fields.Int()
    transacts = fields.List(fields.Nested(transaction2schema()), dump_only=True)


class UserLoginschema(Schema):
    username = fields.Str()
    password = fields.Str(required=True)


class TokenReset(Schema):
    res_token = fields.Int()
    password = fields.Str()
    confirm_password = fields.Str()
