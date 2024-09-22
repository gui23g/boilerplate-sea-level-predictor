import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Original Data')

    # Create first line of best fit
    slope, intercept = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])[:2]
    years_extended = pd.Series([i for i in range(1879, 2014 + 1)])
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Best fit line (1880-2013)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope, intercept = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])[:2]
    years_extended = pd.Series([i for i in range(1879, 2014)])
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Best fit line (1879-2013)')

    # Add labels and title
    plt.xlabel('Ano')
    plt.ylabel('Nível do mar (inches)')
    plt.title('Crescimento do nível do mar')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()