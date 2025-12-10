# Custom_CUBE_simple_node

## Cloning this repository
If you see an error like `Permission denied (publickey)` while cloning with the SSH URL (`git@github.com:...`), it means your local machine is not authenticated with GitHub over SSH. You can fix this in either of two ways:

1. **Use HTTPS instead of SSH**
   ```bash
   git clone https://github.com/<OWNER>/<REPO>.git
   ```
   Replace `<OWNER>/<REPO>` with the actual GitHub path.

2. **Add an SSH key to your GitHub account**
   - Generate a key if you do not have one already:
     ```bash
     ssh-keygen -t ed25519 -C "your_email@example.com"
     ```
   - Add the public key (the `.pub` file) to your GitHub account settings under **SSH and GPG keys**.
   - Start the SSH agent and add your key:
     ```bash
     eval "$(ssh-agent -s)"
     ssh-add ~/.ssh/id_ed25519
     ```
   - Retry cloning with the SSH URL.

If you are working inside a container or CI runner, make sure the SSH key is available in that environment or prefer the HTTPS URL, which does not require SSH credentials for public repositories.
