from typing import Any

from manstis_guard.config import ManstisGuardConfig

async def get_provider_impl(
        config: ManstisGuardConfig,
        deps: dict[str, Any],
):
    from manstis_guard.safety import ManstisGuardImpl

    assert isinstance(config, ManstisGuardConfig), f"Unexpected config type: {type(config)}"

    impl = ManstisGuardImpl(config, deps)
    await impl.initialize()
    return impl
