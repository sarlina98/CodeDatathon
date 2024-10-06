import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;

public class CSVDateConverter {

    public static void main(String[] args) {

        String inputFilePath = "C:\\Users\\Pvt_A\\Downloads\\ConvertedCounties2023.csv";  
        String outputFilePath = "C:\\Users\\Pvt_A\\Downloads\\ConvertedCounties2023Dated.csv";     


        SimpleDateFormat inputDateFormat = new SimpleDateFormat("MM/dd/yyyy"); 
        SimpleDateFormat outputDateFormat = new SimpleDateFormat("yyyy-MM-dd");


        int expectedColumns = 10; 

        try (BufferedReader br = new BufferedReader(new FileReader(inputFilePath));
             FileWriter writer = new FileWriter(outputFilePath)) {

 
            String header = br.readLine();
            if (header != null) {
                writer.append(header).append("\n");
            }


            String line;
            while ((line = br.readLine()) != null) {

                String[] columns = line.split(",");

        
                if (columns.length < expectedColumns) {
            
                    String[] newColumns = new String[expectedColumns];
                    System.arraycopy(columns, 0, newColumns, 0, columns.length);
                    for (int i = columns.length; i < expectedColumns; i++) {
                        newColumns[i] = "";  
                    }
                    columns = newColumns;
                }

               
                String date = columns[0];

                
                try {
                    String formattedDate = outputDateFormat.format(inputDateFormat.parse(date));
                    columns[0] = formattedDate; 
                } catch (ParseException e) {
                    System.out.println("Invalid date format for: " + date);
                    
                    continue; 
                }

               
                writer.append(String.join(",", columns)).append("\n");
            }

            System.out.println("CSV file with updated date format created successfully: " + outputFilePath);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

