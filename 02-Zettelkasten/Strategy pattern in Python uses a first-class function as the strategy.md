---
aliases: [Strategy in Python, Python Strategy pattern]
---

This is the idiomatic Python implementation of the [[The Strategy pattern makes algorithms interchangeable by hiding each behind a common interface|Strategy pattern]]. In Python functions are objects, so a strategy is <mark style="background: yellow">just a function you pass around</mark> — no interface, no abstract base class, no concrete strategy classes.

### Project structure

```
payments/
    __init__.py
    protocol.py     # PaymentStrategy Protocol + type alias
    strategies.py   # concrete fns (stateless) and classes (stateful)
    registry.py     # _strategies dict + resolve()
    service.py      # CheckoutService (Context)
routes/
    orders.py       # FastAPI endpoint — thin HTTP layer
```

`protocol.py` is imported by everything else. `strategies.py` imports from `protocol.py` only — never the reverse. This keeps the dependency direction clean and avoids circular imports.

---

### The contract — `protocol.py`

```python
from typing import Callable, Protocol

# simple alias — works for stateless functions
PaymentStrategy = Callable[["Order"], None]

# explicit Protocol — works for both functions and callable classes
class PaymentStrategyProtocol(Protocol):
    def __call__(self, order: "Order") -> None: ...
```

Use `Callable` for type hints throughout. `Protocol` adds a named contract for documentation and stricter static analysis — both satisfy the same slot.

---

### Concrete strategies — `strategies.py`

Stateless strategies are plain functions. Stateful strategies are `@dataclass` classes with `__call__` — <mark style="background: cyan">callable like a function, but carrying their own state</mark>:

```python
from dataclasses import dataclass
from .protocol import PaymentStrategy

def credit_card(order: "Order") -> None:
    ...   # stateless — plain function is enough

def paypal(order: "Order") -> None:
    ...   # stateless — plain function

@dataclass
class CryptoPayment:
    wallet: "Wallet"          # needs state → dataclass + __call__

    def __call__(self, order: "Order") -> None:
        ...   # use self.wallet — still satisfies PaymentStrategy
```

`CheckoutService` cannot tell the difference between `credit_card` and `CryptoPayment()` — both are callable and both satisfy `PaymentStrategy`.

---

### Resolver — `registry.py`

```python
from .protocol import PaymentStrategy
from .strategies import credit_card, paypal, CryptoPayment

_strategies: dict[str, PaymentStrategy] = {
    "card":   credit_card,
    "paypal": paypal,
    "crypto": CryptoPayment(wallet=default_wallet),
}

def resolve(payment_type: str) -> PaymentStrategy:
    strategy = _strategies.get(payment_type)
    if strategy is None:
        raise ValueError(f"Unknown payment type: {payment_type}")
    return strategy
```

---

### Context — `service.py`

```python
from dataclasses import dataclass
from .protocol import PaymentStrategy

@dataclass
class CheckoutService:
    _pay: PaymentStrategy

    def checkout(self, order: "Order") -> None:
        self._pay(order)        # no if/else
```

`@dataclass` generates `__init__` — same philosophy as Lombok `@RequiredArgsConstructor` in Java.

---

### Wiring it together — service + endpoint

```python
# payments/order_service.py
from .registry import resolve
from .service import CheckoutService

def checkout(order_id: int, payment_type: str) -> None:
    order = ...                                   # load order
    strategy = resolve(payment_type)              # "paypal" → paypal fn
    CheckoutService(strategy).checkout(order)
```

```python
# routes/orders.py
from fastapi import APIRouter
from payments.order_service import checkout

router = APIRouter(prefix="/orders")

@router.post("/{order_id}/checkout")
def checkout_endpoint(order_id: int, payment_type: str) -> None:
    checkout(order_id, payment_type)              # thin — delegate to service
```

---

### Read more
- [[The Strategy pattern makes algorithms interchangeable by hiding each behind a common interface]]
- [[Strategy pattern in Kotlin uses a function type instead of an interface]]
- [[Strategy pattern in Java is an interface implemented by interchangeable algorithm classes]]
- [[First-class functions treat functions as values that can be passed, stored, and returned]]
