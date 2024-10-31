# main.py

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from models import db, Project, Package
import requests

# Inicializa o app Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados com o app
db.init_app(app)
api = Api(app)

# Função para verificar pacotes no PyPI
def check_pypi_package(package_name, version=None):
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            versions = data.get('releases', {})
            latest_version = max(versions.keys()) if versions else None
            if version and version not in versions:
                return {"error": "Version not found"}
            return {"name": package_name, "version": version or latest_version}
        return {"error": "Package not found"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500

# Endpoint para criação, listagem e deleção de projetos
class ProjectResource(Resource):
    def post(self):
        data = request.get_json()
        name = data.get("name")
        packages = data.get("packages", [])

        if Project.query.filter_by(name=name).first():
            return {"error": "Project already exists"}, 400

        new_project = Project(name=name)
        db.session.add(new_project)

        for pkg in packages:
            package_info = check_pypi_package(pkg.get("name"), pkg.get("version"))
            if package_info.get('error'):
                return {'error': package_info['error']}, 400

            new_package = Package(name=package_info["name"], version=package_info["version"], project=new_project)
            db.session.add(new_package)

        db.session.commit()
        return {"message": "Project created successfully"}, 201

    def get(self, project_name):
        project = Project.query.filter_by(name=project_name).first()
        if not project:
            return {"error": "Project not found"}, 404

        project_data = {
            "name": project.name,
            "packages": [{"name": pkg.name, "version": pkg.version} for pkg in project.packages]
        }
        return project_data, 200

    def delete(self, project_name):
        project = Project.query.filter_by(name=project_name).first()
        if not project:
            return {"error": "Project not found"}, 404

        db.session.delete(project)
        db.session.commit()
        return {"message": "Project deleted"}, 200

# Adiciona os recursos à API
api.add_resource(ProjectResource, "/projects", "/projects/<string:project_name>")

@app.route("/")
def index():
    return "Hello World!"


# Inicializa a aplicação
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
