# Project 03 — Nginx Reverse Proxy on RHEL 9.8

**A hands-on DevOps project integrating Nginx, Docker, Flask, and MariaDB with SELinux-aware reverse proxy configuration.**

![Platform](https://img.shields.io/badge/Platform-RHEL%209.8-red)
![Nginx](https://img.shields.io/badge/Nginx-1.20.1-green)
![Docker](https://img.shields.io/badge/Docker-29.8.2-blue)
![SELinux](https://img.shields.io/badge/SELinux-Enforcing-orange)
![Testing](https://img.shields.io/badge/Testing-Passed-brightgreen)

## 1. Project Overview

This project demonstrates how to configure Nginx as a reverse proxy on Red Hat Enterprise Linux 9.8 to route HTTP requests to an existing Dockerized Flask calculator application connected to MariaDB.

The project focuses on Linux service management, HTTP networking, reverse proxy configuration, SELinux, firewall administration, application testing, and troubleshooting.

## 2. Objectives

- Install and configure Nginx on RHEL 9.8.
- Understand reverse proxy architecture.
- Forward HTTP traffic from Nginx to a Dockerized Flask backend.
- Configure a custom Nginx listening port.
- Manage services using systemd.
- Configure SELinux for HTTP services.
- Inspect firewall rules using firewalld.
- Test API endpoints through the reverse proxy.
- Analyze Nginx access and error logs.
- Document real troubleshooting experience.

## 3. Architecture

```text
Windows Client / Browser
          |
          | HTTP :8083
          v
+-------------------------+
| RHEL 9.8 VMware Machine |
|                         |
| Nginx Reverse Proxy     |
| Port: 8083              |
+------------+------------+
             |
             | proxy_pass
             | 127.0.0.1:8082
             v
+-------------------------+
| Docker Container        |
| Python Flask API        |
| Internal Port: 5000     |
+------------+------------+
             |
             | Docker Network
             v
+-------------------------+
| MariaDB 11 Container    |
| Calculation History     |
| Persistent Storage      |
+-------------------------+
```

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| RHEL 9.8 | Linux server environment |
| VMware | Virtualization |
| Nginx 1.20.1 | Reverse proxy |
| Docker | Application containerization |
| Flask | Calculator REST API |
| MariaDB 11 | Database |
| SELinux | Mandatory access control |
| firewalld | Network firewall |
| systemd | Service management |
| curl | HTTP endpoint testing |
| Git and GitHub | Version control and documentation |

## 5. Project Structure

```text
03-Nginx-Reverse-Proxy/
├── nginx/
│   └── calculator-proxy.conf
├── docs/
│   └── screenshots/
└── README.md
```

## 6. Nginx Reverse Proxy Configuration

Configuration file: `/etc/nginx/conf.d/calculator-proxy.conf`

```nginx
server {
    listen 8083;
    server_name _;

    access_log /var/log/nginx/calculator_access.log;
    error_log /var/log/nginx/calculator_error.log;

    location / {
        proxy_pass http://127.0.0.1:8082;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Nginx listens on port 8083 and forwards incoming requests to the Flask application through port 8082 on the RHEL host.

The proxy headers preserve information about the original request.

## 7. Installation and Configuration

Install Nginx:

```bash
dnf install nginx -y
```

Verify the installation:

```bash
nginx -v
```

Validate the configuration:

```bash
nginx -t
```

Enable and start the Nginx service:

```bash
systemctl enable --now nginx
```

Check service status:

```bash
systemctl status nginx
```

## 8. SELinux Configuration

SELinux remained in Enforcing mode during this project.

TCP port 8083 was assigned to the `http_port_t` type. Since the port was previously assigned to another type, the existing mapping was changed during the lab.

Check port mappings:

```bash
semanage port -l | grep '^http_port_t'
```

Enable outbound network connections for confined HTTP services:

```bash
setsebool -P httpd_can_network_connect on
```

Verify:

```bash
getsebool httpd_can_network_connect
```

Expected result:

```text
httpd_can_network_connect --> on
```

This boolean permits HTTP services to establish network connections. Production deployments should evaluate more restrictive alternatives when appropriate.

## 9. Firewall Configuration

Firewalld was active on the RHEL virtual machine.

The Nginx port was temporarily enabled using:

```bash
firewall-cmd --zone=public --add-port=8083/tcp
```

Verify runtime access:

```bash
firewall-cmd --zone=public --query-port=8083/tcp
```

At the time of initial testing, this was a runtime rule only. Persistent, source-restricted firewall configuration is part of the final security review.

## 10. Testing and Validation

### Health Check

```bash
curl -i http://127.0.0.1:8083/health
```

Result:

```http
HTTP/1.1 200 OK
Server: nginx/1.20.1
```

```json
{"status":"healthy"}
```

### Calculator API

```bash
curl "http://127.0.0.1:8083/add?a=10&b=5"
```

Response:

```json
{
  "a": 10.0,
  "b": 5.0,
  "operation": "addition",
  "result": 15.0
}
```

### Database Persistence

```bash
curl http://127.0.0.1:8083/history
```

The history endpoint returned the newly created calculation, confirming that the request passed through Nginx and Flask and that MariaDB stored the record successfully.

### Windows Browser Test

The application was also accessed using the RHEL virtual machine's IP address and Nginx port 8083.

## 11. Troubleshooting Experience

### Issue 1 — Nginx Configuration Syntax Error

During configuration, the following error occurred:

```text
unknown log format "error_log"
```

**Cause:** An incorrect Nginx logging directive caused `error_log` to be interpreted as an access-log format.

**Resolution:** Corrected the log directives and validated the configuration using `nginx -t`.

### Issue 2 — Port Conflict

Port 8080 was already occupied by Apache HTTP Server (`httpd`).

**Resolution:** Selected port 8083 for Nginx without stopping Apache or disrupting existing services.

### Issue 3 — SELinux Port Restrictions

Port 8083 was not initially assigned to the HTTP service port type.

**Resolution:** Updated its SELinux port mapping and enabled the required HTTP network-connection boolean.

### Issue 4 — Firewall Persistence

Port 8083 was initially allowed through a runtime-only firewalld rule.

**Follow-up:** Review source-restricted permanent access before finalizing security hardening.

## 12. Monitoring and Logs

Nginx access logs:

```bash
tail -f /var/log/nginx/calculator_access.log
```

Nginx error logs:

```bash
tail -f /var/log/nginx/calculator_error.log
```

Service logs:

```bash
journalctl -u nginx
```

These logs help investigate request failures, HTTP response codes, and service problems.

## 13. Key Learnings

- How a reverse proxy handles incoming HTTP requests.
- How Nginx forwards requests to a containerized application.
- How host and container ports differ.
- How to identify port conflicts on Linux.
- How to configure and troubleshoot systemd services.
- How SELinux affects web services.
- How firewalld runtime and permanent rules differ.
- How to troubleshoot Nginx configuration errors.
- How to verify application and database integration.
- How to inspect HTTP access logs.

## 14. Future Improvements

- Restrict direct Flask backend exposure.
- Make the firewall configuration persistent and limit it to trusted clients.
- Remove unnecessary default Nginx listeners.
- Add HTTPS/TLS for deployments beyond the local lab.
- Configure log rotation and additional monitoring.
- Automate configuration using Ansible.

## 15. Related Project

[Project 02 — Dockerized Python Application](../02-Dockerize-Python-App/README.md)

## 16. Repository

[DevOps Projects — Arun Krishna S](https://github.com/Arunkrishna02/DevOps-Projects)

---

**Project outcome:** Successfully configured and tested an Nginx reverse proxy for a Dockerized Flask application backed by MariaDB on RHEL 9.8, including SELinux administration, HTTP logging, and practical troubleshooting.
