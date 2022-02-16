from flask import jsonify


class WelcomeController:
    @staticmethod
    def index():
        return jsonify({"message": "Welcome to mutant api"})
