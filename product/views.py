# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
import json
import requests

# Create your views here.


def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', locals(), context)


def search_product(request):
    product_id = request.GET.get('productId')
    category_type = request.GET.get('categoryType')
    page_num = request.GET.get('pageNum', 1)

    error_message = None
    try:
        request_url = settings.PRODUCT_SEARCH_URL %(settings.EBAY_APP_ID, page_num, category_type, product_id)
        print request_url
        response = requests.get(request_url)
        response_dict = json.loads(response.text)
        response_dict = response_dict['findItemsByProductResponse'][0]

        if response_dict['ack'][0] == 'Success':
            result_list = response_dict['searchResult'][0]['item']
            pagination_info = response_dict['paginationOutput']

            current_page = int(pagination_info[0]['pageNumber'][0])
            total_pages = pagination_info[0]['totalPages'][0]
            page_num_list = range(1, int(total_pages)+1)
        else:
            error_message = 'No results found'
    except:
        error_message = 'No results found'

    return render_to_response('results.html', locals(), RequestContext(request))
