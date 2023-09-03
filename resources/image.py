from flask import request
from flask_smorest import abort, Blueprint
from flask.views import MethodView


from db import db
from schemas import ArtworkImageSchema
from models import ArtworkImageModel
from crawler import get_artwork_imageUrl

blp = Blueprint(
    "Get Image URL", __name__, description="Operations with Google Images"
)


@blp.route("/get_imageUrl")
class ImageUrl(MethodView):
    @blp.response(200, ArtworkImageSchema)
    def get(self):
        """Returns image url from Google Search"""

        # gets the query params
        artwork_id = request.args.get("artworkId")
        artwork_title = request.args.get("artworkTitle")

        print("artwork_id")
        print(artwork_id)

        print("artwork_title")
        print(artwork_title)

        if artwork_id and artwork_title:
            artworkRecord = ArtworkImageModel.query.get(artwork_id)

            if artworkRecord:
                artworkUrl = artworkRecord.imageUrl
            else:
                artworkUrl = self.get_imageUrl(artwork_id, artwork_title)

            return artworkUrl
        else:
            abort(400, message="Missing artworkId or artworkTitle parameter.")

    def get_imageUrl(self, artwork_id, artwork_title):
        imageUrl = get_artwork_imageUrl(artwork_title)

        print("#")
        print(artwork_id, artwork_title)
        print("#")

        if imageUrl:
            artwork_image = ArtworkImageModel(
                artwork_id=artwork_id, imageUrl=imageUrl
            )
            db.session.add(artwork_image)
            db.session.commit()
            return artwork_image
        else:
            return None
