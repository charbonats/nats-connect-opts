# NATS Connect Opts

!!! warning "This is not an official NATS project"
    This is a personal project and is not endorsed by the NATS.io community. It is not guaranteed to be maintained or supported.

!!! bug "This is an experimental project"
    This project is a prototype and should not be used for anything serious. It is not tested, nor is it guaranteed to be correct.

The [nats.go](https://github.com/nats-io/nats.go) package ([Go](https://go.dev/) client for NATS) provides a simple way to configure connect options using the [Options pattern](https://golang.cafe/blog/golang-functional-options-pattern.html)

This project is an attempt to implement the same API in Python.

> Note: This may not be Pythonic and may not be the best way to do it in Python. This is just an experiment.


## References

- The [nats.aio.Client.connect method from nats-py](https://nats-io.github.io/nats.py/modules.html#nats.aio.client.Client.connect).


## How to install

<!-- termynal -->

```bash
$ pip install git+https://github.com/charbonnierg/nats-connect-opts.git
```

## Example usage

``` py linenums="1" title="examples/minimal.py"
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
```

## Other works

- [NATS Micro](https://charbonats.github.io/nats-micro)

- [NATS Request Many](https://charbonats.github.io/nats-request-many)
