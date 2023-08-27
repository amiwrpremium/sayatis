from django.shortcuts import render
from django.views import View
from django.http import (
    HttpRequest,
    HttpResponse,
)


class HomeView(View):
    """
    Base view
    """

    async def get(self, request: HttpRequest) -> HttpResponse:  # noqa
        """
        Get method for base view

        Args:
            request (HttpRequest): request

        Returns:
            HttpResponse: response
        """

        return render(request, "home/index.html")


class FaView(View):
    """
    Base view
    """

    async def get(self, request: HttpRequest) -> HttpResponse:  # noqa
        """
        Get method for base view

        Args:
            request (HttpRequest): request

        Returns:
            HttpResponse: response
        """

        return render(request, "home/index-fa.html")
