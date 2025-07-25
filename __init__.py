"""HomeSeer integration"""
from __future__ import annotations
import logging
from typing import Any
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .const import DOMAIN, DEFAULT_PORT, UPDATE_INTERVAL
from .api import HomeSeerAPI

_LOGGER = logging.getLogger(__name__)
PLATFORMS=['switch','light','binary_sensor']

async def async_setup_entry(hass:HomeAssistant, entry:ConfigEntry)->bool:
    session = async_get_clientsession(hass)
    api = HomeSeerAPI(host=entry.data.get('host'),port=entry.data.get('port',DEFAULT_PORT),session=session)
    async def _async_update():
        return await api.async_get_devices()
    coordinator=DataUpdateCoordinator(hass,_LOGGER,name='homeseer',update_method=_async_update,update_interval=UPDATE_INTERVAL)
    try:
        await coordinator.async_config_entry_first_refresh()
    except Exception as err:
        raise ConfigEntryNotReady from err
    hass.data.setdefault(DOMAIN,{})[entry.entry_id]={'api':api,'coordinator':coordinator}
    await hass.config_entries.async_forward_entry_setups(entry,PLATFORMS)
    return True

async def async_unload_entry(hass:HomeAssistant, entry:ConfigEntry):
    await hass.config_entries.async_unload_platforms(entry,PLATFORMS)
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
