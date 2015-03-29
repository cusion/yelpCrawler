@echo off
echo "start crawler"
echo "restaurant"
scrapy crawl restaurantSpider --logfile=restaurant.log > restaurant.proc
echo "copy restaurant"
copy test_result.json restaurant.json

timeout /t 1800
echo "bank"
scrapy crawl bankSpider --logfile=bank.log > bank.proc
echo "copy bank"
copy test_result.json bank.json

timeout /t 1800
echo "gas station"
scrapy crawl gasStationSpider --logfile=gasStation.log > gasStation.proc
echo "copy gas station"
copy test_result.json gasStation.json

timeout /t 1800
echo "grocery"
scrapy crawl grocerySpider --logfile=grocery.log > grocery.proc
echo "copy grocery"
copy test_result.json grocery.json