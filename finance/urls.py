from rest_framework.routers import DefaultRouter
from .views import (
    TypeViewSet, StatusViewSet, CategoryViewSet,
    SubcategoryViewSet, TransactionViewSet
)

router = DefaultRouter()
router.register(r'types', TypeViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = router.urls
