# Midnight NIGHT Consolidation Tool

**Easy-to-use web tool for consolidating NIGHT tokens from multiple Cardano addresses.**

No technical skills required! Works with Lace, Eternl, and Nami wallets.

---

## Quick Start

### Windows
Double-click: **START_TOOL.bat**

### Mac/Linux
Double-click: **START_TOOL.sh**

Your browser will open automatically. Keep the terminal window open while using the tool!

---

## What This Tool Does

Consolidates NIGHT token allocations from multiple Cardano addresses (used in Midnight's Scavenger Mine) into a single recipient address.

**Benefits:**
- Simplifies final redemption
- Reduces transaction costs
- All NIGHT in one place

---

## Requirements

- **Python 3** (pre-installed on Mac/Linux, download for Windows from [python.org](https://python.org))
- **Cardano Wallet** - Lace, Eternl, or Nami
- **Registered Addresses** at [sm.midnight.gd](https://sm.midnight.gd)

---

## Step-by-Step Instructions

1. **Start the tool** - Double-click `START_TOOL.bat` (Windows) or `START_TOOL.sh` (Mac/Linux)

2. **Enter RECIPIENT address**
   - This is where ALL your NIGHT will go
   - Must be registered and have zero transactions

3. **Copy the message**
   - Click the "Copy Message" button
   - The tool auto-generates the exact message you need

4. **Sign in your wallet**
   - **Lace:** Account → Sign message → Paste → Select payment address → Sign
   - **Eternl:** Settings → Tools → Sign message → Paste → Select payment address → Sign
   - **Nami:** Developer menu → Sign Data → Paste → Sign with payment address

5. **Enter DONOR address**
   - This is the address you just signed with
   - The address you're consolidating FROM

6. **Paste SIGNATURE**
   - Copy the signature from your wallet
   - Paste it into the signature field

7. **Click "Consolidate This Address"**

8. **Repeat for each donor address** you want to consolidate

---

## Important Notes

- **Sign with the DONOR address** (payment address, NOT staking address)
- **Consolidation cannot be undone**
- **Keep terminal window open** while using the tool
- **All NIGHT transfers** - Both past AND future NIGHT from donor goes to recipient
- **Transfer happens after Scavenger Mine closes** (UI may still show NIGHT on donor during mine)

---

## How It Works

The tool runs a local web server that proxies requests to the Midnight API (bypasses browser CORS restrictions). Everything runs on your computer - no data is collected or stored.

```
Your Browser → Local Server → Midnight API
```

---

## Troubleshooting

**Python not installed?**
- Windows: Download from [python.org](https://python.org)
- Mac/Linux: Usually pre-installed

**Browser doesn't open?**
- Copy the URL from terminal (usually `http://localhost:8000`)

**"Address already in use"?**
- Tool automatically finds another port (8000-8100)

**API Errors:**
- `Already consolidated` - This address is already done
- `Invalid signature` - Re-sign the exact message with the donor address
- `Not registered` - Register at [sm.midnight.gd](https://sm.midnight.gd)
- `Invalid address` - Check format (must be `addr1...`, 103 characters)

---

## Files

- `START_TOOL.bat` - Windows launcher
- `START_TOOL.sh` - Mac/Linux launcher
- `START_TOOL.py` - Local server with API proxy
- `index.html` - Web interface

---

## Security

- Runs locally on your computer
- No data collection or transmission (except to official Midnight API)
- Message signing only - not transferring funds
- Open source - review the code
- Uses official API: `scavenger.prod.gd.midnighttge.io`

---

## Tips

- Use "Copy Message" button to avoid typos
- Sign with **payment address**, NOT staking address
- Keep the terminal window open while using the tool
- Consolidate early (deadline: 24hrs after Scavenger Mine ends)

---

## License

MIT License

---

Made for the Midnight community
