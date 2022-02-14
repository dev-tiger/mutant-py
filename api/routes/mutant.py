from flask import Blueprint, jsonify

from api.controllers.mutant import MutantController

mutant_api = Blueprint('mutant_bp', __name__)


@mutant_api.route('/mutant', methods=['POST'])
def mutant():
    return MutantController.mutant()


@mutant_api.route('/stats', methods=['GET'])
def stats():
    return MutantController.stats()
