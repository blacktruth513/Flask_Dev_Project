from flask import Flask, request, jsonify, current_app
from flask.json import JSONEncoder
from sqlalchemy import create_engine, text 
from flask_migrate import Migrate
import config


# Flask가 자동으로 create_app이름의 함수를 factory 함수로 인식해서 해당 함수를 통해 Flask를 실행시킨다.
#create_engine() : 이 함수를 통해 db_url에 명시된 DB에 접속한다. Engine 객체를 반환하는데, 이 객체를 사용해 연결된 DB에 SQL를 실행할 수 있다.
#database.execute() : Engine 객체의 execute() 메소드로 SQL을 DB에 전송해 실행한다. SQL 구문과 구문에 필요한 인자들의 값(딕셔너리) 2개의 인자를 받는다.
#text() : 이 함수에 전달된 문자열에 ':'이 포함되어 있으면 ':' 다음에 오는 단어와 동일한 키를 사용해 딕셔너리에서 읽어 치환한다. 여기서 "WHERE name = :n#ame"은 "WHERE name = user_name"과 같다.

# db = SQLAlchemy()
# migrate = Migrate()
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)

def create_app(test_config = None):  # 다른 파일에서 import 를 해도 문제가 될 일도 줄어듭니다.
    app = Flask(__name__)
    
    app.json_encoder = CustomJSONEncoder

    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.update(test_config) 

    database = create_engine(app.config['DB_URL'], encoding = 'utf-8', max_overflow = 0)		
    app.database = database		   
    
    #ORM part 

    # blueprint part
    from .views import main_views
    app.register_blueprint(main_views.bp) #main_views.py 파일에서 생성한 블루프린트 객체인 bp를 등록하면 된다.

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    
