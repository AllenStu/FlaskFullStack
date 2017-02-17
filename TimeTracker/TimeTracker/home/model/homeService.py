from TimeTracker.home.model.homeModel import AccountModel


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



