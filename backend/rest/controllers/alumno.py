from http import HTTPStatus


# Base de datos de ejemplo
COURSES_DB = {
    1: {
        'courseid': 1,
        'name': 'Programación'
    },
    2: {
        'courseid': 2,
        'name': 'Matemáticas'
    }
}


def get_about():
    return 'Daniel Alonso Báscones', HTTPStatus.OK


def get_courses():
    return {'courses': list(COURSES_DB.values())}, HTTPStatus.OK
