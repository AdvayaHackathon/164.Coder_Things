def get_local_transport_info(location):
    """
    Get local transport options using Transit APIs.
    In a real implementation, this would use transit APIs or similar.
    """
    print(f"Service: Fetching transport options for location: {location}")

    # In a real implementation, we would call an external transit API
    # Example:
    # import requests
    # transit_api_url = "https://api.exampletransit.com/v1/stops"
    # params = {'lat': location['lat'], 'lon': location['lon'], 'radius': 500}
    # response = requests.get(transit_api_url, params=params)
    # return process_transit_data(response.json())

    # Dummy implementation for demonstration purposes
    import random
    
    # Bus options with different frequencies
    bus_lines = [
        {"type": "Bus", "line": "101", "destination": "Downtown", "eta_minutes": random.randint(2, 15)},
        {"type": "Bus", "line": "202", "destination": "Airport", "eta_minutes": random.randint(5, 20)},
        {"type": "Bus", "line": "303", "destination": "Shopping Mall", "eta_minutes": random.randint(3, 18)}
    ]
    
    # Metro/Subway options
    metro_lines = [
        {"type": "Metro", "line": "Blue", "destination": "City Center", "eta_minutes": random.randint(3, 12)},
        {"type": "Metro", "line": "Red", "destination": "University", "eta_minutes": random.randint(5, 15)}
    ]
    
    # Ride sharing options
    rideshare = [
        {"type": "Ride Share", "provider": "ExampleRide", "eta_minutes": random.randint(3, 8), "estimated_cost": f"${random.randint(8, 15)}-${random.randint(16, 25)}"}
    ]
    
    # Format ETAs as human-readable times
    transport_options = []
    
    for option in bus_lines + metro_lines:
        eta = option.pop("eta_minutes")
        option["next_arrival"] = f"{eta} mins" if eta != 1 else "1 min"
        transport_options.append(option)
    
    for option in rideshare:
        eta = option.pop("eta_minutes")
        option["eta"] = f"{eta} mins" if eta != 1 else "1 min"
        transport_options.append(option)
    
    return transport_options