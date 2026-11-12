import urllib.request
import urllib.error
import json

HERMES_BASE = "https://hermes.swap.io"
SOL_MINT = "So11111111111111111111111111111111111111112"
USDC_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"

def discover_x402_endpoints():
    print("=" * 76)
    print(" [1] DISCOVERING SWAP.IO HERMES x402 ENDPOINTS (GET /v1/info)")
    print("=" * 76)
    req = urllib.request.Request(f"{HERMES_BASE}/v1/info", headers={"User-Agent": "HermesZeroKeyAgent/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print(f" * Service : {data.get('description')}")
        print(f" * Docs    : {data.get('docs')}")
        for ep in data.get("endpoints", [])[:5]:
            sol_acc = next((a for a in ep.get("accepts", []) if a.get("network") == "solana"), {})
            fee_payer = (sol_acc.get("extra") or {}).get("feePayer", "N/A")
            bp = str(ep.get("basePrice", "3000"))
            print(f"   -> {ep.get('method'):4s} {ep.get('path'):22s} | Base Price: {bp} atomic USDC | Gasless FeePayer: {fee_payer[:12]}...")
    return data

def trigger_live_x402_quote_challenge():
    print("\n" + "=" * 76)
    print(" [2] EXECUTING LIVE x402 CHALLENGE HANDSHAKE (POST /v1/swap/quote)")
    print("=" * 76)
    payload = json.dumps({
        "inputMint": SOL_MINT,
        "outputMint": USDC_MINT,
        "amount": "250000000",
        "slippageBps": 50
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{HERMES_BASE}/v1/swap/quote",
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "HermesZeroKeyAgent/1.0"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f" * HTTP {resp.status}: {resp.read().decode('utf-8')[:400]}")
    except urllib.error.HTTPError as he:
        body = he.read().decode("utf-8", errors="replace")
        print(f" * Received Official x402 Status : HTTP {he.code} ({he.reason})")
        try:
            parsed = json.loads(body)
            print(" * Live x402 Payment Challenge from hermes.swap.io:")
            print(json.dumps(parsed, indent=2)[:1200])
        except Exception:
            print(f" * Raw 402 Body: {body[:600]}")

if __name__ == "__main__":
    discover_x402_endpoints()
    trigger_live_x402_quote_challenge()
