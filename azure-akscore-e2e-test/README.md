# Azure-like E2E (0-cost local): ADF preproc → Python load → K8s CronJob → GitHub Actions → Argo CD

- App chart: `charts/myapp`
- Data-loader CronJob: `charts/data-loader`
- GHCR CI: `.github/workflows/ci-ghcr*.yaml`
- Argo CD apps: `manifests/argocd/*.yaml`
- ADF-like copy: `.github/workflows/adf-like.yaml` + `tools/adf_like_copy.py`
