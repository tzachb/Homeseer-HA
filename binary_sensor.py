from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorDeviceClass
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

SENSOR_MAP={
    'moisture': BinarySensorDeviceClass.MOISTURE,
    'water': BinarySensorDeviceClass.MOISTURE,
    'motion': BinarySensorDeviceClass.MOTION,
    'alarm': BinarySensorDeviceClass.MOTION,
    'contact': BinarySensorDeviceClass.DOOR,
    'door': BinarySensorDeviceClass.DOOR,
}

def _class(dt):
    for k,v in SENSOR_MAP.items():
        if k in dt: return v
    return None

def _is_sensor(dev):
    itf=dev.get('interface_name','').lower()
    dt=dev.get('device_type_string','').lower()
    return (itf in ('plcbus','z-wave','zwave') and _class(dt) is not None)

async def async_setup_entry(hass, entry, async_add_entities):
    coord=hass.data[DOMAIN][entry.entry_id]['coordinator']
    ents=[HSBinarySensor(coord,d) for d in coord.data if _is_sensor(d)]
    async_add_entities(ents)

class HSBinarySensor(CoordinatorEntity, BinarySensorEntity):
    _attr_has_entity_name=True
    _attr_entity_registry_enabled_default=True
    def __init__(self, coord, dev):
        super().__init__(coord); self._dev=dev
        self._attr_unique_id=f'hs_bin_{dev["ref"]}'
        self._attr_name=f"{dev['name']} ({dev['ref']})"
        self._attr_device_class=_class(dev.get('device_type_string','').lower())
    @property
    def is_on(self):
        return self._dev.get('value',0) not in (0,-1)
    def _handle_coordinator_update(self):
        for d in self.coordinator.data:
            if d['ref']==self._dev['ref']:
                self._dev=d; break
        self.async_write_ha_state()
