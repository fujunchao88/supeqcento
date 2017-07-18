from supeqcento.bussiness.data.model import db
from supeqcento.bussiness.routes import user_module


def init_supeq(app):
    app.blueprint(user_module)

    @app.listener('before_server_start')
    def init_db(app, loop):
        DB_PARAMS = app.config.DB_PARAMS
        db.init(
            DB_PARAMS['NAME'],
            host=DB_PARAMS['HOST'],
            port=int(DB_PARAMS['PORT']),
            user=DB_PARAMS['USER'],
            password=DB_PARAMS['PASSWORD'])

    @app.listener('before_server_start')
    def init_redis(app, loop):
        pass
