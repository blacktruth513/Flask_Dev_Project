from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

# 라우트 함수 등록하기 
@bp.route('/hello')
def standing():
    return 'the last man standing!'

@bp.route('/')
def index():
    return 'hello world'
