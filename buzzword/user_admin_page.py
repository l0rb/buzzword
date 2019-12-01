from django.contrib.admin.sites import AdminSite
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm

class UserAdminAuthenticationForm(AuthenticationForm):
    # the default AdminAuthenticationForm requires user.is_staff
    required_css_class = 'required'

class UserAdminSite(AdminSite):
    site_header = 'Settings'
    site_title = 'Settings'
    index_title = 'Settings list'

    login_form = UserAdminAuthenticationForm

    def has_permission(self, request):
        # don't need to be staff to use this one
        return request.user.is_active

user_admin = UserAdminSite(name='settings')

