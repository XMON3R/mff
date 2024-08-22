'''import pandas as pd
import matplotlib.pyplot as plt

# Načtení dat z CSV souboru
file_path = 'C:/Users/Pc.DESKTOP-U953URB/Desktop/onlyUnitsUSA.csv' # Změň na správnou cestu k souboru
data = pd.read_csv(file_path)

# Čištění dat a odstranění prázdných hodnot
clean_data = data.dropna(subset=['value_actual'])

# Převod hodnot na číselný formát (pokud nejsou)
clean_data['value_actual'] = pd.to_numeric(clean_data['value_actual'], errors='coerce')

# Přeformátování dat pro snadnější vykreslení
pivot_data = clean_data.pivot(index='year', columns='format', values='value_actual')

# Vykreslení grafu
plt.figure(figsize=(14, 8))

# Vybrané formáty pro vykreslení
formats_to_plot = ['CD', 'LP/EP', 'Cassette', 'Download Single', 'Vinyl Single']
for fmt in formats_to_plot:
    if fmt in pivot_data.columns:
        plt.plot(pivot_data.index, pivot_data[fmt], label=fmt)

plt.title('Prodejní trendy hlavních hudebních formátů v průběhu času')
plt.xlabel('Rok')
plt.ylabel('Prodeje (Jednotky)')
plt.legend()
plt.grid(True)
plt.show()

# Načtení dat z CSV souboru
file_path = 'C:/Users/Pc.DESKTOP-U953URB/Desktop/onlyUnitsUSA.csv'  # Změň na správnou cestu k souboru
data = pd.read_csv(file_path)

# Čištění dat a odstranění prázdných hodnot
clean_data = data.dropna(subset=['value_actual'])

# Převod hodnot na číselný formát (pokud nejsou)
clean_data['value_actual'] = pd.to_numeric(clean_data['value_actual'], errors='coerce')

# Přeformátování dat pro snadnější vykreslení
pivot_data = clean_data.pivot(index='year', columns='format', values='value_actual')

# Vytvoření grafu pro LP/EP od roku 1990 do 2019 s maximem 50 a kroky po 5
plt.figure(figsize=(10, 8))

# Filtrování dat pro roky 1990 až 2019
lp_ep_1990_2019 = pivot_data.loc[1990:2019, 'LP/EP']

# Vykreslení grafu
plt.plot(lp_ep_1990_2019.index, lp_ep_1990_2019, label='LP/EP')

plt.title('Prodejní trendy LP/EP (1990 - 2019) - Detailní pohled')
plt.xlabel('Rok')
plt.ylabel('Prodeje (Miliony prodaných kusů)')
plt.ylim(0, 25)
plt.yticks(range(0, 26, 5))  # Nastavení osy y s kroky po 5 jednotkách
plt.legend()
plt.grid(True)
plt.show()
'''


import pandas as pd
import matplotlib.pyplot as plt



# Načtení dat z CSV souboru
file_path = 'C:/Users/Pc.DESKTOP-U953URB/Desktop/onlyUnitsUSA.csv' # Změň na správnou cestu k souboru
data = pd.read_csv(file_path)

# Čištění dat a odstranění prázdných hodnot
clean_data = data.dropna(subset=['value_actual'])

# Převod hodnot na číselný formát (pokud nejsou)
clean_data['value_actual'] = pd.to_numeric(clean_data['value_actual'], errors='coerce')

# Přeformátování dat pro snadnější vykreslení
pivot_data = clean_data.pivot(index='year', columns='format', values='value_actual')

# Vykreslení grafu
plt.figure(figsize=(14, 8))

# Vybrané formáty pro vykreslení CD SINGLY ZVÁŽIT V POROVNÁNÍ S VINYLY!
formats_to_plot = ['LP/EP', 'Vinyl Single','8 - Track', 'Cassette', 'CD', 'Download Single']
for fmt in formats_to_plot:
    if fmt in pivot_data.columns:
        plt.plot(pivot_data.index, pivot_data[fmt], label=fmt)

plt.title('Prodejní trendy hlavních hudebních formátů v průběhu času')
plt.xlabel('Rok')
plt.ylabel('Prodeje (Jednotky)')
plt.legend()
plt.grid(True)
plt.show()


