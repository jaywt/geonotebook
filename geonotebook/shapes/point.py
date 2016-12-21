from shapely.geometry import Point as sPoint

from .base import Shape


class Point(sPoint):
    def crop(self, raster_data, **kwargs):
        window = Shape.bounds_window(raster_data, self.bounds)
        return Shape.read_window(raster_data.reader, window), window

    def subset(self, raster_data, **kwargs):
        data = self.crop(raster_data)[0]
        return data[0][0]