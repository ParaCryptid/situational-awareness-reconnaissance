import geojson

class GeospatialAnalyzer:
    def __init__(self, geojson_file):
        """
        Initialize the analyzer with a GeoJSON file.
        :param geojson_file: Path to the GeoJSON file.
        """
        self.geojson_file = geojson_file

    def analyze_geospatial_data(self):
        """
        Analyze geospatial data to extract insights.
        :return: A summary of geospatial features.
        """
        with open(self.geojson_file, "r") as file:
            data = geojson.load(file)
        
        feature_summary = {
            "total_features": len(data.get("features", [])),
            "feature_types": set([feature["geometry"]["type"] for feature in data.get("features", [])])
        }
        return feature_summary

# Example usage
# analyzer = GeospatialAnalyzer("path/to/geojson/file.geojson")
# summary = analyzer.analyze_geospatial_data()
# print(summary)
