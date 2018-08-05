from django.urls import path
from django.conf.urls import url
from snapdealapp.views import *
app_name="snapdealapp"

urlpatterns = [
    url(r'^$',CategoryMainPage.as_view(),name="main_html"),
    path('signup/', signup, name='signup'),
    path('login/',LoginController.as_view(),name="login_html"),
    path('logout/',logout_user,name="logout_html"),

    path("category/",CategoryListView.as_view(),name="category_html"),
    path("category/add",CreateCategoryView.as_view(),name="categoryadd_html"),
    path('category/<int:pk>/edit',UpdateCategoryView.as_view(),name="edit_category_html"),
    path('category/<int:pk>/delete',DeleteCategoryView.as_view(),name="delete_category_html"),


    path("category/<int:pk>", ProductList.as_view(), name="product_html"),
    path("category/<int:pk>/product/add", CreateProductView.as_view(), name="product_add_html"),
    path("product/<int:pk>",ProductDetails.as_view(),name='product_details_html'),
    path("category/<int:category_id>/product/<int:pk>/edit",UpdateProductView.as_view(),name="product_edit_html"),
    path("category/<int:category_id>/product/<int:pk>/delete",DeleteProductView.as_view(),name="product_delete_html"),

    path("category/<int:pk>/add_to_cart",add_to_cart,name="add_to_cart"),
    path("cart/<int:pk>/delete",DeleteCartView.as_view(),name="remove_from_cart"),
    path("cart",Cartlistview.as_view(),name='cart'),

    path("cart/clear",clear_cart,name='clear_cart'),
    path("placeorder/", place_order, name="place_order"),
    path("order", Orderlistview.as_view(), name="order_html"),
    path("order/", order, name="order"),
    path("orderedlist/<int:pk>/delete", DeleteOrderedlistView.as_view(), name="remove_from_orderedlist"),

    path('search/', search_all, name='list'),

    path('categorysearch/<slug:string>/', SearchCategoryView, name='list_category'),
    path('productsearch/<slug:string>/', SearchProductView, name='list_product'),

    path("address", AddressListView.as_view(), name="address_html"),
    path("address/<int:pk>/delete", DeleteAddressView.as_view(), name="address_delete_html"),
    path("address/<int:pk>/edit", UpdateAddressView.as_view(), name="address_edit_html"),
    path("address/add", CreateAddressView.as_view(), name="address_add_html"),

    path('payment_success',payment_success,name='payment_success'),
    path('payment_options',payment_options,name='payment_options'),
    path('allproducts',AllProducts.as_view(),name='allproducts'),

]