def get_digital_guide_response(topic, personality):
    """
    Generate guide response with personality using templates.
    In a real implementation, this could use a conversational AI service.
    """
    print(f"Service: Generating guide response for {topic} with personality {personality}")

    # In a real implementation, we might:
    # 1. Fetch information about the topic from a knowledge base or API
    # 2. Use a more sophisticated template system or AI to generate responses
    # 3. Potentially integrate with a conversational AI platform

    # Basic information about common tourist topics
    topic_info = {
        "eiffel tower": "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower. Constructed from 1887 to 1889, it was initially criticized by some of France's leading artists and intellectuals for its design, but it has become a global cultural icon of France.",
        "louvre museum": "The Louvre Museum is the world's largest art museum and a historic monument in Paris, France. A central landmark of the city, it is located on the Right Bank of the Seine. Approximately 38,000 objects from prehistory to the 21st century are exhibited over an area of 72,735 square meters.",
        "taj mahal": "The Taj Mahal is an ivory-white marble mausoleum on the right bank of the river Yamuna in the Indian city of Agra. It was commissioned in 1632 by the Mughal emperor Shah Jahan to house the tomb of his favorite wife, Mumtaz Mahal.",
        "great wall of china": "The Great Wall of China is a series of fortifications made of stone, brick, tamped earth, wood, and other materials, built along an east-to-west line across the historical northern borders of China to protect the Chinese states and empires against the raids and invasions of various nomadic groups.",
        "colosseum": "The Colosseum is an oval amphitheatre in the centre of the city of Rome, Italy. It is the largest ancient amphitheatre ever built, and is still the largest standing amphitheatre in the world today, despite its age."
    }
    
    # Look up information about the topic (case-insensitive)
    topic_lower = topic.lower()
    base_info = topic_info.get(topic_lower, f"Information about {topic} would be retrieved from a knowledge base in a production environment.")
    
    # Generate response with the appropriate personality
    if personality == "funny":
        prefix = f"Alright, buckle up! Let's talk about {topic}. They say tourists visit it to take selfies, but the real reason is to make their Instagram followers jealous! Anyway, here's the scoop: "
        suffix = " ...And that's why I always bring an extra pair of socks when visiting. Trust me on this one!"
        response = prefix + base_info + suffix
    elif personality == "friendly":
        prefix = f"Hey there! Curious about {topic}? It's one of my favorite places to tell people about! Here's what makes it special: "
        suffix = " Hope that helps! Let me know if you have any other questions. I'm here to make your trip amazing!"
        response = prefix + base_info + suffix
    else:  # serious (default)
        prefix = f"Regarding {topic}. The historical and cultural significance is as follows. "
        suffix = " This information is based on historical records and academic research."
        response = prefix + base_info + suffix
    
    return response