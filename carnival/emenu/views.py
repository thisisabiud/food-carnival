import io
from django.shortcuts import get_object_or_404, render
from emenu.models import Menu, Vendor
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def menu_list(request):
    """
    Displays a list of vendors with links to their menus.

    :param request: The current HTTP request.
    :return: A rendered HTML page with the list of vendors.
    """

    vendors_list = Vendor.objects.order_by('name')
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

