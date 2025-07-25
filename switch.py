from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

def _is_switch(dev):
    itf = dev.get('interface_name','').lower()
    dt = dev.get('device_type_string','').lower()
    if itf in ('plcbus') and 'lamp' not in dt:
        return True
    if itf.startswith('z-wave') or itf.startswith('zwave'):
        return 'switch' in dt or 'relay' in dt
    if 'scene' in dt:
        return True
    return False

async def async_setup_entry(hass, entry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    api = data['api']; coord = data['coordinator']
    ents=[HSSwitch(coord, api, d) for d in coord.data if _is_switch(d)]
    async_add_entities(ents)

class HSSwitch(CoordinatorEntity, SwitchEntity):
    _attr_has_entity_name=True
    _attr_entity_registry_enabled_default=True
    def __init__(self, coord, api, dev):
        super().__init__(coord)
        self.api=api; self._dev=dev
        itf = dev.get('interface_name','').lower()
        if itf.startswith('z-wave') or itf.startswith('zwave'):
            self._on_val, self._off_val = 255,0
        elif itf=='plcbus':
            self._on_val, self._off_val = 101,0
        else:
            self._on_val, self._off_val = 100,0
        self._attr_unique_id = f'hs_switch_{dev["ref"]}'
        self._attr_name = f"{dev['name']} ({dev['ref']})"
    @property
    def is_on(self):
        return self._dev.get('value',0) not in (0,-1)
    async def async_turn_on(self, **k):
        await self.api.async_set_device_value(self._dev['ref'], self._on_val)
        await self.coordinator.async_request_refresh()
    async def async_turn_off(self, **k):
        await self.api.async_set_device_value(self._dev['ref'], self._off_val)
        await self.coordinator.async_request_refresh()
    def _handle_coordinator_update(self):
        for d in self.coordinator.data:
            if d['ref']==self._dev['ref']:
                self._dev=d; break
        self.async_write_ha_state()
