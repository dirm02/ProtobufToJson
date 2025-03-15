import requests
import json
from google.protobuf.json_format import MessageToJson
from google.transit import gtfs_realtime_pb2

def fetch_and_convert():
    # API endpoint and key
    url = "https://api.stm.info/pub/od/gtfs-rt/ic/v2/vehiclePositions"
    headers = {
        "accept": "application/x-protobuf",
        "apiKey": "l7e72eee36d2534b11b517cb23cb103394"
    }
    
    try:
        # Make the request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the protobuf response
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(response.content)
        
        # Convert to JSON
        json_data = MessageToJson(feed)
        
        # Save to file
        with open('vehicle_positions.json', 'w') as f:
            f.write(json_data)
            
        print("Successfully converted protobuf to JSON. Data saved to 'vehicle_positions.json'")
        
        # Print first entity as sample
        if feed.entity:
            print("\nSample data (first entity):")
            sample_json = MessageToJson(feed.entity[0])
            print(json.dumps(json.loads(sample_json), indent=2))
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    fetch_and_convert() 