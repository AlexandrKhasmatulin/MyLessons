from rest_framework.pagination import PageNumberPagination


class LessonPaginator(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page size'
    max_page_size = 10