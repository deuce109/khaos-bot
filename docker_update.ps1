docker build ./ -t ip-bot:latest
if ($?) {
    docker service update discord_ip-bot --force
    if ($?) {
        docker container prune --force
        docker image prune --force
    }
}