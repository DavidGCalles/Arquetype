from flask import Blueprint, jsonify, request

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
