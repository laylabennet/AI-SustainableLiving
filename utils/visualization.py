import matplotlib.pyplot as plt

class DataVisualization:
    @staticmethod
    def plot_environmental_data(environmental_data):
        # Placeholder logic for plotting environmental data
        temperature = environmental_data["temperature"]
        air_quality = environmental_data["air_quality"]

        labels = ["Temperature", "Air Quality"]
        values = [temperature, air_quality]

        plt.bar(labels, values)
        plt.xlabel("Metrics")
        plt.ylabel("Values")
        plt.title("Environmental Data Visualization")
        plt.show()

    @staticmethod
    def plot_sustainability_factors(sustainability_factors):
        # Placeholder logic for plotting sustainability factors
        plt.figure(figsize=(6, 4))
        plt.bar(sustainability_factors.keys(), sustainability_factors.values())
        plt.xlabel("Sustainability Factors")
        plt.ylabel("Predicted Levels")
        plt.title("Predicted Sustainability Factors")
        plt.show()
