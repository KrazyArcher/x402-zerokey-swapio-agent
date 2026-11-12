# x402-ZeroKey-SwapIO-Agent

Autonomous AI Agents on Solana Pay 0.003 USDC Per Quote via HTTP 402 (x402) + Swap.io (hermes.swap.io) - Gasless, Zero Sign-Ups, Zero Subscriptions.

## The Problem: Why Static API Keys Break Autonomous AI Agents
Traditional crypto and DEX aggregator APIs force developers into -/month subscriptions, credit card KYC, and static API_KEY secrets.

## The Solution: Swap.io Hermes (x402 Protocol on Solana)
Swap.io (https://swap.io / https://hermes.swap.io) exposes the Routhex multi-provider routing engine (Jupiter, DFlow, OKX DEX) behind HTTP 402 Payment Required:
1. Zero API Keys: Send a POST request directly to https://hermes.swap.io/v1/swap/quote
2. HTTP 402 Challenge: hermes.swap.io responds with atomic USDC price (3000 = .003 USDC), recipient BPz2u6eoWLervxEqfpsMCVmKk7h6fEVsd7L5rvEibMfD, and gasless feePayer 2wKupLR9q6wXYppw8Gr2NvWxKBUqm4PPJKkQfoxHDBg4.
3. 100% Gasless for Agents: The facilitator covers the Solana network fee - your agent wallet only needs USDC (zero SOL required).
4. On-Chain Receipt: Every paid 200 OK returns an on-chain receipt in X-PAYMENT-RESPONSE. Failed calls are never charged.

## Quickstart
Run: python x402_swapio_agent.py
