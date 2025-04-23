"""
Assignment Overview:

You are building a Dog Image Browser using the Dog CEO REST API.

The app should allow users to:
- View a list of all available dog breeds
- Get a random image of a breed
- Get a random image of a sub-breed

You will be using the Dog CEO API: https://dog.ceo/dog-api/

Your app should display a main menu with the following options:
1. Show all breeds
2. Get a random image from a breed
3. Get a random image from a sub-breed
4. Exit

The system should handle the following errors:
- Handling errors when a user enters an invalid menu option
- Handling errors when a user enters a breed that does not exist
- Handling errors when a user enters a sub-breed that does not exist
- Handling connection errors when calling the API

If there is an error you should print your own custom error message to the user and allow them to try again.
- Hint: you can use a while loop + try / except blocks to handle this

You should use try / except blocks to handle these errors.

You can either use the should use the requests library or the http.client library to make your requests

"""


import requests

def get_all_breeds():
    """GET request to fetch all dog breeds."""
    try:
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print("Error: Could not fetch breed list from API.")
        return {}

def get_random_image(breed):
    """GET request to fetch a random image from a breed."""
    # TODO: Make a request to https://dog.ceo/api/breed/{breed}/images/random
    # TODO: Return the image URL or handle 
    try:
        breed_url = f'https://dog.ceo/api/breed/{breed}/images/random'
        response = requests.get(breed_url)
        response.raise_for_status()
        data = response.json() 
        return data['message']
    except request.exceptions.RequestException:
        print(f'Error fetching image for breed {breed}')
        return {}


def get_random_sub_breed_image(breed, sub_breed):
    """GET request to fetch a random image from a sub-breed."""
    # TODO: Make a request to https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random
    # TODO: Return the image URL or handle errors
    try:
        sub_breed_url = f'https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random'
        response = requests.get(sub_breed_url)
        response.raise_for_status()
        data = response.json()
        return data['message']
    except request.exceptions.RequestException:
        print(f'Error fetching image for sub breed {sub_breed}')
        return {}



def show_breeds(breeds_dict):
    """Prints all available breeds 5 per line."""
    # TODO: Print all breeds (sorted), 5 per line
    # all_breeds = []
    # count = 0
    # for breed in breeds_dict:
    #     all_breeds.append(breed)
    #     count += 1
    #     if count == 5:
    #         all_breeds = sorted(all_breeds)
    #         print(f'{all_breeds[0]}, {all_breeds[1]}, {all_breeds[2]}, {all_breeds[3]}, {all_breeds[4]}')
    #         all_breeds.clear()
    #         count = 0
    sorted_breeds = sorted(breeds_dict.keys())
    for breed in range(0,len(sorted_breeds),5):
        print(','.join(sorted_breeds[breed:breed+5]))


def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Show all breeds")
        print("2. Get a random image from a breed")
        print("3. Get a random image from a sub-breed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            breeds = get_all_breeds()
            show_breeds(breeds)

        elif choice == "2":
            breeds = get_all_breeds()
            breed = input("Enter breed name: ").strip().lower()
            # TODO: Check if breed exists and fetch image
            breeds_dict = get_all_breeds()
            if breed in breeds_dict:
                url = get_random_image(breed)
                print(f'Random image URL for {breed}: {url}')
            # TODO: Print image URL or error message
            else:
                print(f'Error: Breed not found.')


        elif choice == "3":
            breeds = get_all_breeds()
            breed = input("Enter breed name: ").strip().lower()
            # TODO: Check if breed has sub-breeds
            # TODO: Ask for sub-breed, check if valid, then fetch image
            # TODO: Print image URL or error message
            if breed in breeds and breeds[breed]:
                sub_breed = input("Enter sub-breed name: ").strip().lower()
                if sub_breed in breeds[breed]:
                    url = get_random_sub_breed_image(breed, sub_breed)
                    print(f'Random image URL for {sub_breed}: {url}')
            elif breed in breeds:
                print(f'Error: Sub-breed not found.')
            else:
                print(f'Error: Breed does not exist.')


        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()

"""
Sources:
Thank you to Afsana in assistance for "show_breeds" & "elif choice == 3"
"""