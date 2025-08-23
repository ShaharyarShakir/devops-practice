# Helm Basics

- Helm is a package manager for Kubernetes.
- It allows you to define, install, and manage Kubernetes applications using **Charts**.

## Installing a Chart

- Install a chart from a repository:

```bash
helm repo add <repo-name> <repo-url>
helm install <release-name> <repo-name>/<chart-name>
```

- Install a chart from a local directory:

```bash
helm install <release-name> ./<chart-directory>
```

- Install with custom values:

```bash
helm install <release-name> ./<chart-directory> -f values.yaml
```

## Upgrading a Release

- Upgrade to a new chart version or apply changes:

```bash
helm upgrade <release-name> ./<chart-directory>
```

- Upgrade with custom values:

```bash
helm upgrade <release-name> ./<chart-directory> -f values.yaml
```

## Uninstalling a Release

- Remove a deployed release:

```bash
helm uninstall <release-name>
```

## Listing Releases

- List all Helm releases in the current namespace:

```bash
helm list
```

- List releases in all namespaces:

```bash
helm list -A
```

## Checking History and Rollback

- View revision history of a release:

```bash
helm history <release-name>
```

- Rollback to a specific revision:

```bash
helm rollback <release-name> <revision-number>
```
- packaging to upload
```bash
helm package <nameofpackage>
```
## Useful Flags

- --namespace <name> → Specify a namespace for install/upgrade/uninstall.

- --create-namespace → Create the namespace if it doesn't exist.

- --dry-run → Simulate the command without applying changes.
