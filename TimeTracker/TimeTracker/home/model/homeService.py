from TimeTracker.home.model.homeModel import AccountModel
from flask import jsonify


class AccountService():

    def create(self,request):

        account = AccountModel()
        account.first_name = request.form['first_name']
        account.last_name = request.form['last_name']
        account.user_id = request.form['user_id']

        account.put()

        return account

    def getAllAccounts(self):
        list_of_accounts = AccountModel.query_all_accounts()
        records = {}


        if list_of_accounts:
            records["rows"] = [dict(({'key': acct.key.urlsafe()}).items() + acct.to_dict().items()) for acct in list_of_accounts]
        else:
            records = list_of_accounts

        # records = {"rows":[{"first_name":"allen","last_name":"balang","user_id":"sal123"},{"first_name":"juan","last_name":"cruz","user_id":"sal124"},{"first_name":"john","last_name":"doe","user_id":"sal125"}]}

        return records



