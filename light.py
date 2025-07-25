from homeassistant.components.light import LightEntity, ColorMode, ATTR_BRIGHTNESS
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

def _is_light(dev):
    return dev.get('interface_name','').lower()=='plcbus' and 'lamp' in dev.get('device_type_string','').lower()

async def async_setup_entry(hass, entry, async_add_entities):
    data=hass.data[DOMAIN][entry.entry_id]
    coord=data['coordinator']; api=data['api']
    ents=[HSLight(coord, api, d) for d in coord.data if _is_light(d)]
    async_add_entities(ents)

class HSLight(CoordinatorEntity, LightEntity):
    _attr_supported_color_modes={ColorMode.BRIGHTNESS}
    _attr_entity_registry_enabled_default=True
    def __init__(self,coord,api,dev):
        super().__init__(coord)
        self.api=api; self._dev=dev
        self._attr_unique_id=f'hs_light_{dev["ref"]}'
        self._attr_name=f"{dev['name']} ({dev['ref']})"
    @property
    def is_on(self):
        return self._dev.get('value',0)>0
    @property
    def brightness(self):
        return int(round(self._dev.get('value',0)/100*255)) if self.is_on else None
    async def async_turn_on(self, **k):
        v=int(round(k.get(ATTR_BRIGHTNESS,255)/255*100)) if k.get(ATTR_BRIGHTNESS) is not None else 101
        await self.api.async_set_device_value(self._dev['ref'],v)
        await self.coordinator.async_request_refresh()
    async def async_turn_off(self, **k):
        await self.api.async_set_device_value(self._dev['ref'],0)
        await self.coordinator.async_request_refresh()
    def _handle_coordinator_update(self):
        for d in self.coordinator.data:
            if d['ref']==self._dev['ref']:
                self._dev=d; break
        self.async_write_ha_state()
