# djangorest
USECASE: Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
ENDPOINT: http://127.0.0.1:8000/rest/performancemetrix?fields=impressions,clicks,channel,country&date_to=01-06-2017&groupby=channel&groupby=country&ordering=-clicks

USECASE: Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
ENDPOINT: http://127.0.0.1:8000/rest/performancemetrix?fields=installs,date&date_from=01-05-2017&date_to=31-05-2017&os=ios&groupby=date&ordering=date

USECASE: Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
ENDPOINT: http://127.0.0.1:8000/rest/performancemetrix?fields=revenue,os&date=01-06-2017&country=US&groupby=os&ordering=-revenue

USECASE: Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI
ENDPOINT: http://127.0.0.1:8000/rest/performancemetrix?fields=metric_cpi,spend,channel&country=CA&groupby=channel&ordering=-metric_cpi.
