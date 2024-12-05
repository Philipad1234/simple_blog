from flask import Flask, render_template
from post import Post
import requests

blogs_url = " https://api.npoint.io/c790b4d5cab58020d391"
blog_posts = requests.get(blogs_url).json()
post_objects = []
for post in blog_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    selected_post = None
    for blog_post in post_objects:
        if blog_id == blog_post.id:
            selected_post = blog_post
    return render_template("post.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
