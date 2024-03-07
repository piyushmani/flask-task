from flask import Blueprint, request, jsonify
from database.models import Tenant, ProjectMetadata
from database.db import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/check', methods=['GET'])
def check():
    return {'msg': "hello"}, 201

@api_bp.route('/tenant', methods=['POST'])
def create_tenant():
    body = request.get_json()
    movie = Tenant(**body).save()
    id = movie.id
    return {'id': str(id)}, 201

@api_bp.route('/project_metadata', methods=['POST'])
def create_project_metadata():
    body = request.get_json()
    ProjectMetadata(**body).save()
    return jsonify({'message': 'Project metadata created successfully'}), 201

