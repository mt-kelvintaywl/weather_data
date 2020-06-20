# sign up and obtain an API key at openweathermap.org
OPENWEATHER_API_KEY=[replace me]

# replace stream name to your own
KDF_STREAM_NAME=ktay-moneytree-jp-weather

CITIES='Singapore Sydney Tokyo London California Beijing'

for CITY in $CITIES
do
  JSON=$(curl http://api.openweathermap.org/data/2.5/weather\?q\=$CITY\&appid\=$OPENWEATHER_API_KEY | jq -cR)
  aws firehose put-record --delivery-stream-name $KDF_STREAM_NAME --record "{\"Data\": $JSON}"
done
