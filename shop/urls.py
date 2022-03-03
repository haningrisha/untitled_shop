from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shop import views
from compilations import views as comp_views

urlpatterns = [
    # Shop paths
    path('shops/', views.ShopListView.as_view(), name='shop-list'),
    path('shops/<int:pk>', views.ShopDetailView.as_view(), name='shop-detail'),
    path('shops/<int:pk>/products', views.ShopProductListView.as_view(), name='shop-product-list'),

    # Seller paths
    path('sellers/', views.SellerListView.as_view(), name='seller-list'),
    path('sellers/<int:pk>', views.SellerDetailView.as_view(), name='seller-detail'),

    # Product paths
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

    # Tag paths
    path('tags/', views.TagListView.as_view(), name='tag-list'),
    path('tags/<int:pk>', views.TagDetailView.as_view(), name='tag-detail'),

    # Category paths
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),

    # Customer paths
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),

    # Order paths
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),

    # Cart paths
    path('carts/', views.CartListView.as_view(), name='cart-list'),
    path('carts/<int:pk>', views.CartDetailView.as_view(), name='cart-detail'),

    # Customer paths
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>', views.CommentDetailView.as_view(), name='comment-detail'),

    # Compilation paths
    path('compilations/discount_products', comp_views.DiscountCompilationView.as_view(), name='discount-compilation'),
    path('compilations/popular_products', comp_views.PopularCompilationView.as_view(), name='popular-compilation'),
    path('compilations/personal_products', comp_views.PersonalCompilationView.as_view(), name='personal-compilation'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
