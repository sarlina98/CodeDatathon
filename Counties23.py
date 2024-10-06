import pandas as pd
from openai import OpenAI # Ensure you have the OpenAI library installed

# Initialize OpenAI client
client = OpenAI()

# Define the file path for the CSV and the output file
file_path = r"C:\Users\sarli\Downloads\FullNames2023.csv"
output_file_path = r"C:\Users\sarli\Downloads\Counties2023.csv"

# Read the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Open the output file in append mode
with open(output_file_path, 'a') as output_file:
    # Iterate over each row in the DataFrame
    for index, row in data.iterrows():
        # Access city and state from the current row
        date = row[0]
        city = row['City']
        state = row['State']
        number = row['Number']

        # Create the prompt for the OpenAI API
        prompt = f"Answer only with the name of the county where the city '{city}', {state} is. Add nothing else."

        # Get the county name from OpenAI API
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the county name
        county_name = completion.choices[0].message.content.strip()

        # Format the output line
        output_line = f"Date: {date}, Number of Reportings: {number}, City: {city}, State: {state}, -> County: {county_name}\n"

        # Write the output line to the file
        output_file.write(output_line)

        # Optionally print to console as well
        print(output_line.strip())