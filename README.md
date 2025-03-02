# Check Python Types Annotations

This project demonstrates type checking in Python scripts using [Pyright](https://github.com/microsoft/pyright). It includes pre-prepared code examples validated with Pyright. The project is part of Homework #3 for the OTUS course and is intended for educational purposes.

## Features

- **Code Examples**: Python scripts with type annotations to showcase Pyright.
- **Makefile**:
  - `make local`: Runs type checking locally.
  - `make typing`: Runs type checking in a Docker container.
- **MIT License**: Open-source and free to use.

## Prerequisites

- Python 3.11 or higher.
- Docker and Docker Compose (for `make typing`).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/speculzzz/check-pytypes-annotations.git
   cd check-pytypes-annotations
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. For Docker usage, ensure Docker and Docker Compose are installed.

## Usage

### Local Type Checking

Run type checking locally:
```bash
make local
```

### Type Checking in Docker

Run type checking in a Docker container:
```bash
make typing
```

This will:
1. Build a Docker image.
2. Run Pyright inside the container.
3. Output the results.
4. Shut down the container.

## Project Structure

- `*/task.py`: Python scripts with type annotations.
- `Dockerfile`: Docker configuration.
- `docker-compose.yml`: Docker Compose setup.
- `Makefile`: Automation for local and Docker-based type checking.
- `pyproject.toml`: Configuration for build tools and type checkers.
- `requirements.txt`: Project dependencies.
- `LICENSE`: MIT License.
- `README.md`: This file.

## License

MIT License. See [LICENSE](LICENSE) for details.

## Author

- **speculzzz** (speculzzz@gmail.com)

---

Feel free to use it!