# Security Policy

## Scope

This repository is a **public documentation and demonstration portfolio** for MovaCore.

It intentionally excludes:

- Production source code from the private repository
- Environment files, API keys, tokens, passwords
- Customer PII, supplier credentials, payment data
- Internal hostnames, VPS IPs, SSH configs, database dumps
- Proprietary commercial business logic copied verbatim

## Reporting a Vulnerability

If you discover a security issue in the **demonstration code** published here, open a GitHub issue labeled `security` with a clear description and reproduction steps that do **not** include real secrets.

If you believe you have found a vulnerability in a **live MovaCore deployment**, do not post exploit details publicly. Contact the repository owner privately.

## Secrets Hygiene

Demonstration examples read configuration from environment variables. Use `.env.example` with placeholder values only. Never commit a real `.env`.

## Responsible Documentation

Architecture docs describe patterns at a level useful for engineering review without enabling unauthorized access to private systems.
