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
        # Quarterly data, States+DC only, 2015-2025 (We can change this later)
        response = requests.get(f"https://api.eia.gov/v2/electricity/electric-power-operational-data/data/?frequency=quarterly&data[0]=ash-content&data[1]=consumption-for-eg&data[2]=consumption-for-eg-btu&data[3]=consumption-uto&data[4]=consumption-uto-btu&data[5]=cost&data[6]=cost-per-btu&data[7]=generation&data[8]=heat-content&data[9]=receipts&data[10]=receipts-btu&data[11]=stocks&data[12]=sulfur-content&data[13]=total-consumption&data[14]=total-consumption-btu&facets[location][]=AK&facets[location][]=AL&facets[location][]=AR&facets[location][]=AZ&facets[location][]=CA&facets[location][]=CO&facets[location][]=CT&facets[location][]=DC&facets[location][]=DE&facets[location][]=FL&facets[location][]=GA&facets[location][]=HI&facets[location][]=IA&facets[location][]=ID&facets[location][]=IL&facets[location][]=IN&facets[location][]=KS&facets[location][]=KY&facets[location][]=LA&facets[location][]=MA&facets[location][]=MD&facets[location][]=ME&facets[location][]=MI&facets[location][]=MN&facets[location][]=MO&facets[location][]=MS&facets[location][]=MT&facets[location][]=NC&facets[location][]=ND&facets[location][]=NE&facets[location][]=NH&facets[location][]=NJ&facets[location][]=NM&facets[location][]=NV&facets[location][]=NY&facets[location][]=OH&facets[location][]=OK&facets[location][]=OR&facets[location][]=PA&facets[location][]=RI&facets[location][]=SC&facets[location][]=SD&facets[location][]=TN&facets[location][]=TX&facets[location][]=UT&facets[location][]=VA&facets[location][]=VT&facets[location][]=WA&facets[location][]=WI&facets[location][]=WV&facets[location][]=WY&start=2015-Q1&sort[0][column]=period&sort[0][direction]=desc&offset={offset*5000}&length=5000&api_key={os.getenv('EIA_KEY')}")
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
        # Saves to files so we don't have to keep scraping 
        main_df.to_csv(f"datasets/eia_data.csv", index=False)