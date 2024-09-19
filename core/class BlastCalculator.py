class BlastCalculator:
    def calculate_blast_radius(self, yield_kt, overpressure):
        """Calculate the blast radius based on yield and overpressure."""
        if overpressure == 5:
            k = 0.17
        elif overpressure == 1:
            k = 0.33
        else:
            k = 0.17 * (5 / overpressure) ** (1 / 3)
        return k * (yield_kt ** (1 / 3))

    def calculate_thermal_radius(self, yield_kt):
        """Calculate the thermal radiation radius based on the bomb yield."""
        return 0.13 * (yield_kt ** 0.4)

    def calculate_fallout(self, yield_kt, wind_speed, wind_direction):
        """Estimate the fallout spread based on wind conditions."""
        # Simplified fallout model (for demonstration purposes)
        fallout_area = yield_kt * wind_speed * 0.1
        return {
            "fallout_area": fallout_area,
            "wind_direction": wind_direction,
            "description": "Fallout area estimated based on wind conditions."
        }

    def calculate_blast_radius_at_intervals(self, yield_kt, overpressure_intervals):
        """Calculate blast radii for a list of overpressure intervals."""
        radii = {}
        for overpressure in overpressure_intervals:
            radii[overpressure] = self.calculate_blast_radius(yield_kt, overpressure)
        return radii

    def calculate_thermal_radius_at_intervals(self, yield_intervals):
        """Calculate thermal radiation radii for a list of yield intervals."""
        radii = {}
        for interval_yield in yield_intervals:
            radii[interval_yield] = self.calculate_thermal_radius(interval_yield)
        return radii

