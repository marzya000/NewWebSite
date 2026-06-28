#!/bin/bash
set -e

echo "Starting entrypoint..."

echo "Waiting for PostgreSQL at $POSTGRES_HOST:$POSTGRES_PORT..."
until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER"; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done
echo "PostgreSQL is ready!"


echo "Waiting for Redis at $REDIS_HOST:$REDIS_PORT..."
until redis-cli -h "$REDIS_HOST" -p "$REDIS_PORT" ping | grep -q PONG; do
  echo "Redis is unavailable - sleeping"
  sleep 1
done
echo "Redis is ready!"


exec "$@"
