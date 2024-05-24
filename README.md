# Netflix Recommendation System

## Overview

The Netflix Recommendation System is a Python-based application that suggests movies and TV shows to users based on their preferences. The application uses a CSV file containing details about various Netflix titles to provide personalized recommendations.

**CSV file by M Rahul Vyas taken from Kaggle**

**Currently Runs In Terminal**

## Features
- Asks the user for their name and preferred type (Movie or TV Show).
- Allows users to search based on one or two criteria (director, cast, listed_in).
- Provides up to 5 recommendations at a time.
- Allows users to request more recommendations, perform a new search, or exit the application.

## Data

The recommendation system uses a CSV file (`netflix_titles.csv`) with the following columns:
- `show_id`: A unique identifier for each title.
- `type`: The category of the title (Movie or TV Show).
- `title`: The name of the movie or TV show.
- `director`: The director(s) of the movie or TV show.
- `cast`: The list of main actors/actresses in the title.
- `country`: The country or countries where the movie or TV show was produced.
- `date_added`: The date the title was added to Netflix.
- `release_year`: The year the movie or TV show was originally released.
- `rating`: The age rating of the title.
- `duration`: The duration of the title, in minutes for movies and seasons for TV shows.
- `listed_in`: The genres the title falls under.
- `description`: A brief summary of the title.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/tynip/Movies_TvSeries_Recommendation_Software.git
    cd netflix-recommendation-system
    ```

## Usage
1. Ensure the `netflix_titles.csv` file is in the same directory as the script.
2. Run the script:
    ```sh
    python main.py
    ```

3. Follow the on-screen prompts:
    - Enter your name.
    - Choose between Movies or TV Shows.
    - Provide the first search criterion (director, cast, or listed_in).
    - Optionally, provide a second search criterion.
    - View the recommendations and choose to see more, start a new search, or exit.

## Example

```sh
Hello! Welcome to the Netflix Recommendation System.
What's your name? Tynip
Hi Tynip!
Are you interested in Movies or TV Shows? Movie
How would you like to search? (director, cast, listed_in): director
Enter the director: Christopher Nolan
Do you want to add a second search parameter? (yes/no): yes
Enter a second search criteria (director, cast, listed_in): listed_in
Enter the listed_in: Action & Adventure
Here are some recommendations for you:
1. Inception (2010) - Action & Adventure, Sci-Fi
...
What would you like to do next? (1: More recommendations, 2: New search, 3: Exit): 1
No more recommendations found of this type.
What would you like to do next? (1: More recommendations, 2: New search, 3: Exit): 3
Thanks for using our software. Have A Good Day. Goodbye!
...
```

## Considerations
- CSV file by [M Rahul Vyas](https://www.kaggle.com/rahulvyasm/datasets) taken from Kaggle
- Project with academic and practical purposes.