import json

class DataManager:
    def __init__(self):
        self.user_profiles_file = "data/user_profiles.json"
        self.environmental_data_file = "data/environmental_data.json"
        self.sustainability_recommendations_file = "data/sustainability_recommendations.json"

    def load_user_profiles(self):
        with open(self.user_profiles_file, "r") as f:
            user_profiles = json.load(f)
        return user_profiles

    def save_user_profiles(self, user_profiles):
        with open(self.user_profiles_file, "w") as f:
            json.dump(user_profiles, f, indent=4)

    def load_environmental_data(self):
        with open(self.environmental_data_file, "r") as f:
            environmental_data = json.load(f)
        return environmental_data

    def save_environmental_data(self, environmental_data):
        with open(self.environmental_data_file, "w") as f:
            json.dump(environmental_data, f, indent=4)

    def load_sustainability_recommendations(self):
        with open(self.sustainability_recommendations_file, "r") as f:
            sustainability_recommendations = json.load(f)
        return sustainability_recommendations

    def save_sustainability_recommendations(self, sustainability_recommendations):
        with open(self.sustainability_recommendations_file, "w") as f:
            json.dump(sustainability_recommendations, f, indent=4)
