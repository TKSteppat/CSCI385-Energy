import pandas as pd
import os
import requests
import os
from dotenv import load_dotenv

# .env file should have the api key, obviously not included in the repo
load_dotenv(dotenv_path=".env")

if __name__ == "__main__":
    offset = 0
    keep_scraping = True
    main_df = pd.DataFrame()
    while keep_scraping:
        # API call to EIA 
        # Annual data, States+DC only, 2015-2025 (We can change this later)
        response = requests.get(f"https://api.eia.gov/v2/electricity/retail-sales/data/?frequency=annual&data[0]=customers&data[1]=price&data[2]=revenue&data[3]=sales&facets[stateid][]=AK&facets[stateid][]=AL&facets[stateid][]=AR&facets[stateid][]=AZ&facets[stateid][]=CA&facets[stateid][]=CO&facets[stateid][]=CT&facets[stateid][]=DC&facets[stateid][]=DE&facets[stateid][]=FL&facets[stateid][]=GA&facets[stateid][]=HI&facets[stateid][]=IA&facets[stateid][]=ID&facets[stateid][]=IL&facets[stateid][]=IN&facets[stateid][]=KS&facets[stateid][]=KY&facets[stateid][]=LA&facets[stateid][]=MA&facets[stateid][]=MD&facets[stateid][]=ME&facets[stateid][]=MI&facets[stateid][]=MN&facets[stateid][]=MO&facets[stateid][]=MS&facets[stateid][]=MT&facets[stateid][]=NC&facets[stateid][]=ND&facets[stateid][]=NE&facets[stateid][]=NH&facets[stateid][]=NJ&facets[stateid][]=NM&facets[stateid][]=NV&facets[stateid][]=NY&facets[stateid][]=OH&facets[stateid][]=OK&facets[stateid][]=OR&facets[stateid][]=PA&facets[stateid][]=RI&facets[stateid][]=SC&facets[stateid][]=SD&facets[stateid][]=TN&facets[stateid][]=TX&facets[stateid][]=UT&facets[stateid][]=VA&facets[stateid][]=VT&facets[stateid][]=WA&facets[stateid][]=WI&facets[stateid][]=WV&facets[stateid][]=WY&start=2015&sort[0][column]=period&sort[0][direction]=desc&offset={offset*5000}&length=5000&api_key={os.getenv('EIA_API_KEY')}")
        data = response.json()["response"]["data"]  
        total = response.json()["response"]["total"]
        # Can only get 5000 rows at a time
        # Offset is used to keep track of where we are in the scrape
        # If we have scraped all the rows, we set keep scraping to false
        if (offset+1)*5000 < int(total):
            offset += 1
        else:
            keep_scraping = False
        df = pd.json_normalize(data)
        main_df = pd.concat([main_df, df], ignore_index=True)
        # Simple print just so we can see the progress
        print(f"Scraped {offset*5000} rows out of {total}")
    # save to file
    main_df.to_csv(f"datasets/eia_data2.csv", index=False)
    print(f"Saved to datasets/eia_data2.csv")