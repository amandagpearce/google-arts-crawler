import os
from dotenv import load_dotenv
from google_images_search import GoogleImagesSearch


def get_artwork_image_url(query):
    load_dotenv()
    # Googles programmable search engine API key
    search_engine_key = os.getenv("PROGRAMMABLE_SEARCH_ENGINE_API_KEY")
    # Search Engine ID from google's programmable search engine controlpanel
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")

    gis = GoogleImagesSearch(search_engine_key, search_engine_id)

    search_params = {
        "q": query,
        "num": 1,  # Number of images to fetch
        "safe": "high",  # Safety level (options: high, medium, off)
        "fileType": "jpg|png",  # Limit search to JPEG and PNG files
        "size": "large",  # Filter for large images
        "rights": (  # Creative Commons licenses
            "cc_publicdomain|"
            "cc_attribute|"
            "cc_sharealike|"
            "cc_noncommercial|"
            "cc_nonderived"
        ),
    }

    gis.search(search_params=search_params)
    first_result = gis.results()[0]

    print("result.url", first_result.url)

    return first_result.url if first_result else None
