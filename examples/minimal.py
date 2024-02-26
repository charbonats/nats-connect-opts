from __future__ import annotations

from nats_contrib.connect_opts import connect, option


async def main() -> None:
    """A simple example of using the connect function."""

    client = await connect(
        # Configure the servers
        option.WithServers(
            [
                "nats://localhost:4222",
                "nats://localhost:4223",
            ]
        ),
        # Configure the reconnect strategy
        option.WithAllowReconnect(
            max_attempts=10,
            delay_seconds=0.5,
        ),
        # Configure the connection name
        option.WithConnectionName("my-connection"),
        # Configure the flusher
        option.WithFlusher(
            queue_size=100,
            timeout_seconds=10,
        ),
    )

    # Close the client
    await client.close()
