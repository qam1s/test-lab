#!/bin/bash

set -e

uv run uvicorn main:app --reload &
SERVER_PID=$!
sleep 1
uv run pytest
kill $SERVER_PID 2>/dev/null
wait $SERVER_PID 2>/dev/null
