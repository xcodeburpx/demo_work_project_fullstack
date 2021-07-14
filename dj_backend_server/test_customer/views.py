from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import Customer
# Create your views here.

class CustomerListView(ListView):
    model = Customer
    template_name = 'test_customer/main.html'

def customer_render_pdf_view(request, *args, **kwargs):

    pk = kwargs.get('pk')
    customer = get_object_or_404(Customer, pk=pk)   

    template_path = 'test_customer/pdf2.html'
    context = {'customer': customer}

    response = HttpResponse(content_type='application/pdf')

    # IF download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # IF display:
    response['Content-Disposition'] = 'filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view(request):
    template_path = 'test_customer/pdf1.html'
    context = {'myvar': 'this is your template context'}

    response = HttpResponse(content_type='application/pdf')

    # IF download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # IF display:
    response['Content-Disposition'] = 'filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response