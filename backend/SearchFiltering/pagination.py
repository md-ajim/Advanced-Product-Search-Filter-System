

from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 4                      # default page size
    page_size_query_param = 'page_size'  # allows frontend to override with ?page_size=
    max_page_size = 100                # prevents abuse by setting an upper limit
