from django.conf.urls import patterns, include, url
from django.contrib import admin
from userauth.views import *
from phoneinfo.views import *
from phonechange.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zichanmanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


#####user login
	url(r'^$',user_login),
	url(r'^account_login$',account_login),
	url(r'^user_logout$',user_logout),

###user manager 

	url(r'^user_index/user_add$',user_add),
	url(r'^user_index/user_del$',user_del),
	url(r'^upfile_index/$',upfile_index),
	url(r'^baofei/$',baofei),
#	url(r'^phoneinfo_add$',phoneinfo_add),
	
###


    url(r'^phone_info$',phone_info),
	url(r'^phoneinfo_add$',phoneinfo_add),
	url(r'^phoneinfo_del$',phoneinfo_del),
    #url(r'^phonechange/$',phoneinfochange),
    url(r'^user_index/$',user_index),

####chang manager
	url(r'^change_info/$',change_info),
	url(r'^change_info/phone_change_req/$',phone_change_req),
	url(r'^change_commit_index/$',change_commit_index),
	url(r'^change_commit_index/change_commit/$',change_commit),
	url(r'^change_find_index/$',change_find_index),
	url(r'^change_password_index/$',change_password_index),
	url(r'^change_password_index/change_password_commit/$',change_password),

)
