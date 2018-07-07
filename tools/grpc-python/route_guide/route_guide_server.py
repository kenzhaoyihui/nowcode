from concurrent import futures
import time
import math

import grpc

import route_guide_pb2
import route_guide_pb2_grpc
import route_guide_resources

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def get_feature(feature_db, point):
    for feature in feature_db:
        if feature.location == point:
            return feature
    return None


def get_distance(start, end):
    """Distance between two points."""
    coord_factor = 10000000.0
    lat_1 = start.latitude / coord_factor
    lat_2 = end.latitude / coord_factor
    lon_1 = start.longitude / coord_factor
    lon_2 = end.longitude / coord_factor

    lat_rad_1 = math.radians(lat_1)
    lat_rad_2 = math.radians(lat_2)
    delta_lat_rad = math.radians(lat_2 - lat_1)
    delta_lon_rad = math.radians(lon_2 - lon_1)

    a = (pow(math.sin(delta_lat_rad / 2), 2) +
         (math.cos(lat_rad_1) *
          (math.cos(lat_rad_2)) * pow(math.sin(delta_lon_rad / 2), 2)))

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    R = 6371000

    return R * c

class RouteGuideTest(route_guide_pb2_grpc.RouteGuideServicer):
    def __init__(self):
        self.db = route_guide_resources.read_route_guide_database()

    def GetFeature(self, request, context):
        pass

    def ListFeatures(self, request, context):
        pass

    def RecordRoute(self, request_iterator, context):
        pass

    def RouteChat(self, request_iterator, context):
        pass

    
    
