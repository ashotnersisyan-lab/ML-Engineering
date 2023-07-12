# Start with MLflow base image
FROM ghcr.io/mlflow/mlflow:v2.4.1

# Expose the required MLflow ports
EXPOSE 5000

# Set the entrypoint command to start the MLflow server
CMD ["mlflow", "server", "--host", "0.0.0.0", "--backend-store-uri", "/mlflow"]
