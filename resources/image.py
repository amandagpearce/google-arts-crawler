from flask import request, jsonify  # Import jsonify
from flask_smorest import abort, Blueprint
from flask.views import MethodView
from sqlalchemy import func
import re

from db import db
from schemas import ArtworkImageSchema
from models import ArtworkImageModel
from google_script import get_artwork_image_url

blp = Blueprint(
    "Get Image URL", __name__, description="Operations with Google Images"
)


@blp.route("/get_image_url")
class ImageUrl(MethodView):
    @blp.response(200, ArtworkImageSchema)
    def get_image_url(self, artwork_title, artwork_artist):
        imageUrl = get_artwork_image_url(f"{artwork_title} {artwork_artist}")

        print("imageUrl")
        print(imageUrl)

        if imageUrl:
            artwork_record = ArtworkImageModel(
                artworkTitle=artwork_title,
                imageUrl=imageUrl,
                artist=artwork_artist,
            )
            db.session.add(artwork_record)
            db.session.commit()

            return jsonify({"imageUrl": imageUrl})  # Return JSON with imageUrl
        else:
            return jsonify(
                {"message": "No image found for the given query"}
            )  # Return JSON message

    def get(self):
        """Returns image URL from Google Search"""

        # gets the query params
        # artwork_id = request.args.get("artworkId")
        artwork_title = request.args.get("artworkTitle")
        artwork_artist = request.args.get("artist")

        if artwork_artist and artwork_title:
            # Normalize input by removing symbols and converting to lowercase
            normalized_title = re.sub(r"\W+", "", artwork_title).lower()
            normalized_artist = re.sub(r"\W+", "", artwork_artist).lower()

            # case-insensitive search
            artworkRecord = ArtworkImageModel.query.filter(
                func.lower(ArtworkImageModel.artworkTitle).contains(
                    normalized_title
                ),
                func.lower(ArtworkImageModel.artist).contains(
                    normalized_artist
                ),
            ).first()

            if artworkRecord:
                print("artwork record found")
                artworkUrl = artworkRecord.imageUrl
                print(artworkUrl)
                return jsonify({"imageUrl": artworkUrl})
            else:
                artworkUrl = self.get_image_url(artwork_title, artwork_artist)

                print("artworkUrl")
                print(artworkUrl)

                return artworkUrl
        else:
            abort(400, message="Missing artworkId or artworkTitle parameter.")
