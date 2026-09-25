import csv
import os


class CSVReader:

    @staticmethod
    def read_csv(filename):

        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "test_data",
            filename
        )

        with open(
            file_path,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            data = []

            for row in reader:

                data.append(row)

            return data