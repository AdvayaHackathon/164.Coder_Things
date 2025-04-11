from app import db  # Import the initialized DummyDB client

def get_hidden_gems_from_db(location, user_prefs):
    """
    Fetch hidden gems based on location and preferences.
    Uses our DummyDB instead of Firestore.
    """
    print(f"Service: Fetching hidden gems for {location} with prefs: {user_prefs}")

    try:
        # Get hidden gems from our dummy database
        # In a real implementation, we would query based on location and user preferences
        gems_collection = db.collection('hidden_gems')
        gems_docs = gems_collection.stream()
        
        # Convert to list of dictionaries
        gems_list = []
        for doc in gems_docs:
            if hasattr(doc, 'to_dict'):
                # This would be for a real Firestore document
                gem = doc.to_dict()
                gem['id'] = doc.id
                gems_list.append(gem)
            else:
                # For our dummy implementation
                gems_list.append(doc.data)
                
        print(f"Found {len(gems_list)} hidden gems")
        return gems_list
    except Exception as e:
        print(f"Error fetching gems: {e}")
        # Fallback to static data if there's an error
        return [
            {"name": "Secret Waterfall", "lat": 12.9716, "lon": 77.5946, "description": "A beautiful hidden waterfall surrounded by lush greenery.", "source": "static"},
            {"name": "Local Artisan Market", "lat": 12.9720, "lon": 77.5950, "description": "Great local crafts and authentic cultural items sold by locals.", "source": "static"},
        ]