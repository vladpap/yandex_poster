from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Point


def poster_detail_view(request, post_id):

    point = get_object_or_404(
        Point.objects.prefetch_related('images'),
        id=post_id)
    point_images = [f'.{image.image.url}' for image in point.images.all()]

    point_id = {
        "title": point.title,
        "imgs": point_images,
        "description_short": point.short_description,
        "description_long": point.long_description,
        "coordinates": {
            "lng": point.longitude,
            "lat": point.latitude
            }
    }

    return JsonResponse(point_id)


def map_poster(request):

    points = [{
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [point.longitude, point.latitude]
        },
        'properties': {
            'title': point.title,
            'placeId': point.id,
            'detailsUrl': reverse('detail_view', args=(point.id,))
        }
    } for point in Point.objects.all()]

    places_geojson = {
        'type': 'FeatureCollection',
        'features': points
        }
    return render(
        request,
        'index.html',
        context={'places_geojson': places_geojson})
