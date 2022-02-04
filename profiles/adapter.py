
from allauth.account.adapter import DefaultAccountAdapter
from .models import *


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        This is called when saving user via allauth registration.
        We override this to set additional data on user object.
        """
        # Do not persist the user yet so we pass commit=False
        # (last argument)
        user = super(AccountAdapter, self).save_user(
            request, user, form, commit=False)
        user.userType = form.cleaned_data.get('userType')
        user.userType = UserType(request.POST['userType'])

        if not user.userType:
            user.userType = UserType(USERTYPE_DEFAULT)  # Set default user type

        # Save once to get the user ID
        user.save()

        if int(user.userType.id) == USERTYPE_SELLER:
            # Seller user
            seller = UserArtistProfile()
            seller.user_id = user.id
            seller.username = request.POST['username']
            seller.save()
        else:
            # Other than that, general users
            user.userType = UserType(USERTYPE_BUYER)
            buyer = Profile()
            buyer.user_id = user.id
            buyer.username = request.POST.get('username', False)
            buyer.save()
