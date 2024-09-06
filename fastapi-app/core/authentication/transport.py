from fastapi_users.authentication import BearerTransport

bearer_transport = BearerTransport(
    # TODO Обновить URL для получения токена
    tokenUrl="auth/jwt/login"
)
