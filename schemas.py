from marshmallow import Schema, fields


class ArtworkImageSchema(Schema):
    id = fields.Int(dump_only=True)
    artworkId = fields.Int(required=True)
    imageUrl = fields.Str(required=True)


# # Schema for serialization/deserialization
# artwork_image_schema = ArtworkImageSchema()
# artwork_images_schema = ArtworkImageSchema(many=True)
