
import csv

# Open the CSV file for reading
with open('file_name_copy.csv', 'r') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)
    
    # Skip the header line if it exists
    next(csv_reader, None)
    
    # Create an SQL file for writing
    with open('output.sql', 'w') as sql_file:
        # Iterate through each line in the CSV
        for row in csv_reader:
            if len(row) == 7:
                # Extract the values from the CSV row
                name, location, type, fk_host, road_num, local_road_num, pk_name = row
                
                # Create the SQL statement
                sql_statement = (
                    f"update sn_cameras "
                    f"set name='{name}', "
                    f"location='{location}', "
                    f"type='{type}', "
                    f"fk_host={fk_host}, "
                    f"channel={road_num}, "
                    f"local_channel={local_road_num} "
                    f"WHERE pk_camera={pk__name};\n"
                )
                
                # Write the SQL statement to the SQL file
                sql_file.write(sql_statement)

print("SQL statements have been saved to 'output.sql'.")
