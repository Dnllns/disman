from http import HTTPStatus

# Base de datos de ejemplo
USERS_DB = {
    1: {
        'uid': 1,
        'name': 'Juan'
    },
    2: {
        'uid': 2,
        'name': 'Ana'
    }
}


# Procesar peticiones


def get_helloworld():
    return '¡Hola, Mundo!', HTTPStatus.OK


def get_users():
    return {'users': list(USERS_DB.values())}, HTTPStatus.OK
