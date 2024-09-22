"""This blueprint holds every endpoint related to basic crud operations, used for demo purposes"""
from flask import Blueprint, jsonify
from app.dao.generic_dao import BaseDAO

crud_bp = Blueprint('crud', __name__)

crud_dao = BaseDAO()

@crud_bp.route('/crud', methods=['GET'])
def generic_crud():
    """
    Get All items
    ---
    responses:
      200:
        description: Data is retrieved
        schema:
          type: object
          properties:
            data:
              type: object
      400:
        description: No data retrieved.
    """
    data = crud_dao.generic_get_all()
    return jsonify({"data": data})
