# Extras Files

If you wanted to create a service (Linux only) do the following:

### 1. Copy files to folder below

```bash
  sudo cp <..>/market_b3.service market_b3.timer /etc/systemd/system/
```
### 2. Enable and start scheduling

```bash
  sudo systemctl enable market_b3.timer && sudo systemctl start market_b3.timer
```

### Other commands if needed
To view the latest logs, use:
```bash
  sudo journalctl -xfu market_b3.service
```
To view the current timer status, use:
```bash
  sudo systemctl status market_b3.timer
```
To view more info about the last run (triggered by timer or manually triggered), use:
```bash
  sudo systemctl status market_b3.service
```
To restart daemon use:
```bash
  sudo systemctl daemon-reload
```