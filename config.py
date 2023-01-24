from dynaconf import Dynaconf

settings = Dynaconf(
    environments = True,
    envvar_prefix = "ENV",
    settings_files = ["settings.toml", ".secrets.toml"]
)