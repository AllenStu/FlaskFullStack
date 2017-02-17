from TimeTracker.home.model.homeModel import AccountModel

class AccountService():

    def create(self):

        account = AccountModel()
        # account.first_name = new_account.first_name
        # account.last_name = new_account.last_name
        # account.user_id = new_account.user_id

        account.first_name = 'Arthur Allen'
        account.last_name = 'Balang'
        account.user_id = 'sj12132'

        account.put()

        return account