# Načtení dat z CSV souboru
file_path = 'C:/Users/Pc.DESKTOP-U953URB/Desktop/onlyUnitsUSA.csv' # Změň na správnou cestu k souboru
data = pd.read_csv(file_path)

# Čištění dat a odstranění prázdných hodnot
clean_data = data.dropna(subset=['value_actual'])

# Převod hodnot na číselný formát (pokud nejsou)
clean_data['value_actual'] = pd.to_numeric(clean_data['value_actual'], errors='coerce')

# Přeformátování dat pro snadnější vykreslení
pivot_data = clean_data.pivot(index='year', columns='format', values='value_actual')

# Vytvoření grafu pro LP/EP a další formáty od roku 1990 do 2019
plt.figure(figsize=(14, 8))

# Filtrování dat pro roky 1990 až 2019
lp_ep_1990_2019 = pivot_data.loc[1990:2019, 'LP/EP']

# Vykreslení LP/EP
plt.plot(lp_ep_1990_2019.index, lp_ep_1990_2019, label='LP/EP')

# Přidání dalších formátů pro srovnání
formats_to_plot = ['Vinyl Single','8 - Track', 'Cassette', 'CD']
for fmt in formats_to_plot:
    if fmt in pivot_data.columns:
        plt.plot(pivot_data.loc[1990:2019].index, pivot_data.loc[1990:2019, fmt], label=fmt)

plt.title('Prodejní trendy hudebních formátů (1990 - 2019) - Detailní pohled')
plt.xlabel('Rok')
plt.ylabel('Prodeje (Jednotky)')
plt.ylim(0, 50)
plt.yticks(range(0, 51, 5))  # Nastavení osy y s kroky po 5 jednotkách
plt.legend()
plt.grid(True)
plt.show()

# Vytvoření grafu pro LP/EP a další formáty od roku 1973 do 1990
plt.figure(figsize=(14, 8))

# Filtrování dat pro roky 1973 až 1990
lp_ep_1973_1990 = pivot_data.loc[1973:1990, 'LP/EP']

# Vykreslení LP/EP
plt.plot(lp_ep_1973_1990.index, lp_ep_1973_1990, label='LP/EP')

# Přidání dalších formátů pro srovnání
for fmt in formats_to_plot:
    if fmt in pivot_data.columns:
        plt.plot(pivot_data.loc[1973:1990].index, pivot_data.loc[1973:1990, fmt], label=fmt)


plt.title('Prodejní trendy hlavních hudebních formátů v průběhu času')
plt.xlabel('Rok')
plt.ylabel('Prodeje (Jednotky)')
plt.legend()
plt.yticks(range(0, 501, 50))
plt.grid(True)
plt.show()

'''
plt.title('Prodejní trendy hudebních formátů (1973 - 1990) - Detailní pohled')
plt.xlabel('Rok')
plt.ylabel('Prodeje (Jednotky)')
plt.ylim(0, 50)
plt.yticks(range(0, 51, 5))  # Nastavení osy y s kroky po 5 jednotkách
plt.legend()
plt.grid(True)
plt.show()
'''

