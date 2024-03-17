from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from goods.models import Products


def q_search(query) -> Products:
    """A function to perform a search based on the provided query and return the matching Products    """
    if not query.strip():  # Если строка пустая или содержит только пробелы
        return Products.objects.none()  # Возвращаем пустой QuerySet
    elif query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query, config='simple')

    result = Products.objects.annotate(
        rank=SearchRank(
            vector, query)).filter(
        rank__gt=0).order_by("-rank")

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        ))
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        ))
    return result
