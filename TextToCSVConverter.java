import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
//this was created to remove the county word that would be added after running throught the LLM API I would have used python but I
//couldnt get it to properly compile this weekend :P
public class TextToCSVConverter {

    public static void main(String[] args) {
        String inputFilePath = "C:\\Users\\Pvt_A\\Downloads\\Counties2023.csv";  // Replace with your text file path
        String outputFilePath = "C:\\Users\\Pvt_A\\Downloads\\ConvertedCounties2023.csv"; // Replace with your desired output CSV file path

        try (BufferedReader br = new BufferedReader(new FileReader(inputFilePath));
             FileWriter writer = new FileWriter(outputFilePath)) {

            // Write the CSV header (if needed)
            writer.append("Date,Reportings,City,State,County\n");

            String line;

            while ((line = br.readLine()) != null) {
                // Split the line by commas
                String[] parts = line.split(",", -1); // -1 to keep trailing empty strings

                if (parts.length >= 5) { // Check if the line contains at least 5 columns
                    String date = parts[0].trim();       // Date column
                    String reportings = parts[1].trim(); // Reportings column
                    String city = parts[2].trim();       // City column
                    String state = parts[3].trim();      // State column
                    String county = parts[4].trim();     // County column

                    // Remove " County" from the county string if it exists
                    if (county.endsWith(" County")) {
                        county = county.substring(0, county.length() - 7).trim(); // Remove the " County" suffix
                    }

                    // Rebuild the CSV line with the cleaned data
                    writer.append(String.join(",", date, reportings, city, state, county)).append("\n");
                }
            }

            System.out.println("CSV file created successfully: " + outputFilePath);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
