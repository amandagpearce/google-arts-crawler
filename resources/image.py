from flask import request, jsonify  # Import jsonify
from flask_smorest import abort, Blueprint
from flask.views import MethodView

from db import db
from schemas import ArtworkImageSchema
from models import ArtworkImageModel
from crawler import get_artwork_image_url

blp = Blueprint(
    "Get Image URL", __name__, description="Operations with Google Images"
)


@blp.route("/get_image_url")
class ImageUrl(MethodView):
    @blp.response(200, ArtworkImageSchema)
    def get_image_url(self, artwork_id, artwork_title, artwork_artist):
        imageUrl = get_artwork_image_url(f"{artwork_title} {artwork_artist}")

        print("imageUrl")
        print(imageUrl)

        if imageUrl:
            artwork_image = ArtworkImageModel(
                artworkId=artwork_id, imageUrl=imageUrl, artist=artwork_artist
            )
            db.session.add(artwork_image)
            db.session.commit()

            return jsonify({"imageUrl": imageUrl})  # Return JSON with imageUrl
        else:
            return jsonify(
                {"message": "No image found for the given query"}
            )  # Return JSON message

    def get(self):
        """Returns image URL from Google Search"""

        # gets the query params
        artwork_id = request.args.get("artworkId")
        artwork_title = request.args.get("artworkTitle")
        artwork_artist = request.args.get("artist")

        if artwork_id and artwork_title:
            artworkRecord = ArtworkImageModel.query.get(artwork_id)

            if artworkRecord:
                print("artwork record found")
                artworkUrl = artworkRecord.imageUrl
                print(artworkUrl)
                return jsonify(
                    {"imageUrl": artworkUrl}
                )  # Return JSON with imageUrl
            else:
                artworkUrl = self.get_image_url(
                    artwork_id, artwork_title, artwork_artist
                )

                print("artworkUrl")
                print(artworkUrl)

                return artworkUrl  # Return the result directly as JSON
        else:
            abort(400, message="Missing artworkId or artworkTitle parameter.")
