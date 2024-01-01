import pandas as pd
from googlesearch import search

#READS CSV
df = pd.read_csv('test.csv')

result = []
for index, row in df.iterrows():
    # Concatenate company name and address or change depending on your need
    query = f"{row['Name']} {row['Address']}"
    # Perform Google search using the concatenated query
    try:
        urls = list(search(query, tld="com", num=1, stop=1, pause=2))
        print(urls)
        if urls:
            result.append(urls[0])
        else:
            result.append(None)
    except Exception as e:
        print(f"An error occurred for {row['Name']}: {str(e)}")
        result.append(None)

# Create a new DataFrame with 'Company Name' and 'url'
df_result = pd.DataFrame({'Name': df['Name'], 'Website': result})

# Save the DataFrame to a CSV file
df_result.to_csv('Final.csv', index=False)
