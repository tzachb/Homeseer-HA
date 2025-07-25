"""HomeSeer HS3/HS4 JSON API wrapper"""
import aiohttp, async_timeout
from typing import List, Dict
class HomeSeerAPI:
    def __init__(self, host:str, port:int, session:aiohttp.ClientSession):
        self._base=f'http://{host}:{port}'
        self._session=session
    async def async_get_devices(self)->List[Dict]:
        url=f'{self._base}/JSON?request=getstatus'
        async with async_timeout.timeout(15):
            async with self._session.get(url) as resp:
                resp.raise_for_status()
                data=await resp.json(content_type=None)
                return data.get('Devices',[])
    async def async_set_device_value(self, ref:int, value:int):
        url=f'{self._base}/JSON?request=controldevicebyvalue&ref={ref}&value={value}'
        async with async_timeout.timeout(10):
            async with self._session.get(url) as resp:
                resp.raise_for_status()
