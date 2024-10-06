import io
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas 
from emenu.models import Menu, Vendor
from emenu.utils import generate_qr_code
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def menu_list(request):
    """
    Displays a list of vendors with links to their menus.

    :param request: The current HTTP request.
    :return: A rendered HTML page with the list of vendors.
    """

    vendors_list = Vendor.objects.order_by('created_at')
    page_number = request.GET.get('page')
    paginator = Paginator(vendors_list, 8)
    try:
        vendors = paginator.page(page_number)
    except PageNotAnInteger:
        vendors = paginator.page(1)
    except EmptyPage:
        vendors = paginator.page(paginator.num_pages)
    
    context = {'vendors': vendors}
    return render(request, 'emenu/menu_list.html', context)

def menu(request, id):
    """
    Displays a menu for a given vendor.

    :param request: The current HTTP request.
    :param id: The ID of the vendor to display the menu for.
    :return: A rendered HTML page with the menu.
    """
    vendor = get_object_or_404(Vendor, pk=id)
    menu_items = Menu.objects.filter(vendor=vendor)
    context = {'vendor': vendor, 'menu_items': menu_items}
    return render(request, 'emenu/menu.html', context)

def vendor_menu_pdf(request, id):
    """
    Downloads a PDF of the menu for a given vendor.

    :param request: The current HTTP request.
    :param id: The ID of the vendor to download the menu for.
    :return: A PDF file of the menu.
    """
    vendor = get_object_or_404(Vendor, pk=id)
    menu_items = Menu.objects.filter(vendor=vendor)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{vendor.name}_menu.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.setFont('Helvetica-Bold', 16)
    p.drawString(1*inch, 10*inch, f"{vendor.name} Menu")
    p.setFont('Helvetica', 12)
    y=9.5*inch
    for item in menu_items:
        p.drawString(1*inch, y, f"{item.name}: {item.price}")
        y -= 0.25*inch
        p.drawString(1*inch, y, f"{item.description}")
        y -= 0.35*inch
        
    menu_url = request.build_absolute_uri(reverse('emenu:menu_detail', args=[vendor.id]))
    qr_code = generate_qr_code(menu_url)
    p.drawImage(io.BytesIO(qr_code).getvalue(), 6.5*inch, 9*inch, width=2*inch, height=2*inch)
    p.showPage()
    p.save()

    return response
