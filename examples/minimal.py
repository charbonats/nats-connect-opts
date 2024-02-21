from __future__ import annotations

from nats_contrib.connect_opts import connect, options


async def main() -> None:
    """A simple example of using the connect function."""

    client = await connect(
        # Configure the servers
        options.WithServers(
            [
                "nats://localhost:4222",
                "nats://localhost:4223",
            ]
        ),
        # Configure the reconnect strategy
        options.WithAllowReconnect(
            max_attempts=10,
            delay_seconds=0.5,
        ),
        # Configure the connection name
        options.WithConnectionName("my-connection"),
        # Configure the flusher
        options.WithFlusher(
            queue_size=100,
            timeout_seconds=10,
        ),
    )

    # Close the client
    await client.close()
