from profile.profile import profile

import view
from app import app, db
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix="/blog")
app.register_blueprint(profile, url_prefix="/profile")

if __name__ == "__main__":
    app.run()
