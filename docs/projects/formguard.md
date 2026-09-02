[← Back to profile](../../README.md)

# FormGuard

![Repo](https://img.shields.io/badge/Repo-Private-red?style=for-the-badge&logo=github)
[![Contact Me](https://img.shields.io/badge/Contact%20Me-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniel-shalom-13987a1a/)

**Automated verification tool for investor subscription and tax forms.**

<a href="../../assets/FormGuard.gif"><img src="../../assets/FormGuard.gif" width="100%" /></a>

## Overview

Verifying investor subscription and tax forms (W-8BEN, W-8BEN-E, W-9, and similar) by hand is slow, repetitive, and error-prone — every field, signature, and date needs to be checked against compliance rules, and a single missed detail can hold up onboarding. FormGuard automates that review: batch-upload a set of forms, run them through OCR, and get back an intelligent, field-level validation pass instead of a manual line-by-line check.

## Goals

- Cut the hours-per-cycle spent on manual review of investor and tax forms.
- Catch missing fields, invalid formats, and inconsistencies before they become onboarding blockers.
- Give compliance/ops teams a repeatable, auditable check instead of ad hoc manual review.

## Key Features

- **Batch upload** — process many investor forms in one pass instead of one at a time.
- **AWS Textract OCR** — extracts structured field data directly from scanned/uploaded forms.
- **Intelligent validation** — checks extracted fields against form-specific rules (required fields, format checks, cross-field consistency) for W-8BEN, W-8BEN-E, W-9, and related forms.
- **Review-ready output** — flags issues for a human reviewer instead of silently accepting or rejecting.

## Potential Use Cases

- Fund administrators and transfer agents processing investor subscription documents at volume.
- Compliance/KYC teams that need a first-pass automated check before manual sign-off.
- Any workflow that currently relies on manually reviewing standardized tax/compliance forms (W-8BEN, W-8BEN-E, W-9).

## How It Works

1. Upload a batch of investor forms (subscription documents, tax forms).
2. AWS Textract OCR extracts the structured field data from each document.
3. FormGuard runs field-level validation against the rules for that form type.
4. Results are surfaced for review — flagged issues alongside forms that passed validation cleanly.

## Tech Stack

AWS Textract for OCR, with a batch-processing pipeline and rules-based validation layer built around it.

---

This is a private repository. [Contact me on LinkedIn](https://www.linkedin.com/in/daniel-shalom-13987a1a/) for a walkthrough or access.

[← Back to profile](../../README.md)
