# Contributing to KAIScaler

Thank you for your interest in contributing to KAIScaler! We welcome contributions of all kinds, including bug fixes, new features, documentation improvements, and test enhancements.

## How to Contribute

### 1. Fork the Repository
Go to the [KAIScaler GitHub repository](https://github.com/pirate0071kaiscaler) and click the **Fork** button.

### 2. Clone Your Fork
```sh
git clone https://github.com/pirate0071/kaiscaler.git
cd kaiscaler
```

### 3. Create a New Branch
```sh
git checkout -b feature-branch-name
```
Use a descriptive branch name (e.g., `fix-metrics-endpoint` or `add-dashboard-feature`).

### 4. Install Dependencies
```sh
pip install -r requirements.txt
```

### 5. Make Your Changes
- Follow best practices for Python, Kubernetes, and Helm.
- Ensure your code is **well-documented** and **follows PEP8**.

### 6. Run Tests
Run unit tests before submitting your changes:
```sh
pytest tests/
```

### 7. Commit Your Changes
```sh
git add .
git commit -m "feat: add predictive scaling to operator"
```
Use conventional commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation updates
- `test:` for adding or improving tests

### 8. Push Your Changes
```sh
git push origin feature-branch-name
```

### 9. Open a Pull Request (PR)
1. Navigate to your fork on GitHub.
2. Click **New Pull Request**.
3. Fill out the PR template and describe your changes.
4. Submit the PR for review.

### 10. Code Review
- A maintainer will review your PR.
- If changes are requested, make updates and push again.

## Contribution Guidelines
**Write clear, modular, and efficient code.**  
**Ensure tests pass before submission.**  
**Write meaningful commit messages.**  
**Follow Kubernetes and Helm best practices.**  
**Respect existing code structure and documentation.**

## Need Help?
If you have questions, feel free to open an **issue** or reach out via [GitHub Discussions](https://github.com/pirate0071/kaiscaler/discussions).

Happy coding!
