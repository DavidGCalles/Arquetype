from flask import Blueprint, jsonify

crud_bp = Blueprint('crud', __name__)

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
    return jsonify({"data": "ok"})
