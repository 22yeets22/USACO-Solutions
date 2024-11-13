import re
import os
import requests
from bs4 import BeautifulSoup
from pyperclip import copy
from urllib.parse import urlparse


def validate_url(url):
    try:
        result = urlparse(url)
        return result.hostname == 'usaco.org' and result.path.startswith('/index.php')
    except ValueError:
        return False


def fetch_problem_details(url):
    # Fetch the page
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        stdin_input = False

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Step 1: Find the div with class "panel" and extract the h2 tags (problem name)
        panel_div = soup.find('div', class_='panel')
        if panel_div:
            h2_tags = panel_div.find_all('h2')
            if len(h2_tags) >= 2:
                h2_text_1 = h2_tags[0].get_text(strip=True)
                h2_text_2 = h2_tags[1].get_text(strip=True)
                problem_name = f"{h2_text_1} {h2_text_2}"
            else:
                problem_name = "Error: Less than 2 h2 tags found inside the panel."
        else:
            problem_name = "Error: No div with class 'panel' found."

        # Step 2A: Find the div with class "prob-in-spec" and extract the first h4 (filename)
        problem_input_format_div = soup.find('div', class_='prob-in-spec')
        if problem_input_format_div:
            problem_input_filename_tag = problem_input_format_div.find('h4')
            if problem_input_filename_tag:
                problem_filename = problem_input_filename_tag.get_text(strip=True)

                # Step 2B: Use a regular expression to extract the FILENAME from the format "INPUT FORMAT (file FILENAME.in):"
                filename_match = re.search(r"file ([\w\d]+)\.in", problem_filename)
                if filename_match:
                    # Get the captured filename
                    filename = filename_match.group(1)
                else:
                    print('Filename not found, assuming coming from stdin.')
                    stdin_input = True
                    filename = problem_name.split('.')[-1].replace(" ", "").lower()
            else:
                filename = "Error: No h4 tag found inside 'prob-in-spec'."
        else:
            filename = "Error: No div with class 'prob-in-spec' found."
            
        # Step 3: Find the pre tag with class "in" and extract all the text (problem input)
        problem_input_tag = soup.find('pre', class_='in')
        if problem_input_tag:
            problem_input = problem_input_tag.get_text(strip=True)
        else:
            problem_input = "Error: No pre tag with class 'in' found."
        
        # Return all gathered data
        return problem_name, filename, problem_input, stdin_input
    else:
        return f"Error: Unable to fetch the page. Status code: {response.status_code}", "", ""


def ask_yes_no(prompt):
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ['y', 'n']:
            return True if answer == 'y' else False
        

def create_boilerplate_file(contest_name, constest_input, contest_link, filename, stdin_input):
    # Get the current working directory and move one level up
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
    
    # Create the new folder in the parent directory
    new_folder_path = os.path.join(parent_directory, 'problems', filename)

    if os.path.isdir(new_folder_path):
        print(f"Folder {filename} already exists.")
        if not ask_yes_no("Do you want to overwrite it?"):
            return False
    
    os.makedirs(new_folder_path, exist_ok=True)
    
    # Define the full path to the boilerplate file
    boilerplate_file_path = os.path.join(new_folder_path, filename + ".py")
    input_file_path = os.path.join(new_folder_path, filename + ".in")

    # Define the boilerplate template
    boilerplate_name = 'boilerplate-new.txt' if stdin_input else 'boilerplate-old.txt'
    with open(os.path.join(current_directory, boilerplate_name), 'r') as f:
        boilerplate = f.read()
    boilerplate = "\n".join(boilerplate.split("\n")[4:])  # Remove first four lines

    # Replace placeholders with actual inputs
    boilerplate = boilerplate.format(
        contest_name=contest_name,
        contest_link=contest_link,
        filename=filename,
    )
    
    # Write the modified boilerplate to the file in the new folder
    with open(boilerplate_file_path, "w") as f:
        f.write(boilerplate)
        print(f"Boilerplate written to {boilerplate_file_path} successfully.")

    # Write the problem input to the file in the new folder
    with open(input_file_path, "w") as f:
        f.write(constest_input)
        print(f"Input written to {input_file_path} successfully.")
    
    return True


if __name__ == "__main__":
    # Get the problem link from the user
    url = input("Enter the USACO problem URL: ").strip()
    
    if validate_url(url):
        # Fetch and display the problem details
        problem_name, filename, problem_input, stdin_input = fetch_problem_details(url)
        print("Problem name:", problem_name)
        print("Extracted filename:", filename)
        print("(Sample) Problem input:\n" + problem_input)
        print("Input comes from terminal:", stdin_input)

        if not ask_yes_no("Does this look correct?"):
            if not ask_yes_no("Is the problem name correct?"):
                if ask_yes_no("Do you want to enter the problem name manually?"):
                    problem_name = input("Enter the problem name: ").strip()
                else:
                    problem_name = 'DEFAULT'
            if not ask_yes_no("Is the filename correct?"):
                if ask_yes_no("Do you want to enter the filename manually?"):
                    filename = input("Enter the filename: ").strip()
                else:
                    filename = 'DEFAULT'
            if not ask_yes_no("Is the problem input correct?"):
                if ask_yes_no("Do you want to enter the problem input manually?"):
                    problem_input = input("Enter the problem input: ").strip()
                else:
                    problem_input = 'DEFAULT'
            if not ask_yes_no("Is the terminal input section correct?"):
                stdin_input = ask_yes_no("Does the input come from terminal?")
        
        # Write to a file
        success = create_boilerplate_file(problem_name, problem_input, url, filename, stdin_input)

        if success:
            if ask_yes_no("Do you want to copy VSCode commands?"):
                copy(f"cd problems/{filename}")
            print("Sucessfully completed all operations!")
        else:
            print("Failed to create the boilerplate file.")
    else:
        print("Invalid URL. Please enter a valid USACO problem URL.")
