# Deploying the App

The app can be deployed to the hosts listed in the `inventory.yaml` file using the `playbook.yaml` Ansible playbook.

- Set up SSH access to each host.
- Run the following command.

```bash
$ ansible-playbook -i <inventory file> playbook.yaml
```

The app can then be accessed on port 5000 of each host.
