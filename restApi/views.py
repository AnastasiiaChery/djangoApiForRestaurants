import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


with open('initial_restaurants.json', 'r') as json_file:
    restaurants = json.load(json_file)


class RestListCreateView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(restaurants, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        restaurants.append(data)

        return Response(restaurants , status=status.HTTP_201_CREATED)


class RankListView(APIView):

    def get(self, request, *args, **kwargs):
        sort_restaurants = sorted(restaurants, key=lambda x: x['rank'], reverse=True)
        return Response(sort_restaurants, status=status.HTTP_200_OK)

class LuxListView(APIView):

    def get(self, request, *args, **kwargs):
        lux_restaurants = sorted(restaurants, key=lambda x: x['average_bill'], reverse=True)[:1]
        return Response(lux_restaurants, status=status.HTTP_200_OK)


class NameMenuView(APIView):

    def get(self, request, *args, **kwargs):
        item_name = self.kwargs['dish']
        filtered_restaurants = [restaurant for restaurant in restaurants if item_name in restaurant['menu']]
        return Response(filtered_restaurants)

