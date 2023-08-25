from user_interface import UserInterface

def main():
    print("Welcome to AI-SustainableLiving!")
    
    user_interface = UserInterface()

    while True:
        choice = user_interface.main_menu()

        if choice == 1:
            user_profile = user_interface.create_user_profile()
            user_interface.display_user_profile(user_profile)
        elif choice == 2:
            user_id = user_interface.get_user_id()
            environmental_data = user_interface.collect_environmental_data()
            sustainability_factors = user_interface.predict_sustainability_factors(user_id, environmental_data)
            user_interface.display_sustainability_factors(sustainability_factors)
        elif choice == 3:
            user_id = user_interface.get_user_id()
            recommendations = user_interface.get_sustainability_recommendations(user_id)
            user_interface.display_recommendations(recommendations)
        elif choice == 4:
            print("Thank you for using AI-SustainableLiving!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
