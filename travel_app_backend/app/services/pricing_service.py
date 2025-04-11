from app import db  # Import the initialized DummyDB client

def get_price_guide_info(category, location):
    """
    Get price estimates from our dummy DB.
    Previously used Firestore, now replaced with dummy implementation.
    """
    print(f"Service: Fetching prices for {category} in {location}")

    # Sample price data - this would normally be pulled from Firestore
    price_data = {
        "museum": {
            "average_cost": "$15.00",
            "range": "$8.00 - $25.00",
            "notes": "Many museums offer free entry on specific days of the month."
        },
        "meal": {
            "average_cost": "$22.50",
            "range": "$10.00 - $50.00",
            "notes": "Street food is cheapest, high-end restaurants most expensive."
        },
        "hotel": {
            "average_cost": "$120.00",
            "range": "$60.00 - $300.00",
            "notes": "Prices vary significantly by season and location."
        },
        "taxi": {
            "average_cost": "$12.00",
            "range": "$8.00 - $25.00",
            "notes": "Ride-sharing apps may offer better rates than traditional taxis."
        },
        "souvenir": {
            "average_cost": "$8.50",
            "range": "$2.00 - $30.00",
            "notes": "Local markets typically offer better prices than tourist shops."
        }
    }
    
    # Return price data for the requested category, or a default message if not found
    if category in price_data:
        result = price_data[category]
        result["category"] = category
        result["source"] = "Dummy Database"  # Changed from "Sample data"
        return result
    else:
        return {
            "category": category,
            "average_cost": "No data available",
            "range": "Unknown",
            "source": "Dummy Database - No data for this category"
        }