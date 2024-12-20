from pydantic import BaseModel, Field


class DbConfig(BaseModel):
    user: str = Field(description="User for the DB")
    password: str = Field(description="Password to connect to DB")
    host: str = Field(default="127.0.0.1", description="Host of the DB")
    port: str = Field(default="3306")
    name: str = Field(default="app_dev")
