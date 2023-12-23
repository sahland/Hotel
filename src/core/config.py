from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_ADRESS: str

    api_v1_prefix: str = '/api/v1'

    model_config = SettingsConfigDict(env_file='.env')

    
    @property
    def database_url_asyncpg(self):
        return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_ADRESS}:{self.DATABASE_PORT}/{self.POSTGRES_DB}'
    

settings = Setting()