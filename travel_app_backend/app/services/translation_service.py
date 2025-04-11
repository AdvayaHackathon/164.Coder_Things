# from app import translate_client # If initialized in __init__

def translate_text_via_api(text, target_language):
    """
    Translate text using an external API.
    In a real implementation, this would use Google Cloud Translation API or similar.
    """
    print(f"Service: Translating '{text}' to {target_language}")

    # In a real implementation, we would use a translation client
    # Example with Google Cloud Translation:
    # from google.cloud import translate_v2 as translate
    # translate_client = translate.Client()
    # result = translate_client.translate(text, target_language=target_language)
    # return result['translatedText']

    # Dummy implementation for demo purposes
    translations = {
        'es': {
            'hello': 'hola',
            'goodbye': 'adiós',
            'thank you': 'gracias',
            'good morning': 'buenos días'
        },
        'fr': {
            'hello': 'bonjour',
            'goodbye': 'au revoir',
            'thank you': 'merci',
            'good morning': 'bonjour'
        },
        'de': {
            'hello': 'hallo',
            'goodbye': 'auf wiedersehen',
            'thank you': 'danke',
            'good morning': 'guten morgen'
        }
    }
    
    # Case insensitive lookup for common phrases
    text_lower = text.lower()
    if target_language in translations and text_lower in translations[target_language]:
        return translations[target_language][text_lower]
    
    # For demonstration, just append the target language code for unknown phrases
    return f"[Translated to {target_language}]: {text}"