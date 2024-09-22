from flask import Blueprint, jsonify, request
from app.services.db import get_db_connection

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

@main_bp.route('/test_db', methods=["GET"])
def test_db():
    conn = get_db_connection()
    print(conn)
    return jsonify({"message": "ok"})