from django.http import JsonResponse
from django.shortcuts import render
from places.models import Point


def get_point_from_id(id):

    point = Point.objects.filter(id=id).first()
    images = []
    for image in point.images.all():
        images.append(f'.{image.image.url}')

    return {
        "title": point.title,
        "imgs": images,
        "description_short": point.description_short,
        "description_long": point.description_long,
        "coordinates": {
            "lng": point.longitude,
            "lat": point.latitude
            }
    }


def map_poster(request):

    points = []
    points_set = Point.objects.all()
    for point_set in points_set:
        point = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [point_set.longitude, point_set.latitude]
            },
            'properties': {
                'title': point_set.title,
                'placeId': point_set.id,
                'detailsUrl': f'/places/{point_set.id}'
            }
        }
        points.append(point)

    places_geojson = {
        'type': 'FeatureCollection',
        'features': points
        }
    return render(
        request,
        'index.html',
        context={'places_geojson': places_geojson})


def poster_detail_view(request, post_id):
    return JsonResponse(get_point_from_id(post_id))
