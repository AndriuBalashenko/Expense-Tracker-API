from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

...

schema_view = get_schema_view(
    openapi.Info(
        title="Expense Tracker API",
        default_version="v1",
        description="Track your expenses based on your income",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="odionyejude@outlook.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("expenses/", include("expenses.urls")),
    path("income/", include("income.urls")),
    path("userstats/", include("userstats.urls")),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api.json/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

handler404 = "utils.views.error_404"
handler500 = "utils.views.error_500"
