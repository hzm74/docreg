from . import views
from django.urls import path

urlpatterns = [
    path('', views.vloeren, name='vloeren'),
    path('projecten', views.projecten, name='projecten'),
    path('voortgang', views.voortgang, name='voortgang'),
    path('statusbeheer', views.statusbeheer, name='statusbeheer'),
    path('bedrijven', views.bedrijven, name='bedrijven'),
    path('documentinvoeren', views.documentinvoeren, name='documentinvoeren'),
    path('projectinvoeren', views.projectinvoeren, name='projectinvoeren'),
    path('bedrijfinvoeren', views.bedrijfinvoeren, name='bedrijfinvoeren'),

    path('delete_bedrijf', views.delete_bedrijf, name='delete_bedrijf'),
    path('delete_document', views.delete_document, name='delete_document'),
    path('update_document', views.update_document, name='update_document'),

    # path('update_document2', views.update_document2, name='update_document2'),

]
