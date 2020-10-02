Manifests in this directory should be applied using the [kustomize][]
command, like this:

```
kustomize build | oc apply -f-
```

Many of the manifests can be applied using `oc apply -k <directory>`, but
where the syntax of `oc apply -k` and `kustomize` have diverged we will
prefer the `kustomize` syntax.

[kustomize]: https://github.com/kubernetes-sigs/kustomize
