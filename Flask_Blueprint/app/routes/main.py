from flask import Blueprint, jsonify, request
from app.dao.generic_dao import BaseDAO

main_bp = Blueprint('main', __name__)

@main_bp.route('/ping', methods=['GET'])
def ping():
    """
    Ping endpoint to test the server.
    ---
    responses:
      200:
        description: Server is running
        schema:
          type: object
          properties:
            message:
              type: string
              example: pong
    """
    return jsonify({"message": "pong"})

@main_bp.route('/generic_crud', methods=['GET'])
def root():
    """
    Get All items
    ---
    responses:
      200:
        description: Data is retrived
        schema:
          type: object
          properties:
            data:
              type: object
      400:
        description: No data retrived.
    """
    return jsonify({"data": "ok"})
