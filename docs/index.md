---
layout: home
title: Home
---

# Base Python Data Science Monorepo

This repository is both:

1. a **learning platform** for understanding data science fundamentals from first principles
2. an **engineering platform** with reusable libraries, APIs, messaging services, OpenAPI specs, Docker assets, Helm charts, and CI/CD automation

## Audience

### Users
Explore examples, run algorithms locally, and call functionality via API or messaging interfaces.

### Developers
Extend the core libraries, maintain multi-language implementations, and evolve OpenAPI-driven services and clients.

### Administrators / Operators
Build container images, deploy service workloads (including Helm-based deployment for Node Express), and follow CI/CD release workflows.

## Repository structure

- `src/data-scratch-library`: core Python data science package (`dsl`)
- `src/data-scratch-matplotlib`: visualization examples
- `src/data-scratch-scrape`: scraping/data collection examples
- `src/data-scratch-amqp`: AMQP execution service
- `src/data-scratch-mqtt`: MQTT execution service
- `src/data-scratch-node-library`: TypeScript/Node implementation
- `src/data-scratch-cpp-library`: C++ implementation
- `src/rest-scratch-flask`: Flask REST API
- `src/rest-scratch-node-express`: OpenAPI-driven Node Express REST server + Helm chart
- `src/rest-scratch-pistache`: OpenAPI-driven C++ Pistache server
- `src/rest-scratch-rust`: OpenAPI-driven Rust server
- `src/rest-client-ts-node`: OpenAPI-driven TypeScript Node client

## Start here

For full onboarding, setup, validation commands, and operations details, read the root repository guide:

- [`README.md`](../README.md)

Then follow module-level README files for component-specific setup and usage.

## Philosophy

- Prefer explainability over brevity.
- Prefer explicit instructions over clever shortcuts.
- Assume technical readers are new to this repository's structure.
