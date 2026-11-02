import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesdataAnalayzer:
    def __init__(self):
        self.data = None
        self.fig = None

    def load_dataset(self):
        try:
            file_path = input("Enter the CSV file path: ")
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
            print()
        except Exception:
            print("Enter the correct file path.")

    def explore_dataset(self):
        if self.data is None:
            print("Load the dataset first.")
            return

        print("Select an option:")
        print("1. For first 5 rows")
        print("2. For last 5 rows")
        print("3. For column names")
        print("4. For datatypes")
        print("5. For dataset info")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("The top 5 rows:\n", self.data.head())
            print()
        elif choice == 2:
            print("The last 5 rows:\n", self.data.tail())
            print()
        elif choice == 3:
            print("Column names:", self.data.columns)
            print()
        elif choice == 4:
            print(f"The datatypes are:\n{self.data.dtypes}")
            print()
        elif choice == 5:
            print("Dataset info:")
            self.data.info()
            print()
        else:
            print("Invalid choice.")

    def perform_dataset_opreatons(self):
        if self.data is None:
            print("First load the dataset.")
            return

        print("Select an option:")
        print("1. Describe the dataset")
        print("2. Dataset shape")
        print("3. Rename a column")
        print("4. Split data by Region")
        print("5. Search / Sort / Filter")
        print("6. Group by Region (sum, mean, count)")
        print("7. Pivot table")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Dataset Description:\n{self.data.describe()}")
            print()

        elif choice == 2:
            print(f"Dataset Shape: {self.data.shape}")
            print()
            
        elif choice == 3:
            old_name = input("Enter the column name to rename: ")
            new_name = input("Enter the new column name: ")
            if old_name in self.data.columns:
                self.data = self.data.rename(columns={old_name: new_name})
                print("Column renamed successfully.")
                print()
            else:
                print("Column not found.")

        elif choice == 4:
            region = input("Enter the region to filter by: ")
            divided_data = self.data[self.data['Region'] == region]
            print(divided_data)
            print()

        elif choice == 5:
            print("1. Search by Region")
            print("2. Sort by Sales")
            print("3. Filter by Sales greater than a value")
            sub_choice = int(input("Enter your choice: "))
            print()

            if sub_choice == 1:
                region = input("Enter the region to search for: ")
                filtered_data = self.data[self.data['Region'] == region]
                print(filtered_data)
                print()

            elif sub_choice == 2:
                sorted_data = self.data.sort_values(by='Sales', ascending=False)
                print(sorted_data)
                print()

            elif sub_choice == 3:
                value = float(input("Enter the sales value to filter by: "))
                filtered_data = self.data[self.data['Sales'] > value]
                print(filtered_data)
                print()

            else:
                print("Invalid choice.")

        elif choice == 6:
            grouped_data = self.data.groupby('Region').agg({'Sales': ['sum', 'mean', 'count']})
            print(grouped_data)
            print()

        elif choice == 7:
            index_col = input("Enter the column name for index: ")
            columns_col = input("Enter the column name for columns: ")
            values_col = input("Enter the column name for values: ")
            pivot_table = pd.pivot_table(self.data, index=index_col, columns=columns_col, values=values_col, aggfunc='sum')
            print()
            print(f"Pivot Table:\n{pivot_table}")
            print()

        else:
            print("Invalid choice.")

    def handel_missing_data(self):
        if self.data is None:
            print("First load the dataset.")
            return

        print("=== Handel missing data/ For clean data ===")
        print("Select an option: ")
        print("1. Display rows With Missing Values ")
        print("2. Fill missing Values with mean")
        print("3. Drop rows with Missing Values")
        print("4. Replace Missing Values with a Specific Value ")
        print()
        choice = int(input("Enter your Choice: "))
        print()
        if choice == 1:
            if self.data.isna().sum().sum() == 0:
                print("No missing value found in the dataset!")
                print()
            else:
                null = self.data[self.data.isna().any(axis=1)]
                print(null)
                
        elif choice == 2:
            self.data = self.data.fillna(self.data.mean(numeric_only=True))
            print(self.data)
            print()

        elif choice == 3:
            print("Before clearing data")
            print(self.data.isnull().sum())
            self.data = self.data.dropna()
            print()
            print("After cleaning data")
            print(self.data.isnull().sum())
            print()

        elif choice == 4:
            update_value = input("Enter a Value to Replaceit with Missing Value: ")
            self.data = self.data.fillna(update_value)
            print(f"Missing Values Replaced with {update_value} Successfully!")
            print()

        else:
            print("Please enter a valid choice..")

    def statistical_operation(self):
        if self.data is None:
            print("First load the dataset.")
            return

        print("=== Statistical Operations ===")
        print("1. Standard Deviation")
        print("2. Variance")
        print("3. Percentile")
        print("4. Quantile")
        print("5. Describe")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Standard Deviation: {self.data['Sales'].std()}")
            print()

        elif choice == 2:
            print(f"Variance: {self.data['Sales'].var()}")
            print()

        elif choice == 3:
            print(f"90th Percentile: {np.percentile(self.data['Sales'], 90)}")
            print()

        elif choice == 4:
            print(f"75th Quantile: {self.data['Sales'].quantile(0.75)}")
            print()
        elif choice == 5:
            print(f"Description: {self.data['Sales'].describe()}")
            print()

        else:
            print("Invalid Choice!")

    def visualize_data(self):
        
        if self.data is None:
          print("First load the dataset.")
          return
      
        print(self.data.columns)
        print()
        print("=== Data Visualization ===")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        print("7. Box Plot")
        print("8. Heatmap")
    
        choice = int(input("Enter your choice: "))
        title = input("Enter Chart Title: ")
        plt.figure(figsize=(10, 5))

        if choice == 1:
            x = input("Enter x-axis column: ")
            y = input("Enter y-axis column: ")
            self.data.groupby(x)[y].sum().plot(kind="bar")
    
        elif choice == 2:
            x = input("Enter x-axis column: ")
            y = input("Enter y-axis column: ")
            self.data.plot(x=x, y=y, kind="line")
    
        elif choice == 3:
            x = input("Enter x-axis column: ")
            y = input("Enter y-axis column: ")
            self.data.plot(x=x, y=y, kind="scatter")
    
        elif choice == 4:
            col = input("Enter column name: ")
            self.data[col].value_counts().plot(kind="pie", autopct="%.2f%%")
            plt.legend(title=col, bbox_to_anchor=(1.05, 1), loc="upper left")
    
        elif choice == 5:
            col = input("Enter column name: ")
            self.data[col].plot(kind="hist", bins=10, alpha=0.7)
            plt.ylabel("Frequency")
    
        elif choice == 6:
            x = input("Enter x-axis column: ")
            y = input("Enter y-axis column: ")
        
            data = self.data.pivot_table(
                index=x,
                columns="Product",
                values=y,
                aggfunc="sum"
            )
            data.plot(kind="area", stacked=True, ax=plt.gca())
            plt.xlabel(x)
            plt.ylabel(y)
            plt.legend(title="Product", bbox_to_anchor=(1.05, 1), loc="upper left")
       
        elif choice == 7:
               x = input("Enter x-axis column: ")
               y = input("Enter y-axis column: ")
               sns.boxplot(x=x, y=y, data=self.data)
    
        elif choice == 8:
            sns.heatmap(self.data.corr(numeric_only=True), annot=True, cmap="coolwarm")
    
        else:
            print("Invalid choice.")
            return
    
        plt.title(title)
        plt.tight_layout()
        self.fig = plt.gcf()
        plt.show()
        print("Chart Generated Successfully!")

    def save_visualization(self):
        print("=== Save Visualization ===")
        if self.fig is None:
            print("Generate a visualization first.")
            return
        file_name = input("Enter the file name to save the visualization (with extension .png or .jpg): ")
        self.fig.savefig(file_name)
        print(f"Visualization saved as {file_name} successfully.")
        print()

    def options(self):
        print("="*10, "Data Analysis & Visualization Program", "="*10)
        print(" Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("="*35)
        print()

    def menu(self):
        while True:
            self.options()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.load_dataset()
            elif choice == 2:
                self.explore_dataset()
            elif choice == 3:
                self.perform_dataset_opreatons()
            elif choice == 4:
                self.handel_missing_data()
            elif choice == 5:
                self.statistical_operation()
            elif choice == 6:
                self.visualize_data()
            elif choice == 7:
                self.save_visualization()
            elif choice == 8:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    obj = SalesdataAnalayzer()
    obj.menu()
    
    