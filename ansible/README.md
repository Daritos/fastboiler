# Setup with ansible

Playbooks for configuring dependencies and deploying the application (based on Ubuntu)

## Get started

Install required dependencies

```bash
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install git ansible -y
```

Now run the playbook from the repository

```bash
ansible-playbook --ask-become-pass -k deploy_playbook.yml -u <insert_your_username_here>