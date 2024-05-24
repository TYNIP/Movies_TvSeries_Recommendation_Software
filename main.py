from dataProcessing import read_csv, process_data
from search import recommend

def get_user_input(prompt):
    return input(prompt).strip()

def main():
    file_path = 'netflix_titles.csv'
    data = read_csv(file_path)
    index = process_data(data)
    
    print("Hello! Welcome to the Netflix Recommendation System.")
    name = get_user_input("What's your name? ")
    print(f"Hi {name}!")
    print()
    
    while True:
        search_params = {}
        
        type_choice = get_user_input("Are you interested in Movies or TV Shows? ").capitalize()
        if type_choice in ['Movie', 'TV Show']:
            search_params['type'] = type_choice
        
        first_criteria = get_user_input("How would you like to search? (director, cast, listed_in): ").lower()
        first_value = get_user_input(f"Enter the {first_criteria}: ")
        search_params[first_criteria] = first_value
        
        add_second_param = get_user_input("Do you want to add a second search parameter? (yes/no): ").lower()
        if add_second_param == 'yes':
            second_criteria = get_user_input("Enter a second search criteria (director, cast, listed_in): ").lower()
            second_value = get_user_input(f"Enter the {second_criteria}: ")
            search_params[second_criteria] = second_value
        
        start = 0
        limit = 5
        
        while True:
            recommendations = recommend(index, search_params, start, limit)
            if recommendations:
                print("Here are some recommendations for you:")
                print()
                for i, rec in enumerate(recommendations, start=1):
                    print(f"{i}. {rec['title']} ({rec['release_year']}) - {rec['listed_in']}")
            else:
                print()
                print("No more recommendations found based on your criteria.")
            
            next_step = get_user_input("What would you like to do next? (1: More recommendations, 2: New search, 3: Exit): ")
            if next_step == '1':
                start += limit
                additional_recommendations = recommend(index, search_params, start, limit)
                if not additional_recommendations:
                    print("No more recommendations found of this type.")
                    start = 0
            elif next_step == '2':
                break
            elif next_step == '3':
                print()
                print("Thanks for using our software. Have A Good Day. Goodbye!")
                return

if __name__ == "__main__":
    main()
