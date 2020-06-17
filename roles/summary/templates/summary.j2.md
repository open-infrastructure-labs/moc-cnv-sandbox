# Configuration summary

## install_config

```
{{ install_config | to_yaml }}
```

{% for host in groups.managers + groups.workers %}
## {{ host }}

### {{ host }} Interface configuration

```
{{ hostvars[host].ip_addr.stdout }}
```

### {{ host }} Route configuration

```
{{ hostvars[host].ip_route.stdout }}
```

### {{ host }} Reverse lookup primary address

```
{{ hostvars[host].reverse_dns.stdout }}
```

### {{ host }} Running containers

{{ hostvars[host].crictl_ps.stdout_lines | length }} containers total

```
{{ hostvars[host].crictl_ps.stdout }}
```

### {{ host }} Listening TCP ports

{{ hostvars[host].tcp_ports.stdout_lines | length }} listening ports

```
{{ hostvars[host].tcp_ports.stdout }}
```

{% endfor %}

## Install log

```
{{ lookup('file', 'openshift-install.log') }}
```
