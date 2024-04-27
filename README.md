# Indian Railway Express Trains Delay Datasets 
I have created  this dataset to provide comprehensive information about train routes, delays, and cancellations for express trains connecting Guwahati (Assam) to major metro cities in India, namely Delhi, Mumbai, Chennai, and Kolkata.



## Overview

This dataset contains information about train delays for express trains running between Guwahati and various cities in India. It includes details such as train number, train name, origin station, destination station, train type, and delay statistics at each station along the route.
The dataset consists of two parts: a CSV file named "Train List" containing information about express trains connecting Guwahati to metro cities, and a folder "Train_Route" containing CSV files with train route details and delay information

## Dataset Details

- **File Name**: Train_List.csv
- **Description**: Contains metadata for each train, including train number, train name, origin station, destination station, and train type.
- **File Format**: CSV (Comma-Separated Values)

- **File Name Format**: `<Train_Number>.csv` (e.g., `13181.csv`, `20503.csv`)
- **Description**: Contains delay statistics for each station along the route of the corresponding train.
- **File Format**: CSV (Comma-Separated Values)
- **Columns**:
  - `Station`: Name of the station
  - `Station_Name`: Full name of the station
  - `Average_Delay(min)`: Average delay in minutes
  - `Right Time (0-15 min's)`: Percentage of times the train arrived on time or with a delay of up to 15 minutes
  - `Slight Delay (15-60 min's)`: Percentage of times the train arrived with a slight delay (15-60 minutes)
  - `Significant Delay (>1 Hour)`: Percentage of times the train arrived with a significant delay (more than 1 hour)
  - `Cancelled/Unknown`: Percentage of times the train was cancelled or the arrival time was unknown


## Interactive Visualization (provided with code in jupyter notebook "Scraping&Visualization.ipynb")
```
Move the Scraping&Visualization.ipynb notebook in the Dataset folder and run the cells to reproduce the plots.
```

![image](https://github.com/ankitaanand28/DA323_IndianRailwayTrainDelayDatasets/assets/95133586/fdcc6acc-56b5-4670-8625-afc3501136a6)



![image](https://github.com/ankitaanand28/DA323_IndianRailwayTrainDelayDatasets/assets/95133586/0a3b90ef-8cfe-41db-855b-ee5fff13efdc)

![newplot](https://github.com/ankitaanand28/DA323_IndianRailwayTrainDelayDatasets/assets/95133586/df1c2fe5-e06d-431d-b9ef-e8fe4002703b)

## Usage

This dataset can be used for various purposes, including:

- Analyzing trends in train delays between Guwahati and different cities
- Identifying stations with frequent delays and potential causes
- Predictive modeling for estimating train arrival times based on historical data

## Citation

If you use this dataset in your research or analysis, please consider citing it as follows:
```
@dataset{indian-railways-train-delay-dataset,
author = {Ankita Anand},
year = {2024},
title = {Indian Railways Train Delay Dataset},
version = {1.0},
url = {https://github.com/ankitaanand28/DA323_IndianRailwayTrainDelayDatasets}
}
```

## License

This dataset is provided under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).




