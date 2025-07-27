# HomeSeer (HS3/HS4) – Home Assistant Integration

> **Local, no‑cloud control of your HomeSeer smart‑home from Home Assistant 2025.6 and later.**  
> Supports PLC‑BUS, Z‑Wave, virtual scene switches, and water / motion / door sensors out‑of‑the‑box.

---

## ✨ Features

| Category | Details |
|----------|---------|
| **Lights & Switches** | • PLC‑BUS dimmers & relays (101 / 0 logic)<br>• Z‑Wave binary switches (255 / 0) including TKB & Fibaro<br>• Virtual scene switches |
| **Binary Sensors** | • Water‑leak / moisture<br>• Motion (PIR) & general‑purpose alarm<br>• Door / contact |
| **Zero Cloud** | Pure local JSON polling – no cloud keys, no latency. |
| **Auto‑Enable** | Every entity (≈ 129 in a typical HS3 install) is enabled on first import. |
| **Port Flexibility** | Default port **80** (HS3 default). Override to 8181 or any custom port in the setup dialog. |
| **Collision‑Proof IDs** | Unique IDs include `_<ref>` to prevent duplicate slugs. |

---

## 📦 Installation (HACS)

1. **HACS ▸ Integrations ▸ ⋮ ▸ Custom Repositories**  
   *Repository URL:*  
   ```
   https://github.com/<your‑user>/homeseer‑ha
   ```  
   *Category:* **Integration** → **Add**
2. Search **“HomeSeer (HS3/HS4)”** → **Download** → **Restart** Home Assistant.
3. **Add Integration**  
   *Host* = `X.X.X.X`   *Port* = `80` (default) → **Submit**.
4. Approximately **129 entities** (lights, switches, sensors) appear instantly.

---

## 🏠 Entity Breakdown (example)

| Platform | Count | Examples |
|----------|-------|----------|
| Light | 17 | `light.kitchen_main_lamp` |
| Switch | 26 | `switch.tkb_plug` |
| Binary Sensor | 86 | `binary_sensor.water_leak_kitchen` |
| **Total** | **129** | |

---

## 🚀 Roadmap

| Version | Planned |
|---------|---------|
| **1.1.0** | Numeric `sensor` platform (temperature, humidity, power, lux). |
| **1.2.0** | `climate` platform for thermostats |
| **1.3.0** | `media_player` root entities (Chromecast / Kodi) |

---

## 🛠 Troubleshooting

```yaml
logger:
  default: info
  logs:
    custom_components.homeseer: debug
```

---

## 📜 License

MIT License – see [LICENSE](LICENSE).
