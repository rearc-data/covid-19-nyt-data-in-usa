# Coronavirus (COVID-19) Data in the United States | The New York Times

The source code outlining how this product gathers, transforms, revises and publishes its datasets is available at [https://github.com/rearc-data/covid-19-nyt-data-in-usa](https://github.com/rearc-data/covid-19-nyt-data-in-usa).

## Main Overview
The New York Times is releasing a series of data files with cumulative counts of coronavirus cases in the United States, at the state and county level, over time. This is time series data from state and local governments and health departments in an attempt to provide a complete record of the ongoing outbreak.

Since late January, The Times has tracked cases of coronavirus in real time as they were identified after testing. Because of the widespread shortage of testing, however, the data is necessarily limited in the picture it presents of the outbreak.

The New York Times uses this data to power maps and reporting, tracking the outbreak, and it is now being made available to the public in response to requests from researchers, scientists and government officials who would like access to the data to better understand the outbreak.

The NYT's data begins with the first reported coronavirus case in Washington State on Jan. 21, 2020. Data on cumulative coronavirus cases and deaths can be found in two files for states and counties.

#### Data Sources
The datasets included with this product are provided in CSV format.  The dataset columns are:

- us.csv: `date, cases, deaths`
- us-states.csv: `date, state, fips, cases, deaths`
- us-counties.csv: `date, county, state, fips, cases, deaths`
- live_us.csv: `date,cases,deaths,confirmed_cases,confirmed_deaths,probable_cases,probable_deaths`
- live_us-states.csv: `date,state,fips,cases,deaths,confirmed_cases,confirmed_deaths,probable_cases,probable_deaths`
- live_us-counties.csv: `date,county,state,fips,cases,deaths,confirmed_cases,confirmed_deaths,probable_cases,probable_deaths`

The files with a `live_` prefix only feature data for the current day, and can contain inconsistencies/errors that the NY Times addresses with updated throughout a day. For historical data direct yourself to the non-live version of the files.

## More Information
- Source: [The New York Times](https://github.com/nytimes/covid-19-data)      
- [The New York Times Tracking Page](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html)    
- [Dataset License](https://raw.githubusercontent.com/nytimes/covid-19-data/master/LICENSE)  
- Frequency: Daily
- Format: CSV

## Contact Details
- If you find any issues with or have enhancement ideas for this product, open up a GitHub [issue](https://github.com/rearc-data/covid-19-nyt-data-in-usa/issues) and we will gladly take a look at it. Better yet, submit a pull request. Any contributions you make are greatly appreciated :heart:.
- If you are looking for specific open datasets currently not available on ADX, please submit a request on our project board [here](https://github.com/rearc-data/covid-datasets-aws-data-exchange/projects/1).
- If you have questions about the source data, please contact covid-data@nytimes.com.
- If you have any other questions or feedback, send us an email at data@rearc.io.

## About Rearc
Rearc is a cloud, software and services company. We believe that empowering engineers drives innovation. Cloud-native architectures, modern software and data practices, and the ability to safely experiment can enable engineers to realize their full potential. We have partnered with several enterprises and startups to help them achieve agility. Our approach is simple — empower engineers with the best tools possible to make an impact within their industry.