# Protobuf to JSON Converter

A Python script to convert STM GTFS-RT protobuf data to JSON format.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the script:
   ```
   python protobuf_to_json.py
   ```

## Output

The script will:
- Fetch vehicle position data from the STM API
- Convert the protobuf data to JSON
- Save the result to `vehicle_positions.json`
- Display a sample of the data in the terminal

## API Information

This script uses the STM's GTFS-RT vehicle position endpoint:
- URL: https://api.stm.info/pub/od/gtfs-rt/ic/v2/vehiclePositions
- Format: Protobuf (GTFS Realtime)
- Authentication: API key in header

## Requirements

- Python 3.6+
- Internet connection to access the STM API 