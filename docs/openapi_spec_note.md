# OpenAPI Spec Note

`https://api.delx.ai/spec/openapi.json` did not return valid JSON during the latest health check.

## Observed result
- discovery endpoints worked
- OpenAPI endpoint returned a non-JSON payload / parse failure

## Implication
Contributors should treat discovery docs as the stable starting point and validate the OpenAPI spec endpoint before depending on it in automation.
