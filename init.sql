-- init.sql
CREATE TABLE IF NOT EXISTS artwork_images (
    id SERIAL PRIMARY KEY,
    artworkId INT NOT NULL,
    imageUrl TEXT NOT NULL
);
