# 🌍 Terraform Basics

## 📘 What Is Terraform?

[Terraform](https://www.terraform.io/) is an open-source Infrastructure as Code (IaC) tool created by [HashiCorp](https://www.hashicorp.com/). It lets you define, provision, and manage your cloud infrastructure using simple, declarative configuration files written in **HCL (HashiCorp Configuration Language)**.

Instead of manually creating resources like servers or databases via a cloud provider's console, you write code to define **what** your infrastructure should look like — and Terraform takes care of creating it.

---

## 🤔 Why Use Terraform?

- ✅ **Infrastructure as Code (IaC):** Your infrastructure becomes version-controlled, auditable, and reproducible — just like software.
- 🌐 **Multi-Cloud Support:** Works with AWS, Azure, GCP, and many others using providers.
- 🔁 **Automation:** Easily re-create environments or destroy them in seconds.
- 🔄 **Idempotency:** Terraform will only make the changes needed — no more, no less.
- 👥 **Team-Friendly:** Share `.tf` files across teams for consistent infrastructure.

---

# ⚔️ Terraform vs Ansible

## Both **Terraform** and **Ansible** are popular tools in the DevOps and infrastructure automation world — but they solve different problems

## 📘 Overview

| Feature          | Terraform                        | Ansible                             |
| ---------------- | -------------------------------- | ----------------------------------- |
| Tool Type        | Infrastructure as Code (IaC)     | Configuration Management            |
| Language         | HCL (declarative)                | YAML (declarative & procedural)     |
| Purpose          | Provision infrastructure         | Configure existing infrastructure   |
| Agent Required   | No                               | No                                  |
| State Management | Yes (with state files)           | No (stateless by default)           |
| Idempotent       | Yes                              | Yes (if playbooks are written well) |
| Execution Model  | Plan → Apply                     | Imperative Playbook Runs            |
| Cloud-Native     | Strong support (AWS, GCP, Azure) | Supported via modules/integration   |

---

## 🔧 What Is Terraform?

Terraform is an **Infrastructure as Code** tool used to **provision and manage infrastructure** (like VMs, networks, storage) across cloud providers.

### ✅ Key Use Cases:

- Create cloud infrastructure (AWS/GCP/Azure)
- Manage Kubernetes clusters
- Maintain infrastructure state over time

### 🧩 Example Use:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
}
```

## ⚙️ Common Terraform Commands

### 📦 Initialize Terraform

```bash
terraform init
```

### 🧠 Preview Infrastructure Changes

```bash
terraform plan
```

- Shows what Terraform will do before it makes any changes.

### 🚀 Apply the Configuration

```bash
terraform apply
```

- Creates or updates the infrastructure as defined in your **.tf** files.

### 🧹 Destroy Infrastructure

```bash
terraform destroy
```

- Removes all resources defined in the Terraform configuration.

### 🛠 Format Code

```bash
terraform fmt
```

- Formats your Terraform code for consistency and readability.

### 🔎 Validate Configuration

```bash
terraform validate
```

- Checks whether the configuration is syntactically valid.
