from django.shortcuts import render


from validator.models import Certificate
def validate_certificate(request):
    query = request.GET.get('certificate_number', None)
    certificate = None
    error = None

    if query:
        try:
            certificate = Certificate.objects.get(certificate_no=query)
        except Certificate.DoesNotExist:
            error = "Certificate not found. Please check the number and try again."

    return render(request, 'index.html', {
        'certificate': certificate,
        'error': error
    })

