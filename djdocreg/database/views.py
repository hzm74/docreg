from django.shortcuts import render, get_object_or_404, redirect

from .models import Projecten
from .models import Vloeren
from .models import Bedrijven
from .models import Datum_Document
from .models import Controlemomenten_gepland

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect

from .forms import ProjectenForm
from .forms import BedrijvenForm
from .forms import VloerenForm
from .forms import Datum_DocumentForm
from .forms import Controlemomenten_geplandForm
# from .forms import Update_documentForm

from django.db.models import Max
from django.db.models import F

#from django.forms import formset_factory

alle_bedrijven = Bedrijven.objects.all()

# Create your views here.
def projecten(request):
    alle_projecten = Projecten.objects.all()
    return render(request, 'database/projecten.html', {'alle_projecten': alle_projecten})

def vloeren(request):
    alle_vloeren = Vloeren.objects.all()
    alle_vloeren_laatste = Vloeren.objects.annotate(laatste=Max('datum_document__datum')).filter(datum_document__datum=F('laatste'))

    return render(request, 'database/vloeren.html', {'alle_vloeren_laatste': alle_vloeren_laatste})

def voortgang(request):
    alle_vloeren = Vloeren.objects.all()
    return render(request, 'database/voortgang.html', {'alle_vloeren': alle_vloeren})

def statusbeheer(request):
    alle_vloeren = Vloeren.objects.all()
    return render(request, 'database/statusbeheer.html', {'alle_vloeren': alle_vloeren})

def bedrijven(request):
    alle_bedrijven = Bedrijven.objects.all()
    return render(request, 'database/bedrijven.html', {'alle_bedrijven': alle_bedrijven})

def projectinvoeren(request):
    if request.method == 'POST':
        formprojecten = ProjectenForm(request.POST)
        if formprojecten.is_valid():
            formprojecten.save()
            return redirect('projecten')
    else:
        formprojecten = ProjectenForm()
    return render(request, 'database/projectinvoeren.html', {'formprojecten': formprojecten})


#@login_required
def documentinvoeren(request):

    if request.method == 'POST':
        formvloeren = VloerenForm(request.POST, request.FILES)
        nieuwe_datum = request.POST["nieuwe_datum"]
        # formdatumdocument = Datum_DocumentForm(request.POST, request.FILES)
        # if formvloeren.is_valid() and formdatumdocument.is_valid():
        if formvloeren.is_valid():
            new_vloer = formvloeren.save()
            # new_datum_doc = formdatumdocument.save(commit=False)
            datum = Datum_Document.objects.create(datum=nieuwe_datum, vloeren=new_vloer)
            # datum.vloeren = new_vloer
            # new_datum_doc.save()
            return redirect('documentinvoeren')
    else:
        formdatumdocument = Datum_DocumentForm()
        formvloeren = VloerenForm()

    return render(request, 'database/documentinvoeren.html', {'formvloeren': formvloeren, 'formdatumdocument': formdatumdocument})

def bedrijfinvoeren(request):

    if request.method == 'POST':
        formbedrijven = BedrijvenForm(request.POST)
        if formbedrijven.is_valid():
            formbedrijven.save()
            return redirect('bedrijven')
    else:
        formbedrijven = BedrijvenForm()
    return render(request, 'database/bedrijfinvoeren.html', {'formbedrijven': formbedrijven, 'alle_bedrijven': alle_bedrijven})

#@login_required
# https://docs.djangoproject.com/en/3.1/topics/http/decorators/#django.views.decorators.http.require_http_methods
@require_http_methods(['POST'])
@csrf_protect
def delete_bedrijf(request):
    # https://docs.djangoproject.com/en/3.1/ref/request-response/#django.http.QueryDict.getlist
    object_ids = request.POST.getlist('id')
    object_list = Bedrijven.objects.filter(id__in=object_ids)
    # print(object_list)
    object_list.delete()
    return redirect('bedrijven')

#@login_required
@require_http_methods(['POST'])
@csrf_protect
def delete_document(request):
    object_ids = request.POST.getlist('id')
    object_list = Vloeren.objects.filter(id__in=object_ids)
    # print(object_list)
    object_list.delete()
    return redirect('vloeren')

# @require_http_methods(['POST'])
@csrf_protect
#@login_required
def update_document(request):
    alle_vloeren = Vloeren.objects.all()
    alle_vloeren_laatste = Vloeren.objects.annotate(laatste=Max('datum_document__datum')).filter(datum_document__datum=F('laatste'))
    
    if request.method == 'POST':
        datumnew = request.POST.get('nieuwe datum')
        object_ids = request.POST.getlist('id')  #get id's from checked checkboxes template
        object_list = Vloeren.objects.filter(id__in=object_ids)
        #print(object_list)
        #formdatumdocument = Datum_DocumentForm(request.POST)
        #if formdatumdocument.is_valid():
        #    new_datum_doc = formdatumdocument.save(commit=False)
            #new_datum_doc.vloeren = GET VLOEROBJECT FROM OBJECT_LIST (new_vloer = formvloeren.save())
        for object in object_list:
            # new_datum_doc.vloer = object
            # new_datum_doc.save()
            object.datum_document_set.create(datum = datumnew)
    # else:
        # formdatumdocument = Datum_DocumentForm
    return render(request, 'database/document_updaten.html', {'alle_vloeren': alle_vloeren, 'alle_vloeren_laatste': alle_vloeren_laatste})

# def update_document2(request):
#     # alle_vloeren = Vloeren.objects.all() 
#     alle_vloeren_laatste = Vloeren.objects.annotate(laatste=Max('datum_document__datum')).filter(datum_document__datum=F('laatste'))
#     updateform = Update_documentForm()

#     return render(request, "database/document_updaten2.html", {'alle_vloeren_laatste': alle_vloeren_laatste, 'updateform': updateform})

    