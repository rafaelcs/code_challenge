import docker


def run_docker_container(cmd: str):
    client = docker.from_env(version="auto")
    container = client.containers.run(
        "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli", f"{cmd}"
    )
    return container
