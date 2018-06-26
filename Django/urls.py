from django.conf.urls import patterns, include, url
from django.contrib import admin
from trips.views import hello_world, post, post_detail
from restaurant.views import menu, home
#from trips.views import home, insertdata


urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'), #將首頁指向home這個View function
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello_world),
    url(r'^post$', post),
    url(r'^post/(?P<id>\d+)/$', post_detail, name='post_detail'),
    #抓出一個以上阿拉伯數字(\d+ 如:0~無限)，並把抓出來的東西取名為id(?P<id>)
    # 整個()括起來代表作為view.py post_detail函式的參數。
    #而name指的是為該串網址(post/(?P<id>\d+))命名，可讓該網址在Temp中以post_detail此代名作為使用

    url(r'^menu/$', menu),

    #url(r'^$', 'trips.views.home'),
    #url(r'^insertdata/$', 'trips.views.insertdata'),
    #url(r'^(\d{1,2})/plus/(\d{1,2})/$', math), #\d{1,2}表示匹配一或兩個數字 {0~99}，()括起來代表作為四則運算參數

)
