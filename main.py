
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    file_path = input("Enter the path to your CSV file: ")
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        print(data.head())
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

def analyze_data(data):
    print("\nBasic Statistics:")
    print(data.describe())

    print("\nColumn Names:")
    print(data.columns)

    column = input("\nEnter a column name to visualize: ")
    if column in data.columns:
        data[column].plot(kind='hist', title=f"Distribution of {column}")
        plt.show()
    else:
        print("Invalid column name.")

def main():
    data = load_data()
    if data is not None:
        analyze_data(data)

if __name__ == "__main__":
    main()