'''

import csv
import pandas as pd

# Load the CSV file into a DataFrame
#fileLocation = 'C:/Users/Pc.DESKTOP-U953URB/Desktop/musicdata.csv'

fileLocation = 'C:/Users/Pc.DESKTOP-U953URB/Desktop/onlyUnitsUSA.csv'
music_data = pd.read_csv(fileLocation)


def display_sales_by_year(year):
    # Filter data for the given year
    data_year = music_data[music_data['year'] == year].dropna(subset=['value_actual'])
    
    # Calculate the total sales for the year
    total_sales = data_year['value_actual'].sum()
    
    # Create the formatted output
    output = f"{year}\n"
    for _, row in data_year.iterrows():
        format_name = row['format']
        sales = row['value_actual']
        percentage = (sales / total_sales) * 100
        output += f"Format: {format_name}, Sold: {sales:.2f} million units, Percentage of the whole year: {percentage:.2f}%\n"
    
    return output

def years_display(start_year, end_year):
    # Filter data for the given year
    for year in range(end_year - start_year):
        data_year = music_data[music_data['year'] == year].dropna(subset=['value_actual'])
    
        # Calculate the total sales for the year
        total_sales = data_year['value_actual'].sum()
    
        # Create the formatted output
        output = f"{year}\n"
        for _, row in data_year.iterrows():
            format_name = row['format']
            sales = row['value_actual']
            percentage = (sales / total_sales) * 100
            output += f"Format: {format_name}, Sold: {sales:.2f} million units, Percentage of the whole year: {percentage:.2f}%\n"
    
        print(output)


def find_most_popular_format_per_year():
    # Get the unique years from the dataset
    years = music_data['year'].unique()
    
    for year in years:
        # Filter data for the current year
        data_year = music_data[music_data['year'] == year].dropna(subset=['value_actual'])
        
        # Dictionary to keep track of format and its sales
        sales_dict = {}
        
        # Populate the dictionary with format and corresponding sales
        for _, row in data_year.iterrows():
            format_name = row['format']
            sales = row['value_actual']
            sales_dict[format_name] = sales_dict.get(format_name, 0) + sales
        
        # Find the format with the maximum sales
        if sales_dict:
            most_popular_format = max(sales_dict, key=sales_dict.get)
            most_popular_sales = sales_dict[most_popular_format]
            
            # Print the most popular format and its sales for the current year
            print(f"Year: {year}, Most Popular Format: {most_popular_format}, Sold: {most_popular_sales:.2f} million units")
        
        # Clear the dictionary for the next year
        sales_dict.clear()

# Run the function to find and print the most popular format for each year
#find_most_popular_format_per_year()

# Example for the year 1983
#sales_1973 = display_sales_by_year(1983)
#print(sales_1973)

all_sales = years_display(1973,1983)
'''




'''
with open(fileLocation, "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        try: # we need to test if row 11 and 12 has data, some movies doesn't have both or any data
            budget = float(row[11])
            revenue = float(row[12])

            if budget > 0 and revenue > 0:
                profit = revenue - budget # profit should be without cost of movie
                ratio = profit / budget # our ratio we would like to study
                
                if budget >= valueOfExpensiveMovie: # the threshold when we consider movie expensive
                    expensiveMovieRatios.append(ratio)
                else:
                    cheapMovieRatios.append(ratio)
                    
        except ValueError: # we want to skip movies without valid data
            continue



'''


'''
import pandas as pd

# Načtení CSV souboru
file_path = 'C:/Users/Pc.DESKTOP-U953URB/Desktop/musicdata.csv'
df = pd.read_csv(file_path)

'''


'''

import csv

# Define the file path and the column name you want to extract
file_path = 'C:/Users/Pc.DESKTOP-U953URB/Desktop/musicdata.csv'
column_name1 = 'value_actual'  # This will be for "sold"
column_name2 = 'format'  # This will be for "Format"
column_name3 = 'year'  # This will be for "year"

# Initialize an empty list to store the formatted column data
formatted_data = []

# Open the CSV file
with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)  # Use DictReader to handle CSV as dictionaries
    
    # Check if the columns exist
    if column_name1 not in reader.fieldnames:
        raise ValueError(f"Column '{column_name1}' does not exist in the CSV file.")
    if column_name2 not in reader.fieldnames:
        raise ValueError(f"Column '{column_name2}' does not exist in the CSV file.")
    if column_name3 not in reader.fieldnames:
        raise ValueError(f"Column '{column_name3}' does not exist in the CSV file.")
    
    # Extract the data from the desired columns and format it
    for row in reader:
        formatted_data.append(f"Format: {row[column_name2]}, sold: {row[column_name1]}, year: {row[column_name3]}")

# Print the formatted column data
for item in formatted_data:
    print(item)

'''

''' 

# Sloučení Single kategorií do jejich hlavních kategorií

df['Cassette'] = df.get('Cassette', 0) + df.get('Cassette Single', 0)
df['Vinyl'] = df.get('Vinyl', 0) + df.get('Vinyl Single', 0)
df['CD'] = df.get('CD', 0) + df.get('CD Single', 0) + df.get('SACD', 0)



# Odstranění nepotřebných sloupců
df = df.drop(columns=['Music Video', 'DVD Audio', 'Cassette Single', 'Vinyl Single', 'CD Single', 'SACD'], errors='ignore')

'''