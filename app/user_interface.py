class UserInterface:
    def main_menu(self):
        print("\nMain Menu:")
        print("1. Create User Profile")
        print("2. Predict Sustainability Factors")
        print("3. Get Sustainability Recommendations")
        print("4. Exit")
        choice = int(input("Select an option: "))
        return choice

    def create_user_profile(self):
        print("\nCreate User Profile:")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender: ")
        return {
            "name": name,
            "age": age,
            "gender": gender
        }

    def display_user_profile(self, user_profile):
        print("\nUser Profile:")
        print(f"Name: {user_profile['name']}")
        print(f"Age: {user_profile['age']}")
        print(f"Gender: {user_profile['gender']}")

    def get_user_id(self):
        return int(input("\nEnter your user ID: "))

    def collect_environmental_data(self):
        print("\nCollect Environmental Data:")
        temperature = float(input("Enter current temperature: "))
        air_quality = float(input("Enter air quality index: "))
        return {
            "temperature": temperature,
            "air_quality": air_quality
        }

    def predict_sustainability_factors(self, user_id, environmental_data):
        # Placeholder logic for predicting sustainability factors
        return {
            "carbon_footprint": "Low",
            "energy_consumption": "Moderate"
        }

    def display_sustainability_factors(self, sustainability_factors):
        print("\nPredicted Sustainability Factors:")
        print(f"Carbon Footprint: {sustainability_factors['carbon_footprint']}")
        print(f"Energy Consumption: {sustainability_factors['energy_consumption']}")

    def get_sustainability_recommendations(self, user_id):
        # Placeholder logic for getting sustainability recommendations
        return [
            "Reduce energy consumption by turning off lights when not needed.",
            "Use public transportation or carpool to reduce carbon footprint."
        ]

    def display_recommendations(self, recommendations):
        print("\nSustainability Recommendations:")
        for idx, recommendation in enumerate(recommendations, start=1):
            print(f"{idx}. {recommendation}")

