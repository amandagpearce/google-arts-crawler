from google_images_search import GoogleImagesSearch


def get_artwork_image_url(query):
    # params are
    # Googles programmable search engine API key
    # Search Engine ID from google's programmable search engine controlpanel
    gis = GoogleImagesSearch(
    )

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
    result = gis.results()[0]  # Get the first image result

    return result.url if result else None
