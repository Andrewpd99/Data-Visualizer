import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    """Loads data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        print(data.head())  # Display the first few rows of the dataset
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def plot_line_chart(data, x_col, y_col):
    """Creates a line chart."""
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_col], data[y_col], marker='o')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'Line Chart of {y_col} vs {x_col}')
    plt.grid(True)
    plt.show()

def plot_bar_chart(data, x_col, y_col):
    """Creates a bar chart."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_col, y=y_col, data=data)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'Bar Chart of {y_col} vs {x_col}')
    plt.xticks(rotation=45)
    plt.show()

def plot_scatter_plot(data, x_col, y_col):
    """Creates a scatter plot."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, data=data)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'Scatter Plot of {y_col} vs {x_col}')
    plt.grid(True)
    plt.show()

def plot_histogram(data, col):
    """Creates a histogram."""
    plt.figure(figsize=(10, 6))
    sns.histplot(data[col], kde=True)
    plt.xlabel(col)
    plt.title(f'Histogram of {col}')
    plt.show()

def plot_interactive(data, x_col, y_col):
    """Creates an interactive plot using Plotly."""
    fig = px.scatter(data, x=x_col, y=y_col, title=f'Interactive Plot of {y_col} vs {x_col}')
    fig.show()

def main():
    # Replace 'your_file.csv' with your actual data file path
    file_path = 'your_file.csv'
    data = load_data(file_path)
    
    if data is not None:
        # Choose the columns you want to visualize
        x_col = input("Enter the column name for X-axis: ")
        y_col = input("Enter the column name for Y-axis: ")

        # Plot options
        plot_options = {
            1: plot_line_chart,
            2: plot_bar_chart,
            3: plot_scatter_plot,
            4: plot_histogram,
            5: plot_interactive
        }

        print("\nChoose a plot type:")
        print("1: Line Chart")
        print("2: Bar Chart")
        print("3: Scatter Plot")
        print("4: Histogram")
        print("5: Interactive Plot")

        try:
            choice = int(input("Enter the number of your choice: "))
            if choice in plot_options:
                if choice == 4:  # Histogram requires only one column
                    plot_options[choice](data, x_col)
                else:
                    plot_options[choice](data, x_col, y_col)
            else:
                print("Invalid choice. Please select a valid plot type.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
