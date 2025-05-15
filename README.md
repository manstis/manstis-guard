# `llama-stack` configuration

## External Configuration

### `llama-stack` run configuration
```
version: '2'
image_name: ollama
apis:
- agents
- datasetio
- eval
- inference
- safety
- scoring
- telemetry
- tool_runtime
- vector_io
providers:
  agents:
  - provider_id: meta-reference
    provider_type: inline::meta-reference
    config:
      persistence_store:
        type: sqlite
        namespace: null
        db_path: ${env.SQLITE_STORE_DIR:~/.llama/distributions/ollama}/agents_store.db
  inference:
  - provider_id: ollama
    provider_type: remote::ollama
    config:
      url: ${env.OLLAMA_URL:http://localhost:11434}
  safety:
  - provider_id: manstis-guard
    provider_type: inline::manstis-guard
    config:
      model_id: ${env.INFERENCE_MODEL}
...
models:
- metadata: {}
  model_id: ${env.INFERENCE_MODEL}
  provider_id: ollama
  model_type: llm
shields:
- shield_id: manstis-guard-shield
  provider_id: manstis-guard
...
external_providers_dir: /home/manstis/.llama/external_config

```
### External configuration folder structure
```
./external_config/
└── inline
    └── safety
      └── manstis-guard.yaml
```
### Definition of `manstis-guard.yaml`
```
module: manstis_guard
config_class: manstis_guard.config.ManstisGuardConfig
pip_packages: []
api_dependencies:
  - inference
optional_api_dependencies: []
```
