import configparser
import os
import csv
import logging
import sys
import datetime
import pandas as pd
import shutil

class DeleteVideo:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.file_age = int(self.config.get('INTERVAL', 'file_age'))
        self.events_path = str(self.config.get('EVENTS_PATH', 'events_path'))
        self.csv_filename = "events_files.csv"
        self.today_date = datetime.datetime.today()
        # Configure logging
        logging.basicConfig(
            filename='delete_events.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s'
        )

    def create_blank_csv(self, csv_name):
        if os.path.exists(csv_name):
            # Backup the existing file with a timestamp
            backup_name = f"backup_{datetime.datetime.now().strftime('%Y_%m_%d')}_{csv_name}"
            os.rename(csv_name, backup_name)
            logging.info(f"Existing CSV file '{csv_name}' renamed to '{backup_name}'.")
        try:
            with open(csv_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['EVENTS_FOLDER_PATH', 'CREATED_DATE', 'EVENTS_AGE'])
            logging.info(f"CSV file '{csv_name}' created successfully.")
        except Exception as e:
            logging.error(f"Error: {e}")

    def get_events_dir(self):
        try:
            with os.scandir(self.events_path) as paths:
                data = []
                for events_dir in paths:
                    if events_dir.name.isnumeric() and events_dir.is_dir():
                        complete_path=os.path.join(self.events_path,events_dir.name)
                        file_creation_time=datetime.datetime.fromtimestamp(os.path.getctime(complete_path))
                        time_diff=(self.today_date-file_creation_time).days
                        if time_diff > self.file_age:
                            data.append([complete_path, str(file_creation_time), time_diff])
                self.create_blank_csv(self.csv_filename)
                with open(self.csv_filename, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(data)
                self.delete_events_folder()
            logging.info("Process completed successfully.")
        except Exception as e:
            logging.error(f"Error: {e}")

    def delete_events_folder(self):
        try:
            df = pd.read_csv(self.csv_filename)
            for index, row in df.iterrows():
                folder_path = row['EVENTS_FOLDER_PATH']
                if os.path.exists(folder_path):
                    # Delete the folder
                    shutil.rmtree(folder_path)
                    logging.info(f"Deleted folder: {folder_path}")
        except Exception as e:
            logging.error(f"Error: {e}")

def main():
    ps = DeleteVideo()
    ps.get_events_dir()

if __name__ == "__main__":
    main()

