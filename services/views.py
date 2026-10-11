from django.shortcuts import get_object_or_404, redirect, render
from .forms import ServiceRequestForm
from .models import ServiceRequest


def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save()
            return redirect("request_confirmation", pk=service_request.pk)
    else:
        form = ServiceRequestForm()

    return render(request, "services/request_form.html", {"form": form})


def request_confirmation(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    return render(
        request,
        "services/request_confirmation.html",
        {"service_request": service_request},
    )


def request_list(request):
    requests = ServiceRequest.objects.order_by("-created_at")
    return render(request, "services/request_list.html", {"requests": requests})