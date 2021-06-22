from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Person, Address

class CreatePdf(View):
    template_name = 'pdf_view.html'

    def get(self, request, p_id):
        if Person.objects.filter(usuario_id=p_id).exists() and Address.objects.filter(persona_id=p_id).exists():
            persona = Person.objects.get(usuario_id=p_id)
            direccion = Address.objects.get(persona_id=p_id)
        contextP = {'persona': persona, 'direccion': direccion}
        template_path = self.template_name
        #context = {'myvar': 'Aquí va el contexto'}
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        # If download:
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # If display:
        response['Content-Disposition'] = 'filename="reporte.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(contextP)

        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
           return HttpResponse('Ha ocurrido un error <pre>' + html + '</pre>')
        return response
