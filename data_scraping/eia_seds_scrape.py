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
        response = requests.get(f"https://api.eia.gov/v2/seds/data/?frequency=annual&data[0]=value&facets[seriesId][]=CLTCE&facets[seriesId][]=CLTCV&facets[seriesId][]=FFTCE&facets[seriesId][]=NGTCV&facets[seriesId][]=NNTCE&facets[seriesId][]=NUETV&facets[seriesId][]=PATCV&facets[seriesId][]=PMTCE&facets[stateId][]=AK&facets[stateId][]=AL&facets[stateId][]=AR&facets[stateId][]=AZ&facets[stateId][]=CA&facets[stateId][]=CO&facets[stateId][]=CT&facets[stateId][]=DC&facets[stateId][]=DE&facets[stateId][]=FL&facets[stateId][]=GA&facets[stateId][]=HI&facets[stateId][]=IA&facets[stateId][]=ID&facets[stateId][]=IL&facets[stateId][]=IN&facets[stateId][]=KS&facets[stateId][]=KY&facets[stateId][]=LA&facets[stateId][]=MA&facets[stateId][]=MD&facets[stateId][]=ME&facets[stateId][]=MI&facets[stateId][]=MN&facets[stateId][]=MO&facets[stateId][]=MS&facets[stateId][]=MT&facets[stateId][]=NC&facets[stateId][]=ND&facets[stateId][]=NE&facets[stateId][]=NH&facets[stateId][]=NJ&facets[stateId][]=NM&facets[stateId][]=NV&facets[stateId][]=NY&facets[stateId][]=OH&facets[stateId][]=OK&facets[stateId][]=OR&facets[stateId][]=PA&facets[stateId][]=RI&facets[stateId][]=SC&facets[stateId][]=SD&facets[stateId][]=TN&facets[stateId][]=TX&facets[stateId][]=UT&facets[stateId][]=VA&facets[stateId][]=VT&facets[stateId][]=WA&facets[stateId][]=WI&facets[stateId][]=WV&facets[stateId][]=WY&start=2015&sort[0][column]=period&sort[0][direction]=desc&offset={offset*5000}&length=5000&api_key={os.getenv('EIA_API_KEY')}")
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
    main_df.to_csv(f"datasets/raw/eia_seds_data.csv", index=False)
    print(f"Saved to datasets/raw/eia_seds_data.csv")