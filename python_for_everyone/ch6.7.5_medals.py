MEDALS = 3               # Number of medal types: Gold, Silver, Bronze
COUNTRIES = 8            # Total number of countries

# A list containing the names of the countries
countries = ["USA", "China", "Russia", "Germany", "France", "UK", "Japan", "Italy"]

# A 2D list where each row represents one country's medal counts
counts = [
    [0, 3, 0],           # USA: 0 Gold, 3 Silver, 0 Bronze
    [1, 2, 1],           # China: 1 Gold, 2 Silver, 1 Bronze
    [2, 1, 2],           # Russia: 2 Gold, 1 Silver, 2 Bronze
    [3, 0, 3],           # Germany: 3 Gold, 0 Silver, 3 Bronze
    [4, 0, 4],           # France: 4 Gold, 0 Silver, 4 Bronze
    [5, 0, 5],           # UK: 5 Gold, 0 Silver, 5 Bronze
    [6, 0, 6],           # Japan: 6 Gold, 0 Silver, 6 Bronze
    [7, 0, 7]            # Italy: 7 Gold, 0 Silver, 7 Bronze
]

# Print the table headings
print("Country Gold Silver Bronze Total")

# Loop through each country
for i in range(COUNTRIES):

    # Print the country name
    print("%10s" % countries[i], end="")

    # Reset the total medals for the current country
    total = 0

    # Loop through the three medal counts
    for j in range(MEDALS):

        # Print the current medal count
        print("%8d" % counts[i][j], end="")

        # Add the medal count to the country's total
        total = total + counts[i][j]

    # Print the total number of medals for the country
    print("%8d" % total)