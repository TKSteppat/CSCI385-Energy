 # save smaller csvs to meet github's file size limit
import pandas as pd

if __name__ == "__main__":
    main_df = pd.read_csv("datasets/eia_data.csv")
    num_csvs = main_df.shape[0]//150000
    for i in range(num_csvs+1):
        lower_bound = i*150000
        upper_bound = (i+1)*150000
        if upper_bound > main_df.shape[0]:
            upper_bound = main_df.shape[0]
        df = main_df.iloc[lower_bound:upper_bound]
        df.to_csv(f"datasets/eia_data_{i+1}.csv", index=False)