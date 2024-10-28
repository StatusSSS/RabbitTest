from pydantic_settings import BaseSettings, SettingConfigDict


class Setting(BaseSettings):
    DATA_BASE_URL: str

    model_config = SettingConfigDict(
        env_file =".env",
        extra="ignore"
    )