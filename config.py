import pydantic
from typing import Literal, Optional
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

#EnvContext = Literal['personal', 'test', 'stage', 'prod']


class Settings(pydantic.BaseSettings):
    # --- Browser Capabilities ---
    browserName: str = 'chrome'
    browserVersion: str = '100.0'
    hold_driver_at_exit: bool = False
    base_url: str = 'https://motivtelecom.ru/'
    window_width: int = 1920
    window_height: int = 1080
    # --- > > Selenium credentials---
    # userName: Optional[str] = pydantic.Field(None, env='browserstack.userName')
    # accessKey: Optional[str] = pydantic.Field(None, env='browserstack.accessKey')

    # --- Remote Driver ---
    remote_url: str = 'https://user1:1234@selenoid.autotests.cloud/wd/hub'

    # --- Selene ---
    timeout: float = 9.0

    @property
    def driver_options(self):
        options = Options()
        if 'selenoid.autotests.cloud' in self.remote_url:
            selenoid_capabilities = {'browserName': self.browserName,
                                     'browserVersion': self.browserVersion,
                                     'selenoid:options': {
                                         'enableVNC': True,
                                         'enableVideo': True}
                                     }
            options.capabilities.update(selenoid_capabilities)

        return options


settings = Settings()
