import pandas as pd

class DataAnalizer:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print("loaded successfully.")
        except Exception as e:
            print("Can't load date:", e)

    def convert_to_parquet(self, parquet_path):
        if self.data is not None:
            self.data.to_parquet(parquet_path, engine="pyarrow", index=False)
            print(f"Data converted to Parquet")
        else:
            print("Load data before converting to Parquet.")

    def compute_statistics(self):
        if self.data is not None:
            numeric_data = self.data.select_dtypes(include="number")
            stats = pd.DataFrame({
                "Max": numeric_data.max(),
                "Min": numeric_data.min(),
                "Average": numeric_data.mean(),
                "Absolute": numeric_data.abs().max()  # max absolute value
            })
            return stats
        else:
            print("Load data!")
            return None
def main():
        processor = DataAnalizer(r"C:\Users\DELL\Documents\02082025_SoftwareEngineering\3week\google_review_ratings.csv")
    
        processor.get_data()
    
        processor.convert_to_parquet("dataset.parquet")
    
        stats = processor.compute_statistics()
        if stats is not None:
            print(stats)

if __name__ == "__main__":
    main()


