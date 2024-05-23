# How to update the helm chart

1. Update the template files in `templates/`
2. Update the version in `Chart.yaml` and `values.yaml`
3. Run `helm package elo-indexserver-client-example-batchprocessing/` to create a new `*.tgz` file
4. Run `helm repo index .` to update the `index.yaml` file

## How to install the local chart to a cluster

```
helm install --namespace <yourNamespace> --create-namespace -f custom-values.yaml elo-indexserver-client-example-batchprocessing ./elo-indexserver-client-example-batchprocessing --kubeconfig ~/your_kubeconfig.yml
```

## How to uninstall the chart
```
helm uninstall elo-indexserver-client-example-batchprocessing --namespace <yourNamespace> --kubeconfig ~/your_kubeconfig.yml
kubectl delete namespace <yourNamespace> # if you want to delete the namespace as well
```
