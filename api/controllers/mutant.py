from flask import request, jsonify
from sqlalchemy import func

from api.models import db
from api.models.dna import Dna

"""
Numero minimo de secuencias para ser mutante
"""
SEQUENCE_MUTANT = 2


class MutantController:

    @staticmethod
    def mutant():
        data = request.get_json()
        id_dna = ''.join(data['dna'])
        if Dna.query.filter(Dna.id_dna == id_dna).first() is not None:
            return jsonify({'message': 'DNA already exist'}), 409

        dna_array = list_to_matrix(data['dna'])
        mutant = is_mutant(dna_array)
        new_dna = Dna(id_dna=id_dna, dna=data['dna'], mutant=mutant)
        db.session.add(new_dna)
        db.session.commit()

        if mutant is False:
            return jsonify({'message': 'A human has been added'}), 403
        else:
            return jsonify({'message': 'A mutant has been added'}), 200

    @staticmethod
    def stats():
        mutant_count = db.session.query(func.count(Dna.id_dna)).filter(Dna.mutant.is_(True)).scalar()
        human_count = db.session.query(func.count(Dna.id_dna)).filter(Dna.mutant.is_(False)).scalar()
        if human_count != 0:
            ratio = mutant_count/human_count
        else:
            ratio = f"{mutant_count}:{human_count} the ratio is undefined."
        return jsonify({'count_mutant_dna': mutant_count, 'count_human_dna': human_count, 'ratio': ratio})


def list_to_matrix(array):
    """
    Convierte una lista de str en una matriz
    :param array:
    :return:
    """
    return list(map(lambda x: list(x), array))


def is_mutant(array):
    """
    Recorre el arreglo buscando secuencias mutantes, como a la final tiene que validar de alguna forma
    todos los elementos de la matriz, se intenta evitar validaciones innecesarias, y la busqueda termina
    cuando se hayan encontrado dos cadenas mutantes.
    Como se hace un recorrido por matriz, hay validaciones que se van evitando, como verificar posiciones
    anteriores, ya que se entiende que esas ya se hicieron con anticipación.
    :param array:
    :return:
    """
    sequence = 0
    i = 0
    while i < len(array):
        j = 0
        while j < len(array[i]):
            if vertical_check(array, i, j):
                sequence += 1
            if horizontal_check(array, i, j):
                sequence += 1
            if oblique_check(array, i, j):
                sequence += 1
            if sequence >= SEQUENCE_MUTANT:
                return True
            j += 1
        i += 1
    return False


def vertical_check(array, row, column):
    """
    Verifica desde una casilla de forma vertical si existe una secuencia mutante,
    antes de validar si existe mutante, valida el alcance de casillas para no hacer validaciones innecesarias
    :param array:
    :param row: fila actual
    :param column: columna actual
    :return:
    """
    if len(array) - 1 < row + 3:
        return False
    i = row + 1
    while i <= row + 3:
        if array[row][column] != array[i][column]:
            return False
        i += 1
    return True


def horizontal_check(array, row, column):
    """
    Verifica desde una casilla de forma horizontal si existe una secuencia mutante,
    antes de validar si existe mutante, valida el alcance de casillas para no hacer validaciones innecesarias
    :param array:
    :param row: fila actual
    :param column: columna actual
    :return:
    """
    if len(array[row]) - 1 < column + 3:
        return False
    i = column + 1
    while i <= column + 3:
        if array[row][column] != array[row][i]:
            return False
        i += 1
    return True


def oblique_check(array, row, column):
    """
    Verifica desde una casilla de forma oblicua si existe una secuencia mutante,
    antes de validar si existe mutante, valida el alcance de casillas para no hacer validaciones innecesarias
    :param array:
    :param row: fila actual
    :param column: columna actual
    :return:
    """
    if len(array) - 1 < row + 3 or len(array[row]) - 1 < column + 3:
        return False
    i = row + 1
    j = column + 1
    while i <= row + 3 and j <= column + 3:
        if array[row][column] != array[i][j]:
            return False
        i += 1
        j += 1
    return True
