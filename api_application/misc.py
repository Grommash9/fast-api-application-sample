from fastapi import FastAPI
from api_application import routes
from Secweb.XContentTypeOptions import XContentTypeOptions
from Secweb.StrictTransportSecurity import HSTS


tags_metadata = [
    {
        "name": "Інформація",
        "description": "Отримання загальної інформації",
    }
]

app = FastAPI(
    title="Апі сервіс",
    description='Апі сервіс',
    version="0.0.1",
    contact={
        "name": "alex",
        "url": "https://home.work/",
        "email": "google@gmail.com",

    },
    openapi_tags=tags_metadata,
    docs_url='/docs',
    openapi_url="/openapi.json"
)

app.add_middleware(XContentTypeOptions)
app.add_middleware(HSTS, Option={'max-age': 31536000, 'preload': True})
app.include_router(routes.information.formatted_router)

