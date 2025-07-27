"""Config flow"""
from homeassistant import config_entries
import voluptuous as vol
from homeassistant.const import CONF_HOST, CONF_PORT
from .const import DOMAIN, DEFAULT_PORT
class HomeSeerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION=1
    async def async_step_user(self, user_input=None):
        if user_input:
            return self.async_create_entry(title=f'HomeSeer ({user_input[CONF_HOST]})', data=user_input)
        return self.async_show_form(step_id='user', data_schema=vol.Schema({vol.Required(CONF_HOST):str,vol.Optional(CONF_PORT,default=DEFAULT_PORT):int}))
