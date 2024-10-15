from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.response import Response
from emenu.models import Gallery, Menu, Vendor
from emenu.serializers import VendorSerializer
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
    categories = set(menu_items.values_list('category', flat=True))
    context = {'vendor': vendor, 'menu_items': menu_items, 'categories': categories}
    return render(request, 'emenu/menu.html', context)

@api_view(['GET'])
def vendors_search(request):
    """
    Searches for vendors by name.

    :param request: The current HTTP request.
    :return: A list of vendors matching the search query.
    """

    query = request.GET.get('query', '')
    vendors = Vendor.objects.filter(
        Q(name__icontains=query)
    ).order_by('name')[:3]

    serializer = VendorSerializer(vendors, many=True)
    return Response(serializer.data)

def gallery(request):
    photos = Gallery.objects.all().order_by('-uploaded_at')
    context = {'photos': photos}
    return render(request, 'emenu/gallery.html', context)
