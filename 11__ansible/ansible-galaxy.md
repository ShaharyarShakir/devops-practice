# 🌌 What is Ansible Galaxy?

##### Ansible Galaxy is:

- A community hub for sharing, discovering, and downloading Ansible roles and collections.

- Think of it like npm for JavaScript or PyPI for Python, but for Ansible automation.

##### 📦 You can:

- Reuse other people’s automation (e.g., install NGINX, Docker, Kubernetes, etc.)

- Publish your own reusable roles or collections

- Standardize and version your automation code for teams or the community

## 🛠️ Why Use Ansible Galaxy?

##### ✅ Benefits:

| Feature            | Benefit                                                           |
| ------------------ | ----------------------------------------------------------------- |
| 🔁 Reusability     | Share and reuse modular automation code (roles/collections)       |
| 🛠️ Standardization | Follows a standard structure → easier to collaborate and maintain |
| 📦 Versioning      | Use specific versions of roles (like a package manager)           |
| 🧑‍🤝‍🧑 Collaboration   | Open-source and team-ready                                        |
| 🚀 Faster DevOps   | No need to reinvent the wheel for common setups                   |

## 🚀 How to Create Your Own Role for Galaxy

##### Here's a step-by-step guide to create and publish your own role on Galaxy:

### 🔨 1. Install Ansible

- Make sure you have Ansible installed:

```bash
ansible --version
```

### 🧱 2. Create a Role Skeleton

- Use the built-in ansible-galaxy CLI to generate a new role:

```bash
ansible-galaxy init my_role_name
```

##### This creates a folder structure like:

```bash
my_role_name/
├── defaults/
│   └── main.yml
├── tasks/
│   └── main.yml
├── handlers/
│   └── main.yml
├── meta/
│   └── main.yml
├── README.md
├── ...
```

##### Fill in:

- tasks/main.yml → automation logic

- defaults/main.yml → default variables

- meta/main.yml → metadata like role author, dependencies, etc.

## 🛠 3. Develop Your Role

##### Write your Ansible logic inside the generated folders. For example:

- tasks/main.yml:

```yaml
- name: Install nginx
  apt:
    name: nginx
    state: present
```

## 📤 4. Publish to Ansible Galaxy

##### a. Create an account:

- Go to https://galaxy.ansible.com
  -Log in with your GitHub account.

##### b. Link your GitHub repo

- Your role must be in a public GitHub repo

- Name it like: ansible-role-<your_rolename>

- For example: myusername/ansible-role-nginx

##### c. Import it on Galaxy:

- Go to your Ansible Galaxy profile

- Click "My Content" → "Add Content"

- Import the role from GitHub

- Galaxy will auto-scan your repo, version it, and list it publicly.

## 🧪 5. Use Your Published Role

##### Anyone (including you) can install it like this:

```bash
ansible-galaxy install myusername.nginx
```

##### And use it in a playbook:

```yaml
- hosts: all
  roles:
    - myusername.nginx
```

## 💡 Collections vs Roles

- **Roles**: Individual units of automation logic (classic)

- **Collections**: Bundles of roles, plugins, and modules (modern, more powerful)

###### For most people starting out, **roles are simpler and easier to publish**.

## Summary

| Topic          | Summary                                                              |
| -------------- | -------------------------------------------------------------------- |
| What is it?    | Ansible Galaxy is a hub for sharing automation roles and collections |
| Why use it?    | Promotes reusability, standardization, and faster development        |
| How to use it? | Write roles → publish on GitHub → import to Galaxy                   |
| CLI Tool       | ansible-galaxy helps create and manage roles easily                  |
