from models.db import db
from models.post import Post
from flask_restful import Resource
from flask import request


class Posts(Resource):
    def get(self):
        posts = Post.find_all()
        results = [p.json() for p in posts]
        return results

    def post(self):
        data = request.get_json()
        params = {}
        for k in data.keys():
            params[k] = data[k]
        post = Post(**params)
        post.create()
        return post.json(), 201


class PostSingular(Resource):
    def get(self, post_id):
        post = Post.find_by_id(post_id)
        if not post:
            return {"msg": "Post not found"}, 404
        return post.json()

    def delete(self, post_id):
        post = Post.find_by_id(post_id)
        if not post:
            return {"msg": "Post not found"}, 404
        db.session.delete(post)
        db.session.commit()
        return {"msg": "Post Deleted", "payload": post.json()}

    def put(self, post_id):
        data = request.get_json()
        post = Post.find_by_id(post_id)
        if not post:
            return {"msg": "Post not found"}, 404
        for key in data:
            setattr(post, key, data[key])
        db.session.commit()
        return post.json(), 201
