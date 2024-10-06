import pandas as pd
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Define the file path
file_path = r"C:\Users\sarli\Downloads\FullNames2014.csv"

# Read the CSV file
data = pd.read_csv(file_path)


# Iterate over each row in the DataFrame
for index, row in data.iterrows():
    # Access city and state from the current row
    city = row['City']
    state = row['State']

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

    # Print the extracted county name
    print(f"City: {city}, State: {state} -> County: {county_name}")
    