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
        datalist = []
        record = {}

        for acct in list_of_accounts:
            # strval = strval + acct.first_name
            record = acct.to_dict()
            datalist.append(record)


        # strval = [{'first_name': 'stuart', 'last_name': 'reyes', 'user_id': 'sa123'},
        #           {'first_name': 'ann', 'last_name': 'dela cruz', 'user_id': 'sa124'},
        #           {'first_name': 'john', 'last_name': 'doe', 'user_id': 'sa125'}]

        return datalist



