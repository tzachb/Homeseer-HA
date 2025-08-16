
HomeSeer-HA Integration (Custom HACS Repo)

This is a modern HomeSeer integration for Home Assistant (supports HS3/HS4 JSON API).
Since it’s not yet in the official HACS default store, you can install it as a custom repository in HACS.

🔧 Installation

Open Home Assistant → go to HACS → Integrations.

Click the three-dot menu (top-right) → Custom repositories.

In the URL field, paste:

https://github.com/tzachb/Homeseer-HA


Choose Integration as the category.

Click Add.

Now search for HomeSeer-HA in HACS and install it.

Restart Home Assistant.

Go to Settings → Devices & Services → Add Integration and search for HomeSeer-HA to configure it.

✨ Features

Full support for HS3/HS4 devices via JSON API

Automatic device and entity discovery

Preserves entity IDs for existing automations

Supports switches, dimmers, sensors, binary sensors, and more
