deploy:
		chmod +x ./scripts/*.sh
		cd scripts && ./run-docker.sh local