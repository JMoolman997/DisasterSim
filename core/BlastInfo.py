
import math

class BlastInfo:
    def __init__(self, yield_kt, overpressure=None, lat=None, lon=None, wind_speed=None, wind_direction=None):
        """
        Initialize the BlastInfo object with details about the detonation.
        
        Args:
            yield_kt (float): Yield of the bomb in kilotons.
            overpressure (float, optional): Overpressure in psi for blast radius calculation.
            lat (float, optional): Latitude of the detonation (for map or location-based data).
            lon (float, optional): Longitude of the detonation (for map or location-based data).
            wind_speed (float, optional): Wind speed (for fallout calculation).
            wind_direction (float, optional): Wind direction in degrees (for fallout calculation).
        """
        self.yield_kt = yield_kt
        self.overpressure = overpressure
        self.lat = lat
        self.lon = lon
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

        # Instantiate the BlastCalculator to handle calculations
        self.calculator = BlastCalculator()

    # Request the blast radius based on current overpressure
    def request_blast_radius(self):
        if self.overpressure is None:
            return "Overpressure value is required for blast radius calculation."
        return self.calculator.calculate_blast_radius(self.yield_kt, self.overpressure)

    # Request the thermal radiation radius
    def request_thermal_radius(self):
        return self.calculator.calculate_thermal_radius(self.yield_kt)

    # Request the fallout information (if wind data is provided)
    def request_fallout(self):
        if self.wind_speed is None or self.wind_direction is None:
            return "Wind speed and direction are required for fallout calculation."
        return self.calculator.calculate_fallout(self.yield_kt, self.wind_speed, self.wind_direction)

    # Request blast radius at multiple intervals
    def request_blast_radius_at_intervals(self, overpressure_intervals):
        if not overpressure_intervals:
            return "Overpressure intervals are required."
        return self.calculator.calculate_blast_radius_at_intervals(self.yield_kt, overpressure_intervals)

    # Request thermal radiation radius at multiple yield intervals
    def request_thermal_radius_at_intervals(self, yield_intervals):
        if not yield_intervals:
            return "Yield intervals are required."
        return self.calculator.calculate_thermal_radius_at_intervals(yield_intervals)

    # Add location data for convenience
    def get_location(self):
        if self.lat is not None and self.lon is not None:
            return {"lat": self.lat, "lon": self.lon}
        return "No location data available."


# Example usage
def main():
    # Create a BlastInfo object with sample data
    blast_info = BlastInfo(
        yield_kt=1000,  # 1 megaton
        overpressure=5,  # 5 psi overpressure
        lat=40.7128, lon=-74.0060,  # New York City coordinates
        wind_speed=15, wind_direction=270  # Wind conditions for fallout
    )

    # Request blast radius calculation
    print("Blast Radius (5 psi):", blast_info.request_blast_radius())
    
    # Request thermal radiation radius
    print("Thermal Radiation Radius:", blast_info.request_thermal_radius())

    # Request fallout information
    print("Fallout Information:", blast_info.request_fallout())

    # Request blast radius at specific overpressure intervals
    print("Blast Radius at Intervals:", blast_info.request_blast_radius_at_intervals([10, 5, 2, 1]))

    # Request thermal radiation radius at different yield intervals
    print("Thermal Radiation at Intervals:", blast_info.request_thermal_radius_at_intervals([500, 1000, 2000]))

    # Request location
    print("Location:", blast_info.get_location())

if __name__ == "__main__":
    main()
